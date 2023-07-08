

# Camera Trap Images


A dataset containing one thousand images of Elephas maxims was modelled. Before transforming them into RDF graphs, image metadata was extracted and saved as CSV files. The RDF dataset has a unique path that points to the location of the image on a protected cloud server. The figure below depicts the dataset entities and the output of the semantic modelling.
Data are accessable on Github (https://github.com/Naeima/Forest-Observatory-Ontology/tree/main/Camera%20Trap%20images%20metadata).
 

<!-- ![Camera Trap Images](/img/image.png) -->

# Images' metadata Transformation to Resource Description Framework (RDF)

```python
import pandas as pd #for handling csv and csv contents
from rdflib import Graph, Literal, RDF, URIRef, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD, SSN, SOSA #most common namespaces
import urllib.parse #for parsing strings to URI's
```


```python
df = pd.read_csv('image.csv')
```


```python
df.tail(5)
```


```python
g = Graph()
ID = Namespace('Image_')
SOSA = Namespace('http://www.w3.org/ns/sosa/')
UNIT= Namespace('http://qudt.org/vocab/unit')
schema = Namespace('http://schema.org/')
uri=URIRef('http://www.w3.org/2000/01/rdf-schema#')
OBSPRO= Namespace('http://www.w3.org/ns/sosa/ObservableProperty/')
TIME = Namespace('http://www.w3.org/2006/time#')
VOID = Namespace('http://rdfs.org/ns/void#')
XMLNS = Namespace('http://www.w3.org/XML/1998/namespace')
```


```python
for index, row in df.iterrows():
    g.add((URIRef(foo+row['ID']), RDF.type, sosa.Observation)) 
    g.add((URIRef(foo+row['ID']), sosa.madeBySensor, URIRef(foo+'cameraTrap')))
    g.add((URIRef(foo+row['ID']), sosa.hasResult, Literal(row['ID'], datatype=XSD.string)))  

    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'path')))
    g.add((URIRef(foo+row['ID']), sosa.hasPath, Literal(row['path'], datatype=XSD.anyURI)))
    
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'name')))
    g.add((URIRef(foo+row['ID']), foo.hasName, Literal(row['name'], datatype=XSD.string)))  
    
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'make')))
    g.add((URIRef(foo+row['ID']), foo.hasMake, Literal(row['make'], datatype=XSD.string))) 
    
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'model')))
    g.add((URIRef(foo+row['ID']), foo.hasModel, Literal(row['model'], datatype=XSD.string)))
    
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'date')))
    g.add((URIRef(foo+row['ID']), sosa.resultTime, Literal(row['date'], datatype=XSD.date)))
    g.add((URIRef(foo+row['ID']), sosa.resultTime, Literal(row['time'], datatype=XSD.time)))
```


```python
#print(g.serialize(format='turtle').decode('UTF-8'))
```


```python
# saving RDF graph to disk
g.serialize('images.rdf', format="ttl")
```


```python
# adding serialized data to stardog 

conn_details = {
  'endpoint': 'http://localhost:5820',
  'username': 'admin',
  'password': 'admin'
}
with stardog.Admin(**conn_details) as admin:
    images = admin.new_database('images')

conn = stardog.Connection('images', **conn_details)

conn.begin()

conn.add(
    stardog.content.File('images.rdf', stardog.content_types.TURTLE),
)

conn.commit()
```

