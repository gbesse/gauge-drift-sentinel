# gauge-drift-sentinel

## Français

Séparer dérive de mesure et dérive de procédé avec des pièces témoins.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m gauge_drift_sentinel examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Soustrait le biais mesuré sur pièces de référence à la moyenne du lot, puis propage les bornes d’erreur déclarées. Distingue dérive certaine, intervalle compatible et absence d’identification sans témoin. Complète FabTrace : aucun classement causal à partir de simples corrélations.

### Limites

Le biais doit être commun aux références et produits et stable dans le lot ; bornes fournies, pas intervalles de confiance ni étude Gage R&R. Aucun étalonnage physique.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Separate gauge drift from process drift using reference parts.

Synthetic data; no network access or secret required.

```sh
python -m gauge_drift_sentinel examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Subtracts reference-part bias from batch mean, then propagates declared error bounds. Separates guaranteed shift, compatible interval and lack of identification without a reference. Complements FabTrace without causal classification from mere correlations.

### Limits

Bias must be shared by reference and product and stable within the batch; supplied bounds, not confidence intervals or a Gage R&R study. No physical calibration.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Separar deriva de medición y de proceso mediante piezas de referencia.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m gauge_drift_sentinel examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Resta el sesgo de piezas de referencia de la media del lote y propaga cotas de error declaradas. Separa deriva garantizada, intervalo compatible y falta de identificación sin referencia. Complementa FabTrace sin inferir causas de correlaciones.

### Límites

El sesgo debe ser común a referencia y producto y estable en el lote; cotas dadas, no intervalos de confianza ni estudio Gage R&R. Sin calibración física.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc321.htm
- https://github.com/gbesse/fabtrace
