# Les épreuves

## Coefficients des épreuves

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "A simple radial chart with embedded data.",
  "data": {
    "values": [
      {"Matière": "Spe1", "Coef": 16, "Année de passage": "Terminale"},
      {"Matière": "Spé2", "Coef": 16, "Année de passage": "Terminale"},
      {"Matière": "Spé3", "Coef": 8, "Année de passage": "Première"},
      {"Matière": "Français", "Coef": 10, "Année de passage": "Première"},
      {"Matière": "Philo", "Coef": 8, "Année de passage": "Terminale"},
      {"Matière": "Grand Oral", "Coef": 10, "Année de passage": "Terminale"},
      {"Matière": "Sciences", "Coef": 6, "Année de passage": "1ère et Term"},
      {"Matière": "LVA", "Coef": 6, "Année de passage": "1ère et Term"},
      {"Matière": "LVB", "Coef": 6, "Année de passage": "1ère et Term"},
      {"Matière": "Hist-Géo", "Coef": 6, "Année de passage": "1ère et Term"},
      {"Matière": "EPS", "Coef": 6, "Année de passage": "Terminale"},
      {"Matière": "EMC", "Coef": 2, "Année de passage": "Terminale"}
      ]
    },
    "layer": [
      {"mark": {"type": "arc", "innerRadius": 20, "stroke": "#fff"}}, 
      {"mark": {"type": "text", "radiusOffset": 30},"encoding": {"text": {"field": "Matière", "type": "nominal"}}},
      {"mark": {"type": "text", "radiusOffset": -10},"encoding": {"text": {"field": "Coef", "type": "nominal"},"fill": {"value": "#000"}}}       
      ],
    "encoding": {
      "tooltip": [{"field": "Matière", "type": "nominal" }, { "field": "Coef", "type": "quantitative"}, {"field": "Année de passage", "type": "nominal" }],
      "theta": {"field": "Coef", "type": "quantitative", "stack": true},
      "radius": {"field": "Coef", "scale": {"type": "sqrt", "zero": true, "rangeMin": 20}},
      "color": {"field": "Coef", "type": "nominal", "legend": null}
    }
  }
```
