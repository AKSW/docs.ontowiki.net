The ServiceController provides many helpful functions to interact with the OntoWiki backend. Following each action has its own part in the document.

## Update

Via the **updateAction** you can execute queries to insert, update, delete and select data of the triple store. 

### Insert new data

To insert new triples into the store, you may call service/update with this parameter:

#### named-graph-uri
#### insert


URL:
```
http://localhost/ontowiki/service/update/
```
and **add** either the data via GET:
```
http://localhost/ontowiki/service/update/?named-graph-uri=http%3A%2f%2fschema.org%2f&
insert=%7B%22http%3A%2f%2fschema.org%2fNewResource%2fD01EB4A2E7F26DC0F6F7E068517A09E6%22%3A%7B%22http%3A%2f%2fwww.test.de%22%20%3A%20%5B%7B%22value%22%20%3A%20%22Peter%22%2C%20%22type%22%20%3A%20%22literal%22%2C%20%22lang%22%20%3A%20%22de%22%7D%5D%2C%20%22http%3A%2f%2fwww.w3.org%2f2000%2f01%2frdf-schema%23label%22%20%3A%20%5B%7B%22value%22%20%3A%20%22LabelPeter%22%2C%20%22type%22%20%3A%20%22literal%22%2C%20%22lang%22%20%3A%20%22de%22%7D%5D%2C%20%22http%3A%2f%2fwww.w3.org%2f1999%2f02%2f22-rdf-syntax-ns%23type%22%20%3A%20%5B%7B%22value%22%20%3A%20%22http%3A%2f%2fschema.org%2fNetzer%22%2C%20%22type%22%20%3A%20%22uri%22%7D%5D%7D%7D
```

or via POST:
```
named-graph-uri=http://schema.org/&
insert={"http://schema.org/NewResource/D01EB4A2E7F26DC0F6F7E068517A09E6":{"http://www.test.de" : [{"value" : "Peter", "type" : "literal", "lang" : "de"}], "http://www.w3.org/2000/01/rdf-schema#label" : [{"value" : "LabelPeter", "type" : "literal", "lang" : "de"}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#type" : [{"value" : "http://schema.org/Netzer", "type" : "uri"}]}}
```