---
title: OntoWiki_Model_TitleHelper
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /OntoWiki_Model_TitleHelper.html
editme_path: ontowiki/OntoWiki_Model_TitleHelper.md
---
Class OntoWiki_Model_TitleHelper fetches title properties for a set of resources. You can collect all resources from which you want to get the title later. If you get the title from one of them the TitleHelper gets the title properties for all resources at once.

## A short demonstration

For example there is one triple in your knowledge base

```
<http://foo.bar.de/> rdfs:label "Foo loves Bar !"
```

or maybe its skos:label or skos:prefLabel... and you want to display that resource in the GUI. In OntoWiki we have the principle to hide URIs from the user where possible (they might think its a technical detail and would be scared :). So we made a little helper for getting labels. It hides a SPARQL-Query, knows the most used label-properties, is configurable and you can just push URIs in and get labels out. If you first add all URIs you want, and then request their labels, the Query gets them all at once which is most efficient.

### Create an instance of TitleHelper

This code its from a Controller, so please change it if you need access to the model from another place:
```
$titleHelper = new OntoWiki_Model_TitleHelper($this->_owApp->selectedModel);
```

### Add your resources to the titleHelper-list.

If you have only one URI so use 
```
$titleHelper->addResource( "http://foo.bar.de/" );
```

If you have more, so use
```
$titleHelper->addResources ( array ( "http://foo.bar.de/", "http://we.love.base/" ) );
```
 

### Getting your title you need the getTitle function
```
$fetchedTitle = $titleHelper->getTitle( "http://foo.bar.de" );
```

now $fetchedTitle holds the wanted title (or label). :)

If you want the title for each resource you have, **do not** something like this:
```
foreach($uris as $uri){
  $titleHelper->addResource($uri);
  echo $titleHelper->getTitle($uri);
}
```

It will not work! Instead of this, first add all resources to TitleHelper instance

```
// it assumes that $uris looks like array ( "http://foo.bar.de/", "http://we.love.ontowiki/" );
$titleHelper->addResources ($uris);
```

and than you can iterate about the URI's again to play with the titles

```
foreach($uris as $uri){
   echo $titleHelper->getTitle($uri);
}
```

because the first call of getTitle will trigger the query.