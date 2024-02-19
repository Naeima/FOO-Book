

# RDF Mapping Language Generic Code


```python
from rdflib import Graph, plugin
from rdflib.parser import Parser
from rdflib import URIRef, Literal, Graph, RDF, Namespace


# Set the paths to your CSV file and the ontology file
csv_file = "data.csv"  # Replace with the data source 
ontology_file = "ontology.ttl" # Replace with the ontology

# Create an RDF graph
graph = Graph()

# Load the ontology into the graph
graph.parse(source=ontology_file, format="ttl")

# Set the namespace for your ontology
namespace = Namespace("http://www.ontology/ns/foo/1.1#")

# ... (RML mapping code)
# Iterate over the CSV file and map the data to RDF triples
with open(csv_file, 'r') as file:
    # Skip the header row if present
    next(file)

    for line in file:
        # Split the CSV line into columns
        columns = line.strip().split(',')

        # Extract column values (modify as per your CSV structure)
        column1 = columns[0]
        column2 = columns[1]

        # Create subject URI
        subject_uri = URIRef(namespace + column1)

        # Add triples to the graph
        graph.add((subject_uri, RDF.type, namespace.YourClass))  # Replace with the appropriate class from your ontology
        graph.add((subject_uri, namespace.property1, Literal(column2)))  # Replace with the appropriate predicate from your ontology

# Save the resulting knowledge graph to a file
output_file = "output.rdf"
graph.serialize(destination=output_file, format="ttl")
```
