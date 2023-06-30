# FOO Evaluation

## Oops! Pitfall Scanner

The online freeware scanner detected the structure pitfalls classifying them into three categories, "critical, essential and minor".
FOO had a first rough pass containing different minor pitfalls. 
Generally speaking, minor pitfalls have no significant impact on ontology performance rather than making it look nice.
That said, minor pitfalls such as (i.e., P08 -missing annotation) could degrade the quality of the semantic ontology representation.  

![FOO Oops! Scanner](/img/Oops.png)


## Oops! Results 


![FOO Oops! collage](/img/Oopscollage.png)


- **A**- P04: the eight minor cases detected the unconnected elements in FOO. We imported directly from the BBC wildlife and the common creative licence website. Although we connected most of the imported elements, few remain for future expansion. Therefore, we take no action to alter block A. 

- **B**- P08: reported on missing annotations on thirty-eight cases. We revised the ontology and found that all these elements are duplicates of annotated ones. that is, FOO incurred two copies of them where one copy is missing the annotation. We eliminated duplicates and solved the pitfall case. 

- **C**- P13: flagged another thirty-three cases with undeclared inverse relationships. Given that we adapted these elements, we have no authority in this context to modify them. Therefore, we ignored the P13 result. 

- **D**- P22: We acknowledge that using the same naming conventions in the ontology is one of the W3c recommendations for best practice. However, we anticipated this case due to the nature of FOO, which reuses different ontologies. As we mentioned above at **P13**, we have no right to modify adopted ontologies' elements.   


## Pellet Evaluation

Pellet is an open-source OWL-DL reasoner. It has a good performance reputation for detecting contradicting facts in ontologies. 
Pellet can also make inferences and answer SPARQL queries. We used the protege's plug-in pellet version to reason over FOO and check for inconsistencies.
Pellet processed FOO in 29 ms, computing the inferences for entities' hierarchies and detecting no contradictions. 
A screenshot of the reasoner's report is available here. Nonetheless,  the inferred axioms have been published as an ontology in FOO Github.


![Pellet](/img/Pellet.png)


```{bibliography}
```
