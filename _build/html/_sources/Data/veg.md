

# Vegetation and Habitat Data 


These datasets comprise plant records from forty-nine plots spread among fourteen fragmented forest areas and four continuous forest sites in Sabah, Malaysian Borneo. Live vegetation and deadwood were surveyed at two to three sites at each of the eighteen sites. In addition to vegetation data, the dataset contains measurements of topsoil characteristics, forest structure measures, and metrics of the degree of forest fragmentation in the surrounding landscape of the plots. These data were collected so that studies could be done on (1) the factors that help exotic plant species take over fragmented forest areas and (2) the value of conservation set-asides for carbon storage and plant diversity in oil palm plantations.
Further data can be found at https://github.com/Naeima/Forest-Observatory-Ontology/tree/main/Vegetation.




```python
from rdflib import Graph, Literal, RDF, URIRef, Namespace 
from rdflib.namespace import FOAF , XSD, SSN, SOSA 
import urllib.parse
import pandas as pd 
import matplotlib.pylab as plt
from matplotlib import pyplot
```


```python
df = pd.read_csv('lianas.csv')
```


```python
df['ID1'] = df.index + 1
```


```python
df.head(5)
```


```python
#creating a unique ID 
df['ID'] ='lianas' + df['ID1'].astype(str)
```


```python
df.tail(10)
```


```python
g = Graph()
ID = Namespace('foo_')
owl = Namespace('http://www.w3.org/2002/07/owl#')
sosa = Namespace('http://www.w3.org/ns/sosa/')
foo = Namespace('http://www.ontology/ns/foo/1.1#')
wgs84_pos = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
time = Namespace('http://www.w3.org/2006/time#')
schema = Namespace('http://schema.org/')
XSD=Namespace('http://www.w3.org/2001/XMLSchema#')
```


```python
for index, row in df.iterrows():

    g.add((URIRef(ID+row['ID']), RDF.type, sosa.Observation)) 
    g.add((URIRef(ID+row['ID']), sosa.madeBySensor, URIRef(foo+'VegetationSensor')))
    g.add((URIRef(ID+row['ID']), sosa.hasResult, Literal(row['ID'], datatype=XSD.string))) 
    g.add((URIRef(ID+row['ID']), sosa.hasFeatureOfInterest, URIRef(foo+'lianas'))) 

    g.add((URIRef(ID+row['ID']), sosa.observedProperty, URIRef(foo+'Site_name')))
    g.add((URIRef(ID+row['ID']), foo.hasSite_name, Literal(row['Site_name'], datatype=XSD.string)))
    
    g.add((URIRef(ID+row['ID']), sosa.observedProperty, URIRef(foo+'Plot_no')))
    g.add((URIRef(ID+row['ID']), foo.hasSite_name, Literal(row['Plot_no'], datatype=XSD.string)))
    
    g.add((URIRef(ID+row['ID']), sosa.observedProperty, URIRef(foo+'Site_plot_code')))
    g.add((URIRef(ID+row['ID']), foo.hasSite_plot_code, Literal(row['Site_plot_code'], datatype=XSD.integer)))

    g.add((URIRef(ID+row['ID']), sosa.observedProperty, URIRef(foo+'Date')))
    g.add((URIRef(ID+row['ID']), sosa.resultTime, Literal(row['Date'], datatype=XSD.date)))
    
    g.add((URIRef(ID+row['ID']), sosa.observedProperty, URIRef(foo+'Tree_individual_no')))
    g.add((URIRef(ID+row['ID']), foo.hasTree_individual_no, Literal(row['Tree_individual_no'], datatype=XSD.integer)))
    
    g.add((URIRef(ID+row['ID']), sosa.observedProperty, URIRef(foo+'Tree_ID')))
    g.add((URIRef(ID+row['ID']), foo.hasTree_ID, Literal(row['Tree_ID'], datatype=XSD.string)))
    
    g.add((URIRef(ID+row['ID']), sosa.observedProperty, URIRef(foo+'Tree_dbh_cm')))
    g.add((URIRef(ID+row['ID']), foo.hasTree_dbh_cm, Literal(row['Tree_dbh_cm'], datatype=XSD.float)))
    
    g.add((URIRef(ID+row['ID']), sosa.observedProperty, URIRef(foo+'Tree_height_m')))
    g.add((URIRef(ID+row['ID']), foo.hasTree_height_m, Literal(row['Tree_height_m'], datatype=XSD.float)))
    
    g.add((URIRef(ID+row['ID']), sosa.observedProperty, URIRef(foo+'Liana_dbh_cm')))
    g.add((URIRef(ID+row['ID']), foo.hasLiana_dbh_cm, Literal(row['Liana_dbh_cm'], datatype=XSD.float)))
    
    g.add((URIRef(ID+row['ID']), sosa.observedProperty, URIRef(foo+'Tree_notes')))
    g.add((URIRef(ID+row['ID']), foo.hasTree_notes, Literal(row['Tree_notes'], datatype=XSD.string)))
    
    g.add((URIRef(ID+row['ID']), sosa.observedProperty, URIRef(foo+'Subplot_radius_m')))
    g.add((URIRef(ID+row['ID']), foo.hasSubplot_radius_m, Literal(row['Subplot_radius_m'], datatype=XSD.float)))  
```


```python
# print(g.serialize(format='turtle').decode('UTF-8'))
```


```python
# saving RDF graph to disk
g.serialize('lianas.rdf', format='ttl')
```


```python
# # Code to add data to stardog 
import stardog

conn_details = {
  'endpoint': 'http://localhost:5820',
  'username': 'admin',
  'password': 'admin'
}
with stardog.Admin(**conn_details) as admin:
    lianas = admin.new_database('lianas')

conn = stardog.Connection('lianas', **conn_details)

conn.begin()

conn.add(stardog.content.File('Aqeela.rdf', stardog.content_types.TURTLE)),
#     graph_uri=graph_uri)
conn.commit()
```
