Welcome to the OntoWiki users and developers wiki. It documents installation and development details. If you can't find the answers you coming here for, please have a try to our mailing lists ([**User Discussions**](http://groups.google.com/group/ontowiki-user), [**Developer Talk**](http://lists.informatik.uni-leipzig.de/mailman/listinfo/ontowiki-dev)). 

# What is OntoWiki? What can it do for you?

OntoWiki is a semantic application as well as a framework which acts as a hardened basement for your application in the Semantic Web context. One of its main purposes is to assist you managing your knowledge. Knowledge means here machine readable data organized as [RDF/XML](http://en.wikipedia.org/wiki/RDF/XML), [Notation3](http://en.wikipedia.org/wiki/Notation3), Turtle as well as [Talis(JSON)](http://docs.api.talis.com/platform-api/output-types/rdf-json). You organize your knowledge using an feature-rich user interface managing classes, properties and resources. *If you don't know what is this all about, please have a look [here](http://en.wikipedia.org/wiki/Semantic_Web) (and associated pages) before continue reading*. Furthermore what OntoWiki can do for you:
* Providing feature rich user interface to helping you organize and manage resources, relations between resources, classes, ... . We heavily use modern browser technologies to give you a smooth user experience.
* It is a [Linked Data](http://www.w3.org/standards/semanticweb/data) server for you data as well as a [Linked Data](http://www.w3.org/standards/semanticweb/data) client to fetch additional data from the web
* It is a Semantic Pingback Client in order to receive and send back-linking request as known from the blogosphere
* You can use the backend you know to store your data, because OntoWiki is backend independent, which means you can save your data on a MySQL database as well as on a Virtuoso Triple Store

But thats not all, OntoWiki provides a rich set of extensions. In the following a collection:
* Wikipedia like [Wiki's](https://github.com/AKSW/article.ontowiki/wiki): create wiki pages using Markdown and have to possibility to attach wiki pages to existing resources
* [PubSubHubbub](https://github.com/AKSW/pubsub.ontowiki#pubsubontowiki) to spread your local knowledge changes over the web and be synced with foreign sources 
* Extension named [CubeViz](https://github.com/AKSW/cubeviz.ontowiki/wiki) for visualization of statistical data which are organized in the [DataCube](http://www.w3.org/TR/vocab-data-cube/) format. OntoWiki + CubeViz are already in use for the [Open Data portal](http://open-data.europa.eu/en/apps) of the European Union!
* [Integration](https://github.com/AKSW/map.ontowiki) of maps - if your data containing geographical information you are able to see it on a map

# Informations

For informations regarding [[Browser Compatability|Browser-Compatibility]]

For informations regarding [[Backup your Data|Backup-your-data]] 

If you want to visualize your Graph look [[here|Graph-Visualization]]

[[Custom startup script for Debian|Custom-startup-script-for-Debian]]

[[Using reverse Proxy with SSL for OntoWiki|OntoWiki-behind-a-reverseProxy-(with-SSL)]]

[[Performance Tuning|Performance-Tuning]]

[[Security Issues|SecurityIssues]]



# Users

If this is your first time with OntoWiki you might want to read the following pages:
* [[Install Ontowiki|Install-Ontowiki]]
* [[Get Started using OntoWiki|Getting-Started-Users]]

If you are having some trouble, you should look at our [[FAQ Page|FAQ]] . There might be just the right answer for your problems.

If you want to publish Linked Data you should look [[here|LinkedData]]

For more complex User-Stories look [[here|User-Stories]]

# Developers

If you have some experience with OntoWiki and PHP, JavaScript or RDF you might want to help us improving this software. Interesting pages for you are:

### Getting started
* [[Install Ontowiki|Install-Ontowiki]]
* [[Setup a Test Environment|PHPUnit]]
* [[Starting the Development of a new Extension|placeholder-extensions]]
* [[CSS-Development|CSS-Development]]
* [[Writing tests|OntoWiki-Testing-Guide]]
* [[Instance Lists|Instance-Lists]]
* [[Helpful Tools|Tools]]
* [[Webservices|Webservices]]
* [[Worker Background Jobs using Gearman|Worker:-Background-jobs-using-Gearman]]
* [[Wrapper Example|Wrapper-Example]]
* Introductions to [[coding standards|Coding-Standards]] we are working with and while you are at it, you should take a look at our [[HTTP-Parameters-Page|HTTP-Parameters]]

### OntoWiki application
* [[Information about classes|Classes]]
* [[Information about controllers|Controllers]]
* [[Information about events|Events]]

There is also an API-Documentation available [http://api.ontowiki.net/].

You might want to pick up one of the problems, posted on our [[Roadmap|Roadmap]] (needs to get actualized)

# Professional Support
AKSW gives professional support for deployment and customization. Please ask [[Philipp Frischmuth|http://aksw.org/PhilippFrischmuth.html]] and [[Natanael Arndt|http://aksw.org/NatanaelArndt.html]] regarding this