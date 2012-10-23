The Navigation Extension is one of the OntoWiki core extensions which are included in a vanilla OntoWiki.

## Configuration
You can configure the Navigation Extension through the [Extension Configurator](Extension Configurator) or by manually editing its DOAP-File.

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

    config.<id>.titleMode = titleHelper

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

;;; resources in this namespace are not visible by default but can be activated
config.classes.hiddenNS[]   = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
config.classes.hiddenNS[]   = "http://www.w3.org/2000/01/rdf-schema#"
config.classes.hiddenNS[]   = "http://www.w3.org/2002/07/owl#"

;;; same as ignored namespaces but by relation
config.classes.hiddenRelation[]   = "http://ns.ontowiki.net/SysOnt/hidden"

;;; If showImplicitElements is true, also resources without a type are shown in the list,
;;; when they are correctly connected with an instanceRelation
config.classes.showImplicitElements = true

;;; If set to false, empty navigation entries are not shown by default
;;; Empty means, they do not have instances
;;; THIS CAN BE TIME CONSUMING
config.classes.showEmptyElements = true

;;; If set to true, instances are counted and display right next to the name
;;; THIS CAN BE TIME CONSUMING
config.classes.showCounts = false

;;; If set to true, navigation arrow will be visible only if there's subclasses
;;; THIS CAN BE TIME CONSUMING
config.classes.checkSub = true

;;; If set to true, no default hierarchy is shown and the user MUST search
;;; for an entry in order to browse from one of the search results
;;; This is needed for very big databases like DBpedia
config.classes.hideDefaultHierarchy = false

;;; If set, the hierarchy starts from this element and is restricted to this
;config.classes.rootElement = ""

;;; If set, root node name will be changed to this
;config.classes.rootName = ""

;;; If set, root node will be linked to this URI
;config.assets.rootURI = ""

;;; If set, the top level menu will be generated with this query
;config.classes.query.top = "SELECT DISTINCT ?resourceUri WHERE { ?resourceUri <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://ns.ontowiki.net/classtest/RdfsClassA> }"

;;; If set navigate deeper queries will be generated based on this template. %resource% will be changed for parent resource
;config.classes.query.deeper = "SELECT DISTINCT ?resourceUri WHERE { ?resourceUri <http://www.w3.org/2000/01/rdf-schema#subClassOf> <%resource%> OPTIONAL { ?resourceUri <http://ns.ontowiki.net/SysOnt/hidden> ?reg } FILTER (isURI(?resourceUri)) }"

;;; If set, list will be generated using this query
;config.classes.list.query = "SELECT DISTINCT ?resourceUri WHERE { ?resourceUri ?p ?o . ?resourceUri <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?rdfsclassa FILTER (!isBLANK(?resourceUri)) FILTER (sameTerm(?rdfsclassa, <%resource%>)) }"

;;; If set list will be generated using this JSON instanceConfig
;;; All " must be replaced with |
;;; More info instance config: http://code.google.com/p/ontowiki/wiki/InstanceListSpecification
config.classes.list.config = "{|filter|:[{|rdfsclass|:|%resource%|,|mode|:|rdfsclass|}]}"

### RDFS/OWL Property Hierarchy

    config.properties.name              = "Properties"
    config.properties.titleMode            = titleHelper
    config.properties.hierarchyTypes[]     = "http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"
    config.properties.hierarchyTypes[]     = "http://www.w3.org/2002/07/owl#DatatypeProperty"
    config.properties.hierarchyTypes[]     = "http://www.w3.org/2002/07/owl#ObjectProperty"
    config.properties.hierarchyTypes[]     = "http://www.w3.org/2002/07/owl#AnnotationProperty"
    config.properties.hierarchyRelations.in[] = "http://www.w3.org/2000/01/rdf-schema#subPropertyOf"
    config.properties.instanceRelation.out[]  = "http://www.w3.org/2000/01/rdf-schema#subPropertyOf"
    config.properties.showImplicitElements = false
    config.properties.showEmptyElements    = true
    config.properties.showCounts           = false
    config.properties.hideDefaultHierarchy = false
    config.properties.checkSub = true
    config.properties.list.config = "{|shownProperties|:[{|uri|:|%resource%|,|label|:|Label 1|,|action|:|add|,|inverse|:false}],|filter|:[{|property|:|%resource%|,|filter|:|bound|}]}"

### Spatial Hierarchy
config.spatial.name = "Spatial"
config.spatial.hierarchyTypes[] = "http://ns.aksw.org/spatialHierarchy/SpatialArea"
config.spatial.hierarchyTypes[] = "http://ns.aksw.org/spatialHierarchy/Planet"
config.spatial.hierarchyTypes[] = "http://ns.aksw.org/spatialHierarchy/Continent"
config.spatial.hierarchyTypes[] = "http://ns.aksw.org/spatialHierarchy/Country"
config.spatial.hierarchyTypes[] = "http://ns.aksw.org/spatialHierarchy/Province"
config.spatial.hierarchyTypes[] = "http://ns.aksw.org/spatialHierarchy/District"
config.spatial.hierarchyTypes[] = "http://ns.aksw.org/spatialHierarchy/City"
;config.spatial.hierarchyTypes[] = "http://ns.aksw.org/spatialAddressFeatures/classes/PostalCode"
config.spatial.hierarchyRelations.in[] = "http://ns.aksw.org/spatialHierarchy/isLocatedIn"
;config.spatial.hierarchyRelations.out[] = "http://ns.aksw.org/spatialHierarchy/contains"
config.spatial.instanceRelation.out[]  = "http://ns.aksw.org/addressFeatures/physical/country"
config.spatial.instanceRelation.out[]  = "http://ns.aksw.org/addressFeatures/physical/city"
;config.spatial.instanceRelation.out[]  = "http://ns.aksw.org/addressFeatures/physical/zip"
config.spatial.titleMode = titleHelper
;config.spatial.showImplicitElements = true
;config.spatial.showEmptyElements = true
;config.spatial.showCounts = false

### Faunistics Hierarchy
config.faun.name = "Faunistics"
config.faun.hierarchyTypes[] = "http://purl.org/net/faunistics#Family"
config.faun.hierarchyTypes[] = "http://purl.org/net/faunistics#Genus"
config.faun.hierarchyTypes[] = "http://purl.org/net/faunistics#Species"
config.faun.hierarchyTypes[] = "http://purl.org/net/faunistics#Order"
config.faun.hierarchyTypes[] = "http://purl.org/net/faunistics#SubOrder"
config.faun.hierarchyRelations.in[]   = "http://purl.org/net/faunistics#subTaxonOf"
config.faun.instanceRelation.out[]  = "http://purl.org/net/faunistics#identifiesAs"
config.faun.titleMode = titleHelper
config.faun.checkSub = true
;config.faun.showImplicitElements = true
;config.faun.showEmptyElements = true
;config.faun.showCounts = false


### SKOS Hierarchy
config.skos.name = "SKOS"
config.skos.hierarchyTypes[] = "http://www.w3.org/2004/02/skos/core#Concept"
;config.skos.hierarchyTypes[] = "http://www.w3.org/2004/02/skos/core#ConceptScheme"
config.skos.hierarchyRelations.in[]   = "http://www.w3.org/2004/02/skos/core#broader"
config.skos.hierarchyRelations.out[]   = "http://www.w3.org/2004/02/skos/core#narrower"
config.skos.instanceRelation.in[]  = "http://www.w3.org/2004/02/skos/core#narrower"
config.skos.instanceRelation.out[]  = "http://www.w3.org/2004/02/skos/core#broader"
config.skos.titleMode = titleHelper
config.skos.showCounts = false

### Organizational Hierarchy
config.org.name = "Groups"
config.org.hierarchyTypes[] = "http://xmlns.com/foaf/0.1/Group"
config.org.hierarchyTypes[] = "http://xmlns.com/foaf/0.1/Organization"
config.org.hierarchyRelations.out[]   = "http://ns.ontowiki.net/SysOnt/subGroup"
config.org.instanceRelation.in[]  = "http://xmlns.com/foaf/0.1/member"
config.org.instanceRelation.out[]  = "http://xmlns.com/foaf/0.1/member_of"
config.org.titleMode = titleHelper
;config.org.showImplicitElements = true
;config.org.showEmptyElements = true
config.org.showCounts = true

### GO Hierarchy
config.go.name                    = "Gene Ontology"
config.go.hierarchyTypes[]        = "http://www.geneontology.org/dtds/go.dtd#term"
config.go.hierarchyRelations.in[] = "http://www.geneontology.org/dtds/go.dtd#is_a"
;config.go.instanceRelations.in[] = "http://www.geneontology.org/GO.format.gaf-2_0.shtml#go_id"
config.go.titleMode               = titleHelper
config.go.showCounts              = false
config.go.checkSub                = true
config.go.hideDefaultHierarchy    = false
;config.go.list.query              = "SELECT DISTINCT ?resourceUri WHERE { ?resourceUri <http://www.geneontology.org/GO.format.gaf-2_0.shtml#go_id> <%resource%>. FILTER (sameTerm(?property, <http://www.geneontology.org/dtds/go.dtd#is_a>) || sameTerm(?property, <http://www.geneontology.org/GO.format.gaf-2_0.shtml#with_from>) || sameTerm(?property, <http://www.geneontology.org/GO.format.gaf-2_0.shtml#go_id>) ) }"
config.go.list.query              = "SELECT DISTINCT ?resourceUri WHERE { ?resourceUri <http://www.geneontology.org/GO.format.gaf-2_0.shtml#go_id> <%resource%> }"

### Checklist config
config.checklist.name  = "Checklist"
config.checklist.titleMode = titleHelper
config.checklist.hierarchyTypes[] = "http://www.mindswap.org/2003/owl/geo/geoFeatures.owl#Country"
config.checklist.hierarchyRelations.in[] = "http://www.mindswap.org/2003/owl/geo/geoFeatures.owl#within"
config.checklist.checkSub = true
;config.checklist.list.config = "{|fi"ter|:[{|property|:|http://purl.org/net/faunistics#recordedAtLocation|,|filter|:|equals|,|value1|:|%resource%|,|valuetype|:|uri|}]}"
config.checklist.list.shownProperties = "{|uri|:|http://purl.org/net/faunistics#citationSuffix|,|label|:|citation suffix|,|action|:|add|,|inverse|:false}"
config.checklist.list.query = "SELECT DISTINCT ?resourceUri ?famUri WHERE {     ?recUri <http://purl.org/net/faunistics#recordedAtLocation> ?resourceLocation     OPTIONAL{         ?resourceLocation <http://www.mindswap.org/2003/owl/geo/geoFeatures.owl#within> ?l1.         OPTIONAL{             ?l1 <http://www.mindswap.org/2003/owl/geo/geoFeatures.owl#within> ?l2.             OPTIONAL{                 ?l2 <http://www.mindswap.org/2003/owl/geo/geoFeatures.owl#within> ?l3.             }         }     }     ?recUri <http://purl.org/net/faunistics#identifiesAs> ?resourceUri .     ?resourceUri <http://purl.org/net/faunistics#subTaxonOf> ?genUri .     ?genUri <http://purl.org/net/faunistics#subTaxonOf> ?famUri .     FILTER ( sameTerm(?resourceLocation, <%resource%>) ||     sameTerm(?l1, <%resource%>) ||     sameTerm(?l2, <%resource%>) ||     sameTerm(?l3, <%resource%>)) }"
config.checklist.rootName = "Caucasus Spiders"
config.checklist.rootURI = "http://db.caucasus-spiders.info/Area/152"