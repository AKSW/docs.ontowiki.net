The ServiceController provides many helpful functions to interact with the OntoWiki backend. Following each action has its own part in the document.

## Update

Via the **updateAction** you can execute queries to insert, update, delete and select data of the triple store. 

### Insert new data

To insert new triples into the store, you may call service/update with this parameter:

* **named-graph-uri** - That is the URI of the model in which new triples must be added. 

* **insert** - JSON object which contains the triples. The format is called talis, have a look in their [docs](http://docs.api.talis.com/platform-api/output-types/rdf-json) for further information.

#### Example

This example will create triples in the model **http://schema.org/**. Triples are:

```
<http://schema.org/NewResource/D01EB4A2E7F26DC0F6F7E068517A09E6> <http://www.test.de> "Peter" .
<http://schema.org/NewResource/D01EB4A2E7F26DC0F6F7E068517A09E6> <http://www.w3.org/2000/01/rdf-schema#label> "LabelPeter" .
<http://schema.org/NewResource/D01EB4A2E7F26DC0F6F7E068517A09E6> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://schema.org/Foobar> .
```

As JSON (talis) it looks like:

```
{
    "http://schema.org/NewResource/D01EB4A2E7F26DC0F6F7E068517A09E6": {
        "http://www.test.de": [
            {
                "value": "Peter",
                "type": "literal",
                "lang": "de"
            }
        ],
        "http://www.w3.org/2000/01/rdf-schema#label": [
            {
                "value": "LabelPeter",
                "type": "literal",
                "lang": "de"
            }
        ],
        "http://www.w3.org/1999/02/22-rdf-syntax-ns#type": [
            {
                "value": "http://schema.org/Foobar",
                "type": "uri"
            }
        ]
    }
}
```

To bring the data to the server, call the url **http://localhost/ontowiki/service/update/** and add the following POST data:

```
named-graph-uri=http://schema.org/&
insert={"http://schema.org/NewResource/D01EB4A2E7F26DC0F6F7E068517A09E6":{"http://www.test.de" : [{"value" : "Peter", "type" : "literal", "lang" : "de"}], "http://www.w3.org/2000/01/rdf-schema#label" : [{"value" : "LabelPeter", "type" : "literal", "lang" : "de"}], "http://www.w3.org/1999/02/22-rdf-syntax-ns#type" : [{"value" : "http://schema.org/Foobar", "type" : "uri"}]}}
```