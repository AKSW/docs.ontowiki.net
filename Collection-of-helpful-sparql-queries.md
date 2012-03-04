This page should gives you an overview about helpful SPARQL queries. Have more? Send us a message or add them directly here. 

You can use these queries in combination with our sparqlQuery method to questioning your knowledge bases.

## Get all classes 

```
SELECT DISTINCT ?class
WHERE {
    { ?class <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2000/01/rdf-schema#Class>. }
    UNION
    { ?class <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.w3.org/2002/07/owl#Class>. }
}

```

Gives you a list of all classes (RDFS and OWL) in your ontology. Each entry contains the URI of the class. 