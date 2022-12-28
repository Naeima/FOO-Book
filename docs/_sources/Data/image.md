

# Camera Trap Images


A dataset containing one thousand images of Elephas maxims was modelled. Before transforming them into RDF graphs, image metadata was extracted and saved as CSV files. The RDF dataset has a unique path that points to the location of the image on a protected cloud server. The figure below depicts the dataset entities and the output of the semantic modelling.
Data are accessable on Github (https://github.com/Naeima/Forest-Observatory-Ontology/tree/main/Camera%20Trap%20images%20metadata).
 

![Camera Trap Images](/img/image.png)


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
lat = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
long =Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
alt = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
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
    g.add((URIRef(ID+row['ID']), RDF.type, SOSA.Observation))  
    g.add((URIRef(ID+row['ID']), SOSA.Observation, Literal(row['ID'], datatype=XSD.string)))  
    g.add((URIRef(ID+row['ID']), URIRef(schema+'anno/image#ID'), Literal(row['ID'], datatype=XSD.string)))    
    g.add((URIRef(ID+row['ID']), OBSPRO.path, Literal(row['path'], datatype=XSD.anyURI)))
    g.add((URIRef(ID+row['ID']), OBSPRO.name, Literal(row['name'], datatype=XSD.string)))  
    g.add((URIRef(ID+row['ID']), OBSPRO.make, Literal(row['make'], datatype=XSD.string)))  
    g.add((URIRef(ID+row['ID']), OBSPRO.model, Literal(row['model'], datatype=XSD.string)))
    g.add((URIRef(ID+row['ID']), TIME.date_time, Literal(row['date_time'], datatype=XSD.dateTime)))
    g.add((URIRef(ID+row['ID']), TIME.date_time_digitized, Literal(row['date_time_digitized'], datatype=XSD.dateTime)))
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

# conn_details = {
#   'endpoint': 'http://localhost:5820',
#   'username': 'admin',
#   'password': 'admin'
# }
# with stardog.Admin(**conn_details) as admin:
#     images = admin.new_database('images')

# conn = stardog.Connection('images', **conn_details)

# conn.begin()

# conn.add(
#     stardog.content.File('images.rdf', stardog.content_types.TURTLE),
# )

# conn.commit()
```

