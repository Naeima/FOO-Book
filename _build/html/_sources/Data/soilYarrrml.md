

# Soil Sensor Data YARRRML mappings

 - YARRRML genertaed using Matey (https://rml.io/yarrrml/matey/#)



```python
prefixes:
 foo: "http://www.ontology/ns/foo/1.1#/"
 rdf: "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
 xsd: "http://www.w3.org/2001/XMLSchema#"
 sosa: "http://www.w3.org/ns/sosa/"
 schema: "http://schema.org/"
 skos: "http://www.w3.org/2004/02/skos/core#"

mappings:
  Observation:
    sources:
      - ['soil.csv~csv']
    s: http://www.ontology/ns/foo/1.1#/$(Identifier)
    po:
      - [a, sosa:Observation]
      - [foo:Site, $(Site)]
      - [foo:Land_Use, $(Land_Use)]
      - [foo:Plot_Name, $(Plot_Name)]
      - [foo:Subplot, $(Subplot)]
      - [foo:Horizon, $(Horizon)]
      - [foo:Soil_pH, $(Soil_pH)]
      - [foo:Total_C, $(Total_C)]
      - [foo:Total_N, $(Total_N)]
      - [foo:Total_P, $(Total_P)]
      - [foo:inorganic_P, $(inorganic_P)]
      - [foo:C:N, $(C:N)]
      - [foo:Sand, $(Sand)]
      - [foo:Silt, $(Silt)]
      - [foo:Clay, $(Clay)]
      
```
