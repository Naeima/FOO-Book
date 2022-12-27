

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
      <th>ID</th>
      <th>path</th>
      <th>name</th>
      <th>make</th>
      <th>model</th>
      <th>is_animal</th>
      <th>date_time</th>
      <th>date_time_digitized</th>
      <th>mega</th>
      <th>Marco</th>
      <th>Marco_sub</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>90</th>
      <td>DGFC_90</td>
      <td>/var/home/akin/Untitled Folder/web_app/sep_pic...</td>
      <td>anno_image13.jpg</td>
      <td>RECONYX</td>
      <td>PC800 PROFESSIONAL</td>
      <td>False</td>
      <td>2015:06:27 23:42:53</td>
      <td>2015:06:27 23:42:53</td>
      <td>Animal, prob = 0.107</td>
      <td>Animal, prob =0.8446</td>
      <td>impala, prob =0.3457</td>
    </tr>
    <tr>
      <th>91</th>
      <td>DGFC_91</td>
      <td>/var/home/akin/Untitled Folder/web_app/sep_pic...</td>
      <td>anno_image26.jpg</td>
      <td>RECONYX</td>
      <td>PC800 PROFESSIONAL</td>
      <td>False</td>
      <td>2015:03:29 08:18:59</td>
      <td>2015:03:29 08:18:59</td>
      <td>Animal, prob = 0.131</td>
      <td>Animal, prob =0.6920</td>
      <td>HUMAN, prob =0.5478</td>
    </tr>
    <tr>
      <th>92</th>
      <td>DGFC_92</td>
      <td>/var/home/akin/Untitled Folder/web_app/sep_pic...</td>
      <td>anno_image29.jpg</td>
      <td>RECONYX</td>
      <td>PC800 PROFESSIONAL</td>
      <td>False</td>
      <td>2015:03:30 22:35:03</td>
      <td>2015:03:30 22:35:03</td>
      <td>Animal, prob = 0.57</td>
      <td>Animal, prob =0.7101</td>
      <td>rhino, prob =0.4231</td>
    </tr>
    <tr>
      <th>93</th>
      <td>DGFC_93</td>
      <td>/var/home/akin/Untitled Folder/web_app/sep_pic...</td>
      <td>anno_image54.jpg</td>
      <td>RECONYX</td>
      <td>PC800 PROFESSIONAL</td>
      <td>False</td>
      <td>2015:04:30 21:06:37</td>
      <td>2015:04:30 21:06:37</td>
      <td>empty, prob =0.000</td>
      <td>Animal, prob =0.4166</td>
      <td>elephant, prob =0.1777</td>
    </tr>
    <tr>
      <th>94</th>
      <td>DGFC_94</td>
      <td>/var/home/akin/Untitled Folder/web_app/sep_pic...</td>
      <td>anno_image56.jpg</td>
      <td>RECONYX</td>
      <td>PC800 PROFESSIONAL</td>
      <td>False</td>
      <td>2015:05:01 01:54:24</td>
      <td>2015:05:01 01:54:24</td>
      <td>empty, prob =0.000</td>
      <td>Animal, prob =0.5146</td>
      <td>monkeybaboon, prob =0.6202</td>
    </tr>
  </tbody>
</table>
</div>




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

