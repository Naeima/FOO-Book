# Soil Knowledge Graph Code 
- The code generates the soil knowledge graph (https://naeima.github.io/soil/).

```python
from rdflib import Graph, plugin
from rdflib.parser import Parser
from rdflib import URIRef, Literal, Graph, RDF, Namespace

% Set the paths to your CSV file and the ontology file
csv_file = "SoilNu.csv"  # Replace with the data source 
ontology_file = "foo.ttl" # Replace with the ontology

%  Create an RDF graph
graph = Graph()

% Load the ontology into the graph
graph.parse(source=ontology_file, format="ttl")

% Set the namespace for your ontology
namespace = Namespace("http://www.ontology/ns/foo/1.1#")
namespace1 = Namespace("http://www.w3.org/ns/sosa/")

% RML mapping code
% Iterate over the CSV file and map the data to RDF triples
with open(csv_file, 'r') as file:
    % Skip the header row if present
    next(file)

    for line in file:
        % Split the CSV line into columns
        columns = line.strip().split(',')

        % Extract column values (modify as per your CSV structure)
        column1 = columns[0]
        column2 = columns[1]
        column3 = columns[2]
        column4 = columns[3]
        column5 = columns[4]
        column6 = columns[5]
        column7 = columns[6]
        column8 = columns[7]
        column9 = columns[8]
        column10 = columns[9]
        column11 = columns[10]
        column12 = columns[11]
        column13 = columns[12]
        column14 = columns[13]
        column15 = columns[14]
        column16 = columns[15]
        column17 = columns[16]
        column18 = columns[17]
        column19 = columns[18]
        column20 = columns[19]
        column21 = columns[20]

        % Create subject URI
        subject_uri = URIRef(namespace + column1)

        % Add triples to the graph
        graph.add((subject_uri, RDF.type, namespace1.Observation))  # Replace with the appropriate class from your ontology
        graph.add((subject_uri, namespace.Site, Literal(column2)))  # Replace with the appropriate predicate from your ontology
        graph.add((subject_uri, namespace.Land_Use, Literal(column3)))
        graph.add((subject_uri, namespace.Plot_Name, Literal(column4)))
        graph.add((subject_uri, namespace.Subplot, Literal(column5)))
        graph.add((subject_uri, namespace.NO3_N, Literal(column6)))
        graph.add((subject_uri, namespace.NH4_N, Literal(column7)))
        graph.add((subject_uri, namespace.Total_N, Literal(column8)))
        graph.add((subject_uri, namespace.Ca, Literal(column9)))
        graph.add((subject_uri, namespace.Mg, Literal(column10)))
        graph.add((subject_uri, namespace.K, Literal(column11)))
        graph.add((subject_uri, namespace.P, Literal(column12)))
        graph.add((subject_uri, namespace.Fe, Literal(column13)))
        graph.add((subject_uri, namespace.Mn, Literal(column14)))
        graph.add((subject_uri, namespace.Cu, Literal(column15)))
        graph.add((subject_uri, namespace.Zn, Literal(column16)))
        graph.add((subject_uri, namespace.B, Literal(column17)))
        graph.add((subject_uri, namespace.S, Literal(column18)))
        graph.add((subject_uri, namespace.Pb, Literal(column19)))
        graph.add((subject_uri, namespace.AI, Literal(column20)))
        graph.add((subject_uri, namespace.Cd, Literal(column21)))

% Save the resulting knowledge graph to a file
output_file = "SoilKG.rdf"
graph.serialize(destination=output_file, format="ttl") '''

