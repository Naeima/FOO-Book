
# Animal GPS Collars Data


The Danau Girang Field Centre (DGFC) https://www.dgfc.life/home/ provided us with the collars data for elephants. Collars weighing approximately 14 kg each were officially placed around the elephants' necks to record numerous metrics  every two hours, including time, geolocation, and temperature.
In this study, we modelled twenty-two adult Asian elephants (Elephas maximus), fourteen females and eight males. The collars were created by Africa Wildlife Tracking and fitted ethically by a team of researchers, trackers, and a wildlife vet. Each collar had a Global Positioning System (GPS) receiver and a Very High Frequency (VHF) transmitter. At predetermined intervals, the GPS uploaded each individual's geographical location information to the Globaltrack server, which could be officially obtained from the Globaltrack website (http://www.globaltrack.com). The built-in VHF transmitter aided in retrieving collars that had come off naturally or in locating an individual when additional monitoring was required. The observations in those datasets cover the period range between 2012 to 2018. We refrain from publishing the datasets used in this study because they could be misused to locate an endangered species at risk of poaching. 

<!-- ![Animal GPS Collars Data](/img/collar.png) -->





# GPS Collar RDF Transformation Pipeline 


```python
import pandas as pd #for handling csv and csv contents
from rdflib import Graph, Literal, RDF, URIRef, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD, SSN, SOSA #most common namespaces
import urllib.parse #for parsing strings to URI's
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import stardog
```

```python
df = pd.read_csv('Jasmin.csv')
```



```python
df['Altitude']= pd.to_numeric(df['Altitude'],errors='coerce')
df['Altitude'].mean().round(6)
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
Class = Namespace('http://purl.org/ontology/wo/Class/')
Family = Namespace('http://purl.org/ontology/wo/Family/')
Kingdom = Namespace('http://purl.org/ontology/wo/kingdom/')
Order = Namespace('http://purl.org/ontology/wo/Proboscidea/')
Phylum = Namespace('http://purl.org/ontology/wo/Phylum/')
```


```python
    for index, row in df.iterrows():

    g.add((URIRef(foo+row['ID']), RDF.type, sosa.Observation))
    g.add((URIRef(foo+row['ID']), sosa.madeBySensor, URIRef(foo+'Jasmin')))
    g.add((URIRef(foo+row['ID']), sosa.hasResult, Literal(row['ID'], datatype=XSD.string)))
    
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'LocalDate')))
    g.add((URIRef(foo+row['ID']), sosa.resultTime, Literal(row['LocalDate'], datatype=XSD.date)))
          
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'LocalTime')))
    g.add((URIRef(foo+row['ID']), sosa.resultTime, Literal(row['LocalTime'], datatype=XSD.time)))
      
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'GMTDate')))
    g.add((URIRef(foo+row['ID']), sosa.resultTime, Literal(row['GMTDate'], datatype=XSD.date)))
    
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'GMTTime')))
    g.add((URIRef(foo+row['ID']), sosa.resultTime, Literal(row['GMTTime'], datatype=XSD.time)))
    
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'lat')))
    g.add((URIRef(foo+row['ID']), wgs_84.lat, Literal(row['lat'], datatype=XSD.float)))
     
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'long')))
    g.add((URIRef(foo+row['ID']), wgs_84.long, Literal(row['long'], datatype=XSD.float)))
    
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'Temperature')))
    g.add((URIRef(foo+row['ID']), foo.hasTemperature, Literal(row['Temperature'], datatype=XSD.double)))
    
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'Speed')))
    g.add((URIRef(foo+row['ID']), foo.hasSpeed, Literal(row['Speed'], datatype=XSD.float)))
    
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'Altitude')))
    g.add((URIRef(foo+row['ID']),  wgs_84.alt, Literal(row['Altitude'], datatype=XSD.float)))
   
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'Direction')))
    g.add(( URIRef(foo+row['ID']), sosa.hasDirection, Literal(row['Direction'], datatype=XSD.float)))
    
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'Distance')))
    g.add((URIRef(foo+row['ID']), foo.hasDistance, Literal(row['Distance'], datatype=XSD.float)))
    
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'HDOP')))
    g.add((URIRef(foo+row['ID']), foo.hasHDOP, Literal(row['HDOP'], datatype=XSD.integer)))
 
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'Cov')))
    g.add((URIRef(foo+row['ID']), foo.hasCov, Literal(row['Cov'], datatype=XSD.integer)))
    
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'Count')))
    g.add((URIRef(foo+row['ID']), foo.hasCount, Literal(row['Count'], datatype=XSD.integer)))
    
    g.add((URIRef(foo+row['ID']), sosa.hasFeatureOfInterest, URIRef(foo+'ElephasMaximus')))
    
    g.add((URIRef(foo+'ElephasMaximus'), RDF.type, Class.Mammalia))
    
    g.add((URIRef(foo+'ElephasMaximus'), RDF.type, Family.Elephantidae))
  
    g.add((URIRef(foo+'ElephasMaximus'), RDF.type, Kingdom.Animalia))
          
    g.add((URIRef(foo+'ElephasMaximus'), RDF.type, Phylum.Chordata))
    
```


```python
# print(g.serialize(format='turtle'))
```


```python
# saving RDF graph to disk
g.serialize("Jasmin.rdf", format="ttl")
```


```python
# adding serialized data to stardog 

 conn_details = {
 'endpoint': 'http://localhost:5820',
 'username': 'admin',
  'password': 'admin'
 }
with stardog.Admin(**conn_details) as admin:
    Jasmin = admin.new_database('Jasmin')

 conn = stardog.Connection('Jasmin', **conn_details)

 conn.begin()

 conn.add(
    stardog.content.File('Jasmin.rdf', stardog.content_types.TURTLE),
)

 conn.commit()
```


