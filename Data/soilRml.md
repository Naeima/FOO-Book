

# Soil Sensor Data RML Rules 

- RML Rules were generated using Matey (https://rml.io/yarrrml/matey/).


```python
@prefix rr: <http://www.w3.org/ns/r2rml#> .
@prefix rml: <http://semweb.mmlab.be/ns/rml#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ql: <http://semweb.mmlab.be/ns/ql#> .
@prefix map: <http://mapping.example.com/> .
@prefix ma: <http://www.w3.org/ns/ma-ont#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix sd: <http://www.w3.org/ns/sparql-service-description#> .
@prefix schema: <http://schema.org/> .
@prefix sosa: <http://www.w3.org/ns/sosa/> .
@prefix foo: <http://www.ontology/ns/foo/1.1#/> .

map:map_person_000 rml:logicalSource map:source_000 ;
	rdf:type rr:TriplesMap ;
	rdfs:label "Observation" ;
	rr:predicateObjectMap map:pom_000, map:pom_001, map:pom_002, map:pom_003, map:pom_004, map:pom_005, map:pom_006, map:pom_007, map:pom_008, map:pom_009, map:pom_010, map:pom_011, map:pom_012, map:pom_013, map:pom_014, map:pom_015, map:pom_016 ;
	rr:subjectMap map:s_000 .

map:om_000 rdf:type rr:ObjectMap ;
	rr:constant "http://www.w3.org/ns/sosa/Observation" ;
	rr:termType rr:IRI .

map:om_001 rml:reference "Site" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_003 rml:reference "Land_Use" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_004 rml:reference "Plot_Name" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_006 rml:reference "Subplot" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_007 rml:reference "Horizon" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_008 rml:reference "Soil_pH" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_009 rml:reference "Total_C" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_010 rml:reference "Total_N" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_011 rml:reference "Total_P" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_012 rml:reference "inorganic_P" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_013 rml:reference "C:N" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_014 rml:reference "Sand" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_015 rml:reference "Silt" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:om_016 rml:reference "Clay" ;
	rdf:type rr:ObjectMap ;
	rr:termType rr:Literal .

map:pm_000 rdf:type rr:PredicateMap ;
	rr:constant rdf:type .

map:pm_001 rdf:type rr:PredicateMap ;
	rr:constant foo:Site .

map:pm_002 rdf:type rr:PredicateMap ;
	rr:constant foo:Site .

map:pm_003 rdf:type rr:PredicateMap ;
	rr:constant foo:Land_Use .

map:pm_004 rdf:type rr:PredicateMap ;
	rr:constant foo:Plot_Name .

map:pm_005 rdf:type rr:PredicateMap ;
	rr:constant foo:Plot_Name .

map:pm_006 rdf:type rr:PredicateMap ;
	rr:constant foo:Subplot .

map:pm_007 rdf:type rr:PredicateMap ;
	rr:constant foo:Horizon .

map:pm_008 rdf:type rr:PredicateMap ;
	rr:constant foo:Soil_pH .

map:pm_009 rdf:type rr:PredicateMap ;
	rr:constant foo:Total_C .

map:pm_010 rdf:type rr:PredicateMap ;
	rr:constant foo:Total_N .

map:pm_011 rdf:type rr:PredicateMap ;
	rr:constant foo:Total_P .

map:pm_012 rdf:type rr:PredicateMap ;
	rr:constant foo:inorganic_P .

map:pm_013 rdf:type rr:PredicateMap ;
	rr:constant foo:C .

map:pm_014 rdf:type rr:PredicateMap ;
	rr:constant foo:Sand .

map:pm_015 rdf:type rr:PredicateMap ;
	rr:constant foo:Silt .

map:pm_016 rdf:type rr:PredicateMap ;
	rr:constant foo:Clay .

map:pom_000 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_000 ;
	rr:predicateMap map:pm_000 .

map:pom_001 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_001 ;
	rr:predicateMap map:pm_001 .

map:pom_002 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_002 ;
	rr:predicateMap map:pm_002 .

map:pom_003 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_003 ;
	rr:predicateMap map:pm_003 .

map:pom_004 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_004 ;
	rr:predicateMap map:pm_004 .

map:pom_005 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_005 ;
	rr:predicateMap map:pm_005 .

map:pom_006 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_006 ;
	rr:predicateMap map:pm_006 .

map:pom_007 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_007 ;
	rr:predicateMap map:pm_007 .

map:pom_008 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_008 ;
	rr:predicateMap map:pm_008 .

map:pom_009 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_009 ;
	rr:predicateMap map:pm_009 .

map:pom_010 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_010 ;
	rr:predicateMap map:pm_010 .

map:pom_011 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_011 ;
	rr:predicateMap map:pm_011 .

map:pom_012 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_012 ;
	rr:predicateMap map:pm_012 .

map:pom_013 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_013 ;
	rr:predicateMap map:pm_013 .

map:pom_014 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_014 ;
	rr:predicateMap map:pm_014 .

map:pom_015 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_015 ;
	rr:predicateMap map:pm_015 .

map:pom_016 rdf:type rr:PredicateObjectMap ;
	rr:objectMap map:om_016 ;
	rr:predicateMap map:pm_016 .

map:rules_000 <http://rdfs.org/ns/void#exampleResource> map:map_person_000 ;
	rdf:type <http://rdfs.org/ns/void#Dataset> .

map:s_000 rdf:type rr:SubjectMap ;
	rr:template "http://www.ontology/ns/foo/1.1#/{Identifier}" .

map:source_000 rml:referenceFormulation ql:CSV ;
	rml:source "soil.csv" ;
	rdf:type rml:LogicalSource .

```
