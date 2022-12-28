

# Vegetation and Habitat Data 


These datasets comprise plant records from forty-nine plots spread among fourteen fragmented forest areas and four continuous forest sites in Sabah, Malaysian Borneo. Live vegetation and deadwood were surveyed at two to three sites at each of the eighteen sites. In addition to vegetation data, the dataset contains measurements of topsoil characteristics, forest structure measures, and metrics of the degree of forest fragmentation in the surrounding landscape of the plots. These data were collected so that studies could be done on (1) the factors that help exotic plant species take over fragmented forest areas and (2) the value of conservation set-asides for carbon storage and plant diversity in oil palm plantations.
Further data can be found at https://github.com/Naeima/Forest-Observatory-Ontology/tree/main/Vegetation.

![Vegetation and Habitat Data ](/img/veg.png)


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
ID = Namespace('lianas_')
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
    g.add((URIRef(ID+row['ID']), RDF.type, SOSA.Observation))
    
    g.add((URIRef(ID+row['ID']), SOSA.Observation, Literal(row['ID'], datatype=XSD.string)))
    
    g.add((URIRef(ID+row['ID']), URIRef(schema+'lianas'), Literal(row['ID'], datatype=XSD.string) ))  
    
    g.add((URIRef(ID+row['ID']), schema.Site_name, Literal(row['Site_name'], datatype=XSD.string)))
  
    g.add((URIRef(ID+row['ID']), FEATURE.Plot_no, Literal(row['Plot_no'], datatype=XSD.integer)))

    g.add((URIRef(ID+row['ID']), schema.Site_plot_code, Literal(row['Site_plot_code'], datatype=XSD.string)))
    
    g.add((URIRef(ID+row['ID']), TIME.Date, Literal(row['Date'], datatype=XSD.date)))
    
    g.add((URIRef(ID+row['ID']), OBSPRO.Tree_individual_no, Literal(row['Tree_individual_no'], datatype=XSD.integer)))
    
    g.add((URIRef(ID+row['ID']), schema.Tree_ID	, Literal(row['Tree_ID'], datatype=XSD.string)))
    
    g.add((URIRef(ID+row['ID']), OBSPRO.Tree_dbh_cm, Literal(row['Tree_dbh_cm'], datatype=XSD.float)))
    
    g.add((URIRef(ID+row['ID']), OBSPRO.Tree_height_m, Literal(row['Tree_height_m'], datatype=XSD.float)))
    
    g.add((URIRef(ID+row['ID']), OBSPRO.Liana_dbh_cm, Literal(row['Liana_dbh_cm'], datatype=XSD.integer)))

    g.add((URIRef(ID+row['ID']), OBSPRO.Liana_dbh_cm, Literal(row['Liana_dbh_cm'], datatype=XSD.float)))
    
    g.add((URIRef(ID+row['ID']), schema.Tree_notes, Literal(row['Tree_notes'], datatype=XSD.string)))

    g.add((URIRef(ID+row['ID']), OBSPRO.Subplot_radius_m, Literal(row['Subplot_radius_m'], datatype=XSD.integer) ))
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
# import stardog

# conn_details = {
#   'endpoint': 'http://localhost:5820',
#   'username': 'admin',
#   'password': 'admin'
# }
# with stardog.Admin(**conn_details) as admin:
#     lianas = admin.new_database('lianas')

# conn = stardog.Connection('lianas', **conn_details)

# conn.begin()

# conn.add(
#     stardog.content.File('Aqeela.rdf', stardog.content_types.TURTLE),
# #     graph_uri=graph_uri)
# conn.commit()
```
