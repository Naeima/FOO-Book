

# Soil Sensor Data

 The data consist of soil characteristics and nutrients for tropical forests in Sabah, Malaysia, both unlogged and logged. Soil properties (ID, Site, LandUse, PlotName, Subplot, Horizon, pH, TotalC, TotalN, TotalP, inorganicP, C-N, Sand, Silt, Clay) extracted from buried ion exchange membranes and soil nutrients (Identifier, Site, LandUse, PlotName, Subplot, NO3N, NH4N, TotalN, Ca, Mg, K, P, Fe, Mn Cu, Zn, B This data is a contribution from the BALI collaboration, which is financed by the UK's Natural Environment Research Council (NERC).
Modelled datasets in this study can be found at (https://github.com/Naeima/Forest-Observatory-Ontology/releases/tag/Soil-Data-v1.0.0).

![Soil Sensor Data](/img/soil.png)


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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Identifier</th>
      <th>Site</th>
      <th>Land_Use</th>
      <th>Plot_Name</th>
      <th>Subplot</th>
      <th>Horizon</th>
      <th>Soil_Moisture</th>
      <th>Horizon_Depth</th>
      <th>Bulk_Density</th>
      <th>Soil_pH</th>
      <th>total_C</th>
      <th>total_N</th>
      <th>Inorganic_P</th>
      <th>C:N</th>
      <th>C:P</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>220</th>
      <td>SOP93</td>
      <td>SAFE Project - Kalabakan Forest Reserve</td>
      <td>Oil Palm</td>
      <td>OP</td>
      <td>9</td>
      <td>Organic</td>
      <td>12.26</td>
      <td>3.0</td>
      <td>0.80</td>
      <td>6.63</td>
      <td>2.79</td>
      <td>0.23</td>
      <td>48.31</td>
      <td>12.08</td>
      <td>0.06</td>
    </tr>
    <tr>
      <th>221</th>
      <td>SOP94</td>
      <td>SAFE Project - Kalabakan Forest Reserve</td>
      <td>Oil Palm</td>
      <td>OP</td>
      <td>9</td>
      <td>Organic</td>
      <td>10.83</td>
      <td>5.5</td>
      <td>1.07</td>
      <td>6.53</td>
      <td>6.06</td>
      <td>0.43</td>
      <td>126.75</td>
      <td>13.94</td>
      <td>0.05</td>
    </tr>
  </tbody>
</table>
</div>




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
    g.add((URIRef(ID+row['Identifier']), RDF.type, SOSA.Observation))
    
    g.add((URIRef(ID+row['Identifier']), SOSA.Observation, Literal(row['Identifier'], datatype=XSD.string)))
    
    g.add((URIRef(ID+row['Identifier']), URIRef(schema+'Soil_Properties_CEH'), Literal(row['Identifier'], datatype=XSD.string)))
      
    g.add((URIRef(ID+row['Identifier']), FEATURE.Site, Literal(row['Site'], datatype=XSD.string)))
    
    g.add((URIRef(ID+row['Identifier']), schema.Land_Use, Literal(row['Land_Use'], datatype=XSD.string)))
    
    g.add((URIRef(ID+row['Identifier']), schema.Plot_Name, Literal(row['Plot_Name'], datatype=XSD.string)))
    
    g.add((URIRef(ID+row['Identifier']), FEATURE.Subplot, Literal(row['Subplot'], datatype=XSD.integer))) 

    g.add((URIRef(ID+row['Identifier']), FEATURE.Horizon, Literal(row['Horizon'], datatype=XSD.string))) 
    
    g.add((URIRef(ID+row['Identifier']), OBSPRO.Soil_Moisture, Literal(row['Soil_Moisture'], datatype=XSD.float)))
    
    g.add((URIRef(ID+row['Identifier']), OBSPRO.Horizon_Depth, Literal(row['Horizon_Depth'], datatype=XSD.float)))
    
    g.add((URIRef(ID+row['Identifier']), OBSPRO.Bulk_Density, Literal(row['Bulk_Density'], datatype=XSD.float)))
    
    g.add((URIRef(ID+row['Identifier']), OBSPRO.Soil_pH, Literal(row['Soil_pH'], datatype=XSD.float)))
    
    g.add((URIRef(ID+row['Identifier']), OBSPRO.total_C, Literal(row['total_C'], datatype=XSD.float)))
    
    g.add((URIRef(ID+row['Identifier']), OBSPRO.total_N, Literal(row['total_N'], datatype=XSD.float)))
    
    g.add((URIRef(ID+row['Identifier']), OBSPRO.CtoN, Literal(row['C:N'], datatype=XSD.float)))
    
    g.add((URIRef(ID+row['Identifier']), OBSPRO.CtoP, Literal(row['C:P'], datatype=XSD.float)))
    
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
