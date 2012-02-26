This page should gives you an overview about helpful SPARQL queries. Have more? Send us a message or add them directly here. 

You can use these queries in combination with our sparqlQuery method to questioning your knowledge bases.

## Get all classes 

```
SELECT ?uri ?label
WHERE {
    ?uri ?p1 <http://www.w3.org/2002/07/owl#Class>.
    ?uri <http://www.w3.org/2000/01/rdf-schema#label> ?label .
    FILTER (langmatches(lang(?label), "en"))
}
```

Gives you a list of all classes in your ontology.