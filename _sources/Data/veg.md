

# Vegetation and Habitat Data 


These datasets comprise plant records from forty-nine plots spread among fourteen fragmented forest areas and four continuous forest sites in Sabah, Malaysian Borneo. Live vegetation and deadwood were surveyed at two to three sites at each of the eighteen sites. In addition to vegetation data, the dataset contains measurements of topsoil characteristics, forest structure measures, and metrics of the degree of forest fragmentation in the surrounding landscape of the plots. These data were collected so that studies could be done on (1) the factors that help exotic plant species take over fragmented forest areas and (2) the value of conservation set-asides for carbon storage and plant diversity in oil palm plantations.
Further data can be found at https://github.com/Naeima/Forest-Observatory-Ontology/tree/main/Vegetation.

![Vegetation and Habitat Data ](/img/veg.png)


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
    g.add((tree_observation, RDF.type, FOO.treeObservation))
    g.add((tree_observation, FOO.id, Literal(tree_individual_no, datatype=XSD.string)))
    g.add((tree_observation, FOO.siteName, Literal(site_name, datatype=XSD.string)))
    g.add((tree_observation, FOO.plotNo, Literal(plot_no, datatype=XSD.integer)))
    g.add((tree_observation, FOO.sitePlotCode, Literal(site_plot_code, datatype=XSD.string)))
    g.add((tree_observation, FOO.date, Literal(date, datatype=XSD.date)))
    g.add((tree_observation, FOO.treeIndividualNo, Literal(tree_individual_no, datatype=XSD.integer)))
    g.add((tree_observation, FOO.treeID, Literal(tree_id, datatype=XSD.string)))
    g.add((tree_observation, FOO.treeDbhCm, Literal(tree_dbh_cm, datatype=XSD.double)))
    g.add((tree_observation, FOO.treeHeightM, Literal(tree_height_m, datatype=XSD.double)))
    g.add((tree_observation, FOO.treeNLianas, Literal(tree_n_lianas, datatype=XSD.integer)))
    g.add((tree_observation, FOO.lianaDbhCm, Literal(liana_dbh_cm, datatype=XSD.double)))
    g.add((tree_observation, FOO.treeNotes, Literal(tree_notes, datatype=XSD.string)))
    g.add((tree_observation, FOO.subplotRadiusM, Literal(subplot_radius_m, datatype=XSD.double)))
    g.add((tree_observation, FOO.hasFeatureOfInterest, FOO.tree))
    g.add((tree_observation, FOO.madeBySensor, FOO.treeSensor))

# Serialize the graph to a file
output_file = "lianas_knowledge_graph.ttl"
g.serialize(destination=output_file, format="turtle")

print(f"Knowledge graph has been serialized to {output_file}")

# Download the file
files.download(output_file)
```
