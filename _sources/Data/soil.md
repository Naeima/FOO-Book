

# Soil Sensor Data

 The data consist of soil characteristics and nutrients for tropical forests in Sabah, Malaysia, both unlogged and logged. Soil properties (ID, Site, LandUse, PlotName, Subplot, Horizon, pH, TotalC, TotalN, TotalP, inorganicP, C-N, Sand, Silt, Clay) extracted from buried ion exchange membranes and soil nutrients (Identifier, Site, LandUse, PlotName, Subplot, NO3N, NH4N, TotalN, Ca, Mg, K, P, Fe, Mn Cu, Zn, B This data is a contribution from the BALI collaboration, which is financed by the UK's Natural Environment Research Council (NERC).
Modelled datasets in this study can be found at (https://github.com/Naeima/Forest-Observatory-Ontology/releases/tag/Soil-Data-v1.0.0).






```python
from rdflib import Graph, Literal, RDF, URIRef, Namespace 
from rdflib.namespace import FOAF , XSD, SSN, SOSA 
import urllib.parse
import pandas as pd 
import matplotlib.pylab as plt
from matplotlib import pyplot
```


```python
df = pd.read_csv('soilpro.csv')
```


```python
df.tail(2)
```



```python
g = Graph()
ID = Namespace('SoilPropertiesCeh_')
SOSA = Namespace('http://www.w3.org/ns/sosa/')
UNIT= Namespace('http://qudt.org/vocab/unit/')
schema = Namespace('http://schema.org/')
uri=URIRef('http://www.w3.org/2000/01/rdf-schema#')
OBSPRO= Namespace('http://www.w3.org/ns/sosa/ObservableProperty/')
FEATURE= Namespace('http://www.w3.org/ns/sosa/FeatureOfInterest/')
TIME = Namespace('http://www.w3.org/2006/time#')
VOID = Namespace('http://rdfs.org/ns/void#')
XMLNS = Namespace('http://www.w3.org/XML/1998/namespace')
```


```python
for index, row in df.iterrows():
    
    g.add((URIRef(foo+row['Identifier']), RDF.type, sosa.Observation))
    g.add((URIRef(foo+row['Identifier']), sosa.madeBySensor, URIRef(foo+'Soil_Properties_FRC')))
    g.add((URIRef(foo+row['Identifier']), sosa.hasResult, Literal(row['Identifier'], datatype=XSD.string))) 
    
    g.add((URIRef(foo+row['Identifier']), sosa.hasFeatureOfInterest, URIRef(foo+'Site')))
     
    g.add((URIRef(foo+row['Identifier']), sosa.observedProperty, URIRef(foo+'Land_Use')))
    g.add((URIRef(foo+row['Identifier']), foo.hasLand_Use, Literal(row['Land_Use'], datatype=XSD.string)))
    
    g.add((URIRef(foo+row['Identifier']), sosa.observedProperty, URIRef(foo+'Plot_Name')))
    g.add((URIRef(foo+row['Identifier']), foo.hasPlot_Name, Literal(row['Plot_Name'], datatype=XSD.string)))
 
    g.add((URIRef(foo+row['Identifier']), sosa.observedProperty, URIRef(foo+'Subplot')))
    g.add((URIRef(foo+row['Identifier']), foo.hasSubplot, Literal(row['Subplot'], datatype=XSD.integer)))
 
    g.add((URIRef(foo+row['Identifier']), sosa.observedProperty, URIRef(foo+'Horizon')))
    g.add((URIRef(foo+row['Identifier']), foo.hasHorizon, Literal(row['Horizon'], datatype=XSD.string)))
    
    g.add((URIRef(foo+row['Identifier']), sosa.observedProperty, URIRef(foo+'Soil_pH')))
    g.add((URIRef(foo+row['Identifier']), foo.hasSoil_pH, Literal(row['Soil_pH'], datatype=XSD.float)))
    
    g.add((URIRef(foo+row['Identifier']), sosa.observedProperty, URIRef(foo+'Total_C')))
    g.add((URIRef(foo+row['Identifier']), foo.hasTotal_C, Literal(row['Total_C'], datatype=XSD.float)))
    
    g.add((URIRef(foo+row['Identifier']), sosa.observedProperty, URIRef(foo+'Total_N')))
    g.add((URIRef(foo+row['Identifier']), foo.hasTotal_N, Literal(row['Total_N'], datatype=XSD.float)))
    
    g.add((URIRef(foo+row['Identifier']), sosa.observedProperty, URIRef(foo+'Total_P')))
    g.add((URIRef(foo+row['Identifier']), foo.hasTotal_P, Literal(row['Total_P'], datatype=XSD.float)))
    
    g.add((URIRef(foo+row['Identifier']), sosa.observedProperty, URIRef(foo+'inorganic_P')))
    g.add((URIRef(foo+row['Identifier']), foo.hasInorganic_P, Literal(row['inorganic_P'], datatype=XSD.float)))
    
    g.add((URIRef(foo+row['Identifier']), sosa.observedProperty, URIRef(foo+'Sand')))
    g.add((URIRef(foo+row['Identifier']), foo.hasSand, Literal(row['Sand'], datatype=XSD.float)))

    g.add((URIRef(foo+row['Identifier']), sosa.observedProperty, URIRef(foo+'Silt')))
    g.add((URIRef(foo+row['Identifier']), foo.hasSilt, Literal(row['Silt'], datatype=XSD.float)))

    g.add((URIRef(foo+row['Identifier']), sosa.observedProperty, URIRef(foo+'Clay')))
    g.add((URIRef(foo+row['Identifier']), foo.hasClay, Literal(row['Clay'], datatype=XSD.float)))

```


```python
# print(g.serialize(format='turtle').decode('UTF-8'))
```


```python
# saving RDF graph to disk
g.serialize('Soil.rdf', format='ttl')
```


```python
# adding serialized data to stardog 

# conn_details = {
#   'endpoint': 'http://localhost:5820',
#   'username': 'admin',
#   'password': 'admin'
# }
# with stardog.Admin(**conn_details) as admin:
#     Soil = admin.new_database('Soil')

# conn = stardog.Connection('Soil', **conn_details)

# conn.begin()

# conn.add(
#     stardog.content.File('Soil.rdf', stardog.content_types.TURTLE),
# )

# conn.commit()
```
