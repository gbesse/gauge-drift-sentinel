import unittest
from gauge_drift_sentinel import run

def check(b):return run({'baseline':10,'shift_threshold':.5,'batches':[dict(id='a',**b)]})['batches'][0]
class DomainTests(unittest.TestCase):
 def test_gauge_shift_not_process_shift(self):
  r=check({'products':[12,12],'references':[{'true':5,'measured':7}]});self.assertEqual(r['corrected_shift'],0);self.assertEqual(r['state'],'within_declared_bounds')
 def test_process_shift_detected(self):
  r=check({'products':[13,13],'references':[{'true':5,'measured':7}]});self.assertEqual(r['state'],'guaranteed_shift')
 def test_missing_reference_is_unknown(self):self.assertIsNone(check({'products':[100]})['corrected_shift'])
 def test_uncertainty_retained(self):
  r=check({'products':[10.6],'references':[{'true':5,'measured':5}],'product_error_bound':.2});self.assertEqual(r['state'],'ambiguous_shift')
 def test_negative_shift(self):self.assertEqual(check({'products':[8],'references':[{'true':5,'measured':5}]})['state'],'guaranteed_shift')
 def test_invalid_bound(self):
  with self.assertRaises(ValueError):check({'products':[1],'product_error_bound':-1})
