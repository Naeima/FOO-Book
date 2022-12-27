

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
      <th>Site_name</th>
      <th>Plot_no</th>
      <th>Site_plot_code</th>
      <th>Date</th>
      <th>Tree_individual_no</th>
      <th>Tree_ID</th>
      <th>Tree_dbh_cm</th>
      <th>Tree_height_m</th>
      <th>Tree_N_lianas</th>
      <th>Liana_dbh_cm</th>
      <th>Tree_notes</th>
      <th>Subplot_radius_m</th>
      <th>ID1</th>
      <th>ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Danum W15</td>
      <td>1</td>
      <td>F1P1</td>
      <td>2017-07-21</td>
      <td>2</td>
      <td>Shorea pauciflora</td>
      <td>110.0</td>
      <td>60.0</td>
      <td>3</td>
      <td>10.0</td>
      <td>NaN</td>
      <td>30</td>
      <td>1</td>
      <td>lianas1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Danum W15</td>
      <td>1</td>
      <td>F1P1</td>
      <td>2017-07-21</td>
      <td>2</td>
      <td>Shorea pauciflora</td>
      <td>110.0</td>
      <td>60.0</td>
      <td>3</td>
      <td>9.0</td>
      <td>NaN</td>
      <td>30</td>
      <td>2</td>
      <td>lianas2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Danum W15</td>
      <td>1</td>
      <td>F1P1</td>
      <td>2017-07-21</td>
      <td>2</td>
      <td>Shorea pauciflora</td>
      <td>110.0</td>
      <td>60.0</td>
      <td>3</td>
      <td>9.8</td>
      <td>NaN</td>
      <td>30</td>
      <td>3</td>
      <td>lianas3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Danum W15</td>
      <td>1</td>
      <td>F1P1</td>
      <td>2017-07-21</td>
      <td>3</td>
      <td>Syzygium</td>
      <td>40.5</td>
      <td>NaN</td>
      <td>1</td>
      <td>3.4</td>
      <td>NaN</td>
      <td>30</td>
      <td>4</td>
      <td>lianas4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Danum W15</td>
      <td>1</td>
      <td>F1P1</td>
      <td>2017-07-21</td>
      <td>5</td>
      <td>Syzygium</td>
      <td>62.7</td>
      <td>NaN</td>
      <td>1</td>
      <td>3.4</td>
      <td>NaN</td>
      <td>30</td>
      <td>5</td>
      <td>lianas5</td>
    </tr>
  </tbody>
</table>
</div>




```python
#creating a unique ID 
df['ID'] ='lianas' + df['ID1'].astype(str)
```


```python
df.tail(10)
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
      <th>Site_name</th>
      <th>Plot_no</th>
      <th>Site_plot_code</th>
      <th>Date</th>
      <th>Tree_individual_no</th>
      <th>Tree_ID</th>
      <th>Tree_dbh_cm</th>
      <th>Tree_height_m</th>
      <th>Tree_N_lianas</th>
      <th>Liana_dbh_cm</th>
      <th>Tree_notes</th>
      <th>Subplot_radius_m</th>
      <th>ID1</th>
      <th>ID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3060</th>
      <td>Danum Malua</td>
      <td>1</td>
      <td>F18P1</td>
      <td>2017-10-28</td>
      <td>3892</td>
      <td>Shorea johorensis</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>4</td>
      <td>4.6</td>
      <td>NaN</td>
      <td>30</td>
      <td>3061</td>
      <td>lianas3061</td>
    </tr>
    <tr>
      <th>3061</th>
      <td>Danum Malua</td>
      <td>1</td>
      <td>F18P1</td>
      <td>2017-10-28</td>
      <td>3892</td>
      <td>Shorea johorensis</td>
      <td>60.0</td>
      <td>NaN</td>
      <td>4</td>
      <td>3.2</td>
      <td>NaN</td>
      <td>30</td>
      <td>3062</td>
      <td>lianas3062</td>
    </tr>
    <tr>
      <th>3062</th>
      <td>Danum Malua</td>
      <td>1</td>
      <td>F18P1</td>
      <td>2017-10-28</td>
      <td>3893</td>
      <td>Shorea</td>
      <td>15.0</td>
      <td>NaN</td>
      <td>4</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>20</td>
      <td>3063</td>
      <td>lianas3063</td>
    </tr>
    <tr>
      <th>3063</th>
      <td>Danum Malua</td>
      <td>1</td>
      <td>F18P1</td>
      <td>2017-10-28</td>
      <td>3893</td>
      <td>Shorea</td>
      <td>15.0</td>
      <td>NaN</td>
      <td>4</td>
      <td>4.1</td>
      <td>NaN</td>
      <td>20</td>
      <td>3064</td>
      <td>lianas3064</td>
    </tr>
    <tr>
      <th>3064</th>
      <td>Danum Malua</td>
      <td>1</td>
      <td>F18P1</td>
      <td>2017-10-28</td>
      <td>3893</td>
      <td>Shorea</td>
      <td>15.0</td>
      <td>NaN</td>
      <td>4</td>
      <td>6.7</td>
      <td>NaN</td>
      <td>20</td>
      <td>3065</td>
      <td>lianas3065</td>
    </tr>
    <tr>
      <th>3065</th>
      <td>Danum Malua</td>
      <td>1</td>
      <td>F18P1</td>
      <td>2017-10-28</td>
      <td>3893</td>
      <td>Shorea</td>
      <td>15.0</td>
      <td>NaN</td>
      <td>4</td>
      <td>2.3</td>
      <td>NaN</td>
      <td>20</td>
      <td>3066</td>
      <td>lianas3066</td>
    </tr>
    <tr>
      <th>3066</th>
      <td>Danum Malua</td>
      <td>1</td>
      <td>F18P1</td>
      <td>2017-10-28</td>
      <td>3895</td>
      <td>Macaranga gigantea</td>
      <td>39.0</td>
      <td>27.0</td>
      <td>4</td>
      <td>5.0</td>
      <td>NaN</td>
      <td>30</td>
      <td>3067</td>
      <td>lianas3067</td>
    </tr>
    <tr>
      <th>3067</th>
      <td>Danum Malua</td>
      <td>1</td>
      <td>F18P1</td>
      <td>2017-10-28</td>
      <td>3895</td>
      <td>Macaranga gigantea</td>
      <td>39.0</td>
      <td>27.0</td>
      <td>4</td>
      <td>2.5</td>
      <td>NaN</td>
      <td>30</td>
      <td>3068</td>
      <td>lianas3068</td>
    </tr>
    <tr>
      <th>3068</th>
      <td>Danum Malua</td>
      <td>1</td>
      <td>F18P1</td>
      <td>2017-10-28</td>
      <td>3895</td>
      <td>Macaranga gigantea</td>
      <td>39.0</td>
      <td>27.0</td>
      <td>4</td>
      <td>3.5</td>
      <td>NaN</td>
      <td>30</td>
      <td>3069</td>
      <td>lianas3069</td>
    </tr>
    <tr>
      <th>3069</th>
      <td>Danum Malua</td>
      <td>1</td>
      <td>F18P1</td>
      <td>2017-10-28</td>
      <td>3895</td>
      <td>Macaranga gigantea</td>
      <td>39.0</td>
      <td>27.0</td>
      <td>4</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>30</td>
      <td>3070</td>
      <td>lianas3070</td>
    </tr>
  </tbody>
</table>
</div>




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
