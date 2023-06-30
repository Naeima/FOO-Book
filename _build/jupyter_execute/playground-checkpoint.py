#!/usr/bin/env python
# coding: utf-8

# # #GPS Collar 

# In[1]:


import pandas as pd #for handling csv and csv contents
from rdflib import Graph, Literal, RDF, URIRef, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD, SSN, SOSA #most common namespaces
import urllib.parse #for parsing strings to URI's
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import stardog
import json
import io
import os


# In[2]:


df = pd.read_csv('Jasmin.csv')


# In[3]:


df['Altitude']= pd.to_numeric(df['Altitude'],errors='coerce')
df['Altitude'].mean().round(6)


# In[4]:


df.head(10)


# In[5]:


df.describe()


# In[6]:


# 'Visualising Elephant Jasmin Movements'
# Creating and visualizing a scatter plot on Mapbox
fig = px.scatter_mapbox(df, lat='lat', lon='long',
                  animation_frame = 'GMTDate', animation_group = 'GMTTime',
                  color='Speed', size='Speed',
                  color_continuous_scale=px.colors.cyclical.IceFire,
                  size_max=50, zoom=1.75, hover_name='ID', 
                  hover_data = ['GMTDate', 'GMTTime', 'lat','long'], 
                  title = 'Visualising Elephant Jasmin Movements')

fig.update_layout(
        height=800,
        margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
        mapbox={
            'center': {'lon': 118, 'lat': 5},
            'accesstoken':"pk.eyJ1IjoibmFlaW1hIiwiYSI6ImNsNDRoa295ZDAzMmkza21tdnJrNWRqNmwifQ.-cUTmhr1Q03qUXJfQoIKGQ",
            'style': 'satellite-streets',
            #'style': "open-street-map",
             #'style': 'outdoors',
            'center': {'lon': 118, 'lat': 5},
            'zoom': 8})
fig.show()


# In[7]:


g = Graph()
ID = Namespace('DGFC_')
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


# In[8]:


for index, row in df.iterrows():
    g.add((URIRef(ID+row['ID']), RDF.type, SOSA.Observation))
    
    g.add((URIRef(ID+row['ID']), SOSA.Observation, Literal(row['ID'], datatype=XSD.string)))
    
    g.add((URIRef(ID+row['ID']), URIRef(schema+'DGFC/elephant#Jasmin'), Literal(row['ID'], datatype=XSD.string) ))  
    
    g.add((URIRef(ID+row['ID']), TIME.localDate, Literal(row['LocalDate'], datatype=XSD.date)))

    
    g.add((URIRef(ID+row['ID']), TIME.localTime, Literal(row['LocalTime'], datatype=XSD.time)))

    
    g.add((URIRef(ID+row['ID']), TIME.gMTDate, Literal(row['GMTDate'], datatype=XSD.date)))

    
    g.add((URIRef(ID+row['ID']), TIME.gMTTime, Literal(row['GMTTime'], datatype=XSD.time)))

  
    g.add((URIRef(ID+row['ID']), lat.lat, Literal(row['lat'], datatype=XSD.float)))

    g.add((URIRef(ID+row['ID']), long.long, Literal(row['long'], datatype=XSD.float)))
    
    g.add((URIRef(ID+row['ID']), OBSPRO.Temperature, Literal(row['Temperature'], datatype=XSD.double)))
   
    
    g.add((URIRef(ID+row['ID']), OBSPRO.Speed, Literal(row['Speed'], datatype=XSD.float)))
     
    g.add((URIRef(ID+row['ID']), alt.alt, Literal(row['Altitude'], datatype=XSD.float)))
   

    g.add((URIRef(ID+row['ID']), OBSPRO.Direction, Literal(row['Direction'], datatype=XSD.float)))
    g.add((URIRef(ID+row['ID']), OBSPRO.Distance, Literal(row['Distance'], datatype=XSD.float)))

    g.add((URIRef(ID+row['ID']), OBSPRO.HDOP, Literal(row['HDOP'], datatype=XSD.integer) ))
    g.add((URIRef(ID+row['ID']), OBSPRO.Cov, Literal(row['Cov'], datatype=XSD.integer) ))
    g.add((URIRef(ID+row['ID']), OBSPRO.Count, Literal(row['Count'], datatype=XSD.integer) ))


# In[9]:


# print(g.serialize(format='turtle')).head(10)


# In[10]:


# saving ontology to disk
g.serialize("Jasmin.rdf", format="ttl")


# In[11]:


# adding serialized data to Stardog (knowledge graph platform)

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


# In[12]:


# Fetch data back from Stardog 
conn_details = {
  'endpoint': 'http://localhost:5820',
  'username': 'admin',
  'password': 'admin'}


# In[13]:


conn = stardog.Connection('FOO', **conn_details)


# In[14]:


Jasmin= '''select * {GRAPH <urn:Jasmin> {?Jasmin <http://www.w3.org/2006/time#gMTDate> ?gMTDate;
<http://www.w3.org/2003/01/geo/wgs84_pos#long> ?Jasminlong; 
<http://www.w3.org/2003/01/geo/wgs84_pos#lat> ?Jasminlat;
<http://www.w3.org/ns/sosa/ObservableProperty/Speed>  ?JasminSpeed;
<http://www.w3.org/ns/sosa/ObservableProperty/Temperature> ?JasminTemperature;
<http://www.w3.org/ns/sosa/ObservableProperty/Direction> ?JasminDirection;
FILTER(?gMTDate >= "2011-02-07"^^xsd:date && ?gMTDate <= "2012-02-15"^^xsd:date)}}'''
csv_resultsJasmin = conn.select(Jasmin, content_type='text/csv')
df = pd.read_csv(io.BytesIO(csv_resultsJasmin))
df.head(10)

