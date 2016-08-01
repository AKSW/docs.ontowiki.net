---
title: Webservices
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_Webservices/
editme_path: ontowiki/Webservices.md
---
If you will take a deeper view into the code please look at <tt>ONTOWIKI_DIR/application/controllers/ServiceController.php</tt>

## Authentication (/service/auth)

(currently unstable status)

### Authentication Request

You can authenticate using via web service with an OntoWiki installation under the URI <tt>&lt;ontowiki_uri&gt;/service/auth</tt>

Authentication parameters can be supplied using POST or GET. However, GET is disabled by default and we don't recommend using it as passwords will be visible in the URI sent to the server. If you want to enable GET authentication set OntoWiki's config parameter <tt>rest.allowGetAuth</tt> to true.

The authentication supports the following parameters:

- u -- the username to authenticate with (required parameter if logout is not supplied or false)
- p -- the password to authenticate with (can be omitted; defaults to "")
- logout -- supply this parameter with the value "true" to remove the current authentication (required for logout).

### Authentication Response

The REST Server responds with one of the following HTTP responses:

- 200 OK -- The authentication was successfull. You now can request OntoWiki URIs that require authentication.
- 401 Unauthorized -- The authentication did not succeed. In most cases you supplied invalid user name, password or both.
- 405 Method Not Allowed -- You tried to authenticate via GET, although this is disabled in OntoWiki config.
- 400 Bad Request -- You didn't supply the parameters needed to fullfill the request.

## SPARQL Query (/sparql)

OntoWiki's web service accepts SPARQL queries according to the [SPARQL+protocol](http:_www.w3.org/TR/rdf-sparql-protocol/). The service is reachable under the URI <tt>&lt;ontowiki-uri&gt;/sparql</tt>.

### Usage

values submitted by HTTP GET/POST Variables:

- query: OBLIGATORY must contain the SPARQL-query to be executed on the Database
- default-graph-uri: OPTIONAL can contain an URI of a model to query on

If no datatype was sent the result datatype is XML. Another is JSON:

For XML:

- application/sparql-results+xml
- xml

For JSON:

- application/json
- application/sparql-results+json
- json

Error Message is given if any problem occured. (See Authentication Response for Error-Codes; they are applying on SPARQL Endpoint too).

### Plain example

<tt>/sparql?query=SELECT * WHERE {?s ?p ?o}&amp;default-graph-uri=http://mymodel.org/</tt> will give you all triples from <tt>http://mymodel.org</tt>. The result of the query is delivered as XML like specified from: [http://www.w3.org/TR/rdf-sparql-XMLres/](http://www.w3.org/TR/rdf-sparql-XMLres/).

### jQuery/AJAX example

Here is a short example how to use the SPARQL-endpoint with jQuery's AJAX. You define an event e.g. a double click

```
$('ellipse').dblclick(function () {
  // do something
});
```

Here you fire the request

```
$('ellipse').dblclick(function () {

  // SPARQL query
  var query = "SELECT ?s ?p ?o WHERE { ?s ?p ?o. };";
  
  
  // Fires the ajax request
  $.ajax({
      type: "POST",
      url: document.location.href + '/sparql?query=' + query,
      cache: false,
      dataType: 'json', 
      success: function(html) {
         alert ( html );
         // Your stuff
      }
  });
});
```

The \*dataType\* attributes defines the type of result data. XML or JSON are possible. For detailed information about jQuery's ajax function, please read [http://api.jquery.com/jQuery.ajax/](http://api.jquery.com/jQuery.ajax/).

Thats all. In the success function you can put all your stuff which shall be execute after an answer was received.

## Model Update (/model/update)

OntoWiki supports updating models via its web service. As of version 0.9 we support a [JSON+format](http:_n2.talis.com/wiki/RDF\_JSON\_Specification) but more formats are planned. To update a model, three parameters must be supplied:

- named-graph-uri -- the graph URI to be updated
- original-graph -- the old model as it was before the update process 
- modified-graph -- the updated model. The difference between old and new determines the statements that will be added to the model.

## SPARQL 1.1 Update (/update)

In addition to Model Update, OntoWiki supports a subset of SPARQL 1.1 Update ( [INSERT+DATA](http:_www.w3.org/TR/2010/WD-sparql11-update-20100126/#t411) and [DELETE+DATA](http:www.w3.org/TR/2010/WD-sparql11-update-20100126/#t412) syntax) via <tt>&lt;ontowiki-uri&gt;/update</tt>.

## Cross-Origin Resource Sharing (CORS)

OntoWiki is able to share your resource across domains with [CORS](http:_enable-cors.org/). You just need to enable the [cors+plugin](http:code.google.com/p/ontowiki/source/browse/extensions/plugins/cors/) and OntoWiki sends a

```
Access-Control-Allow-Origin: "*"
```

for all your (linked data) resources including the SPARQL endpoint.

If you want, you can change the specific Access-Control-Allow-Origin value in the cors plugin.ini.

