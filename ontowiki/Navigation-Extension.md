---
title: Navigation-Extension
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_Navigation-Extension/
editme_path: ontowiki/Navigation-Extension.md
---
The Navigation Extension is one of the OntoWiki core extensions which are included in a vanilla OntoWiki.

## Configuration
You can configure the Navigation Extension through the [Extension Configurator](http://docs.ontowiki.net/ontowiki_Extensions/#extension-api-and-development) or by manually editing its DOAP-File.

_Note:_ currently this wiki page describes the configuration option using the INI-Syntax. This syntax is 1:1 mapped to the DOAP-Syntax so you might be ablte to figure out, how you have to write it in the DOAP-File.

Here are some configuration keys and the description of there functionality:

### Sorting
To add a new sorting create two new entries:

    sorting.<key>.name = "Title (e.g. By ...)"
    sorting.<key>.type = "The URI http://"

### Hierarchy configuration
With the navigation extension you are able to create a navigation for any kind of hierarchical
system for your OntoWiki. For each different navigation hierarchy you have to add a set of options
which are described in the following.

All configuration options start with a prefix `config.` which is followed by an id common to all
configuration keys of one navigation configuration.

    config.<id>.

The name which is used for the GUI (not as an id)

    config.<id>.name = "Navigation Name"
    
This option is used to disable caching for selected config

    config.<id>.cache = {true|false}

This option is used to configure, how much effort is used to prepare the
titles of the hierarchy entries. The following config values are recognized:

* titleHelper (default) (this is the fancy but slow titleHelper)
* baseName              (just use the name after the last slash or hash)

```
config.<id>.titleMode = titleHelper
```

If false there will be no check for visibility and this type config
will be always shown in menu

    config.<id>.checkVisibility = {true|false}

If present, this Relation ist used for ordering the hierarchy elements.
In addition to that, ordering can be done in DESC or ASC direction
THIS CAN BE TIME CONSUMING because this is done on the RDF store
If you dont use ordering, the first X entries are returned and sorted by PHP
according to the name

    config.<id>.ordering.relation = "http://ns.ontowiki.net/SysOnt/order"
    config.<id>.ordering.modifier = {DESC|ASC}

**Hierarchy-Types** are the classes which are presented in the navigation lists. You have to specify a URI.
Note: The first of these resource is used as class for resources created via "Add Resource".

    config.<id>.hierarchyTypes[] = "http://www.w3.org/2002/07/owl#Class"

**Hierarchy-Relations** are used to ask for resources which have a certain parent
in addition to that, the absent of any parent is used to identify toplevel resources
there are two types of hierarchy relations: incoming and outgoing.
* outgoing means, the parent navigation resource is subject (like skos:narrower)
* incoming means, the child navigation resources are subjects (like rdfs:subClassOf).

_Note:_ Resources which occur at the object position of an incoming Hierarchy-Relation are implicitly
treated as classes even if they don't explicitly have on of the Hierarchy-Types defined.

    config.<id>.hierarchyRelations.out[] = "http://www.w3.org/2004/02/skos/core#narrower"
    config.<id>.hierarchyRelations.in[] = "http://www.w3.org/2000/01/rdf-schema#subClassOf"

**Instance-Relations** are used to create the list of resources based on the navigation entry again,
there are two types of instance relations: incoming and outgoing.
* outgoing means, the navigation resource is subject (like rdf:type)
* incoming means, the instance resources are subjects (like sioc:member_of)
  
_Note:_ Resources which occur at the object position of an incoming Instance-Relation are implicitly
treated as classes even if they don't explicitly have on of the Hierarchy-Types defined.

    config.<id>.instanceRelation.out[]  = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
    config.<id>.instanceRelation.in[]  = "http://rdfs.org/sioc/ns#member_of"

**Hidden-Namespaces** can be defined to hide resources in these namespaces. They are not visible by
default but can be activated with the option "View > Toggle Elements > Show Hidden Elements".

    config.<id>.hiddenNS[]   = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"

**Hidden-Relations** are used to hide resources which carry the defined relation.

    config.<id>.hiddenRelation[]   = "http://ns.ontowiki.net/SysOnt/hidden"

**Show implicit Elements** is a switch to show resources which don't explicitly have on of the
Hierarchy-Types defined but are implicitly treated e.g. as classes by being part e.g of an
Hierarchy-Relation or Instance-Relation.

    config.classes.showImplicitElements = {true|false}

**Show empty Elements** is a switch to show navigation-elements without instances

_Note:_ Setting this option to false CAN BE TIME CONSUMING because all instances have to be counted.

    config.<id>.showEmptyElements = {true|false}

**Show Counts** switches if instances are counted and display right next to the name.

_Note:_ Setting this option to true CAN BE TIME CONSUMING because all instances have to be counted.

    config.<id>.showCounts = {true|false}

**Check Subclasses** If set to true, navigation arrow will be visible only if there's subclasses

_Note:_ Setting this option to true CAN BE TIME CONSUMING because all subclasses have to be counted.

    config.<id>.checkSub = {true|false}

**Hide default Hierarchy** If set to true, no default hierarchy is shown and the user MUST search
for an entry in order to browse from one of the search results. This is needed for very big
databases like DBpedia

    config.<id>.hideDefaultHierarchy = {true|false}

**Root Element** option can hold an explicitly defined root element. The hierarchy will start
from this element and is restricted to this.

    config.<id>.rootElement = ""

**Root Name** will be the name/title of the root Element.

    config.<id>.rootName = ""

**TODO**
;;; If set, root node will be linked to this URI
;config.assets.rootURI = ""
**TODO**

**Top-Query** If set, the top level menu will be generated with this query

    config.<id>.query.top = "SELECT DISTINCT ?resourceUri WHERE { ?resourceUri <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://ns.ontowiki.net/classtest/RdfsClassA> }"

**Deeper-Query** If set navigate deeper queries will be generated based on this template.
`%resource%` will be replaced by the current parent resource

    config.<id>.query.deeper = "SELECT DISTINCT ?resourceUri WHERE { ?resourceUri <http://www.w3.org/2000/01/rdf-schema#subClassOf> <%resource%> OPTIONAL { ?resourceUri <http://ns.ontowiki.net/SysOnt/hidden> ?reg } FILTER (isURI(?resourceUri)) }"

**Query-List** If set, the instances list will be generated using this query

    config.<id>.list.query = "SELECT DISTINCT ?resourceUri WHERE { ?resourceUri ?p ?o . ?resourceUri <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?rdfsclassa FILTER (!isBLANK(?resourceUri)) FILTER (sameTerm(?rdfsclassa, <%resource%>)) }"

**List-Config** If set list will be generated using this JSON instanceConfig
_Note:_ All `"` must be replaced by `|`
_More info_ about [instance config](http://docs.ontowiki.net/ontowiki_Instance-Lists/).

    config.<id>.list.config = "{|filter|:[{|rdfsclass|:|%resource%|,|mode|:|rdfsclass|}]}"
