from statistics import mean
from .common import number,unique_ids

def run(data):
    batches=data['batches'];baseline=number(data['baseline'],-1e12,1e12);threshold=number(data['shift_threshold'],0,1e12)
    if len(batches)>10000:raise ValueError('size')
    unique_ids(batches);out=[]
    for b in batches:
        products=b['products'];refs=b.get('references',[])
        if not products or len(products)>10000 or len(refs)>10000:raise ValueError('samples')
        for v in products:number(v,-1e12,1e12)
        raw=mean(products);pe=number(b.get('product_error_bound',0),0,1e12);re=number(b.get('reference_error_bound',0),0,1e12)
        if not refs:
            out.append({'id':b['id'],'state':'unidentified_without_reference','raw_shift':raw-baseline,'corrected_shift':None});continue
        bias=[]
        for r in refs:bias.append(number(r['measured'],-1e12,1e12)-number(r['true'],-1e12,1e12))
        offset=mean(bias);shift=raw-offset-baseline;lo=shift-pe-re;hi=shift+pe+re
        guaranteed=lo>threshold or hi<-threshold;stable=-threshold<=lo and hi<=threshold
        out.append({'id':b['id'],'state':'guaranteed_shift' if guaranteed else 'within_declared_bounds' if stable else 'ambiguous_shift','raw_shift':raw-baseline,'reference_bias':offset,'corrected_shift':shift,'shift_interval':[lo,hi],'product_count':len(products),'reference_count':len(refs)})
    return {'batches':out,'uncertainty':'caller-declared absolute error bounds, not statistical confidence intervals'}
