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


# df = pd.read_csv('Jasmin.csv')


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
ID = Namespace('foo_')
owl = Namespace('http://www.w3.org/2002/07/owl#')
sosa = Namespace('http://www.w3.org/ns/sosa/')
foo = Namespace('http://w3id.org/def/foo#')
lat = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
long =Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
alt = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos#')
time = Namespace('http://www.w3.org/2006/time#')
schema = Namespace('http://schema.org/')
XSD=Namespace('http://www.w3.org/2001/XMLSchema#')
Class = Namespace('http://purl.org/ontology/wo/Class/')
Family = Namespace('http://purl.org/ontology/wo/Family/')
Kingdom = Namespace('http://purl.org/ontology/wo/kingdom/')
Order = Namespace('http://purl.org/ontology/wo/Proboscidea/')
Phylum = Namespace('http://purl.org/ontology/wo/Phylum/')


# In[8]:


for index, row in df.iterrows():

    g.add((URIRef(foo+row['ID']), RDF.type, sosa.Observation))
    g.add((URIRef(foo+row['ID']), sosa.madeBySensor, URIRef(foo+'Jasmin')))
    g.add((URIRef(foo+row['ID']), sosa.hasResult, Literal(row['ID'], datatype=XSD.string)))
    
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'LocalDate')))
    g.add((URIRef(foo+row['ID']), foo.LocalDate, Literal(row['LocalDate'], datatype=XSD.date)))
          
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'LocalTime')))
    g.add((URIRef(foo+row['ID']), foo.LocalTime, Literal(row['LocalTime'], datatype=XSD.time)))
      
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'GMTDate')))
    g.add((URIRef(foo+row['ID']), foo.GMTDate, Literal(row['GMTDate'], datatype=XSD.date)))
    
    g.add((URIRef(foo+row['ID']), sosa.observedProperty, URIRef(foo+'GMTTime')))
    g.add((URIRef(foo+row['ID']), foo.GMTTime, Literal(row['GMTTime'], datatype=XSD.time)))
    
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

