

# Soil Sensor Data YARRRML mappings

 - YARRRML genertaed using Matey (https://rml.io/yarrrml/matey/#)

```python
prefixes:
 foo: "http://w3id.org/def/foo#"
 rdf: "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
 xsd: "http://www.w3.org/2001/XMLSchema#"
 sosa: "http://www.w3.org/ns/sosa/"
 schema: "http://schema.org/"
 skos: "http://www.w3.org/2004/02/skos/core#"

mappings:
  Observation:
    sources:
      - ['soil.csv~csv']
    s: http://w3id.org/def/foo#$(Identifier)
    po:
      - [a, foo:Observation]
      - [foo:ites, $(Site)]
      - [foo:land_Use, $(Land_Use)]
      - [foo:plot_Name, $(Plot_Name)]
      - [foo:subplot, $(Subplot)]
      - [foo:horizon, $(Horizon)]
      - [foo:soil_pH, $(Soil_pH)]
      - [foo:total_C, $(Total_C)]
      - [foo:total_N, $(Total_N)]
      - [foo:total_P, $(Total_P)]
      - [foo:inorganic_P, $(inorganic_P)]
      - [foo:c:N, $(C:N)]
      - [foo:sand, $(Sand)]
      - [foo:silt, $(Silt)]
      - [foo:clay, $(Clay)]
      
```
