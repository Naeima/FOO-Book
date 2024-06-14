
# Soil Sensor Data

 The data consist of soil characteristics and nutrients for tropical forests in Sabah, Malaysia, both unlogged and logged. Soil properties (ID, Site, LandUse, PlotName, Subplot, Horizon, pH, TotalC, TotalN, TotalP, inorganicP, C-N, Sand, Silt, Clay) extracted from buried ion exchange membranes and soil nutrients (Identifier, Site, LandUse, PlotName, Subplot, NO3N, NH4N, TotalN, Ca, Mg, K, P, Fe, Mn Cu, Zn, B This data is a contribution from the BALI collaboration, which is financed by the UK's Natural Environment Research Council (NERC).
Modelled datasets in this study can be found at (https://github.com/Naeima/Forest-Observatory-Ontology/releases/tag/Soil-Data-v1.0.0).

![Soil Sensor Data](/img/soil.png)

```python

!pip install rdflib

from google.colab import files
import pandas as pd
import csv
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, XSD

# Prompt for file upload
uploaded = files.upload()

# Read the uploaded CSV file into a pandas DataFrame
for filename in uploaded.keys():
    print('User uploaded file "{name}" with length {length} bytes'.format(
        name=filename, length=len(uploaded[filename])))
    df = pd.read_csv(filename)

# Define namespaces
FOO = Namespace("https://w3id.org/def/foo#")
SOSA = Namespace("http://www.w3.org/ns/sosa/")
GEO = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")

# Create a new graph
g = Graph()

# Bind namespaces
g.bind("foo", FOO)
g.bind("sosa", SOSA)
g.bind("geo", GEO)

# Process data from DataFrame
for index, row in df.iterrows():
    site_name = row.get('Site_name', '').strip()
    plot_no = row.get('Plot_no', '')
    site_plot_code = row.get('Site_plot_code', '')
    date = row.get('Date', '').strip()
    tree_individual_no = row.get('Tree_individual_no', '')
    tree_id = row.get('Tree_ID', '').strip()
    tree_dbh_cm = row.get('Tree_dbh_cm', '')
    tree_height_m = row.get('Tree_height_m', '')
    tree_n_lianas = row.get('Tree_N_lianas', '')
    liana_dbh_cm = row.get('Liana_dbh_cm', '')
    tree_notes = row.get('Tree_notes', '')
    subplot_radius_m = row.get('Subplot_radius_m', '')

    # Create tree observation URI
    tree_observation = URIRef(f"https://w3id.org/def/foo#lianasObservation{tree_individual_no}")

    g.add((tree_observation, RDF.type, FOO.Observation))
    g.add((tree_observation, FOO.SiteName, Literal(site_name, datatype=XSD.string)))
    g.add((tree_observation, FOO.PlotNo, Literal(plot_no, datatype=XSD.integer)))
    g.add((tree_observation, FOO.SitePlotCode, Literal(site_plot_code, datatype=XSD.string)))
    g.add((tree_observation, FOO.Date, Literal(date, datatype=XSD.date)))
    g.add((tree_observation, FOO.TreeIndividualNo, Literal(tree_individual_no, datatype=XSD.integer)))
    g.add((tree_observation, FOO.TreeID, Literal(tree_id, datatype=XSD.string)))
    g.add((tree_observation, FOO.TreeDbhCm, Literal(tree_dbh_cm, datatype=XSD.double)))
    g.add((tree_observation, FOO.TreeHeightM, Literal(tree_height_m, datatype=XSD.double)))
    g.add((tree_observation, FOO.TreeNLianas, Literal(tree_n_lianas, datatype=XSD.integer)))
    g.add((tree_observation, FOO.LianaDbhCm, Literal(liana_dbh_cm, datatype=XSD.double)))
    g.add((tree_observation, FOO.TreeNotes, Literal(tree_notes, datatype=XSD.string)))
    g.add((tree_observation, FOO.SubplotRadiusM, Literal(subplot_radius_m, datatype=XSD.double)))

    # Create lianas sensor URI
    lianas_sensor = URIRef(f"https://w3id.org/def/foo#lianas{tree_individual_no}")
    g.add((lianas_sensor, RDF.type, FOO.lianas))
    g.add((lianas_sensor, FOO.ID, Literal(tree_individual_no, datatype=XSD.string)))
    g.add((lianas_sensor, FOO.hasFeatureOfInterest, FOO.Lianas))
    g.add((tree_observation, FOO.madeBySensor, lianas_sensor))

# Serialize the graph to a file
output_file = "lianas_knowledge_graph.ttl"
g.serialize(destination=output_file, format="turtle")

print(f"Knowledge graph has been serialized to {output_file}")

# Download the file
files.download(output_file)


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
