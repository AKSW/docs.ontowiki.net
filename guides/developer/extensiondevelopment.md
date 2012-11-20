---
layout: page
title: Extension Development 
---

# Extension Development

This is a starting point for all developers who want to create their own eLDS extensions. This includes basic PHP and Zend Skills as well as configuration and setup information for a developers PHP engine.

## Tutorials for PHP Beginners
If you are new to PHP, please have a look at one of these tutorials:
* <http://tut.php-q.net/> (en + de)
* <http://www.w3schools.com/PHP/> (en)
* <http://www.professionelle-softwareentwicklung-mit-php5.de/erste_auflage/index.html> (de)

## Tutorials for Zend Beginners
If you know PHP but not Zend, we recommend these tutorial cause it refers to the newest Zend version:  
* <http://framework.zend.com/docs/quickstart>

## PHP Configuration for Developers
All you need is to re-configure your eLDS Installation to use the **debug mode**. For this, add the following line to your `config.ini`.

     debug = on

In addition to this, we recommend the php extension [[xdebug|http://www.xdebug.org]] for all eLDS developers. **xDebug** provides stack traces and function traces in error messages with:
* full parameter display for user defined functions
* function name, file name and line indications
* support for member functions

We recommend to re-configure some php runtime variables for eLDS. Please have a look at [[Deployment-Recommendations]].

## Extension Architecture

OntoWiki extensions are stored in the extensions folder. A extension can be composed four different types of extensions:

  * Components, 
  * Modules,
  * Wrapper and
  * Plug-ins.

Additionally, we have 2 kinds of non-developer (internal) extensions, namely

  * translations and
  * themes.  

### Extensions

An extension is a meta container that can contain any/multiple of the below explained extension types. An (made up) example could look like this:

ow-root/
* index.php
* extensions/
 * files.ini
 * files/
  * FilesController.php
  * FilesModule.php
  * RelatedFilesModule.php
  * RemoteFilesPlugin.php
  * doap.n3
  * templates/
   * navigation/
    * listfiles.phtml
    * relatedfiles.phtml
    * deletefile.phtml
  * ...

This example seems rather complex but this way you will get all possibilities of a extension.
You can see that one extension folder (files) contains a controller and multiple modules and a plugin.
The files ending in 'Controller.php', 'Module.php' etc will be included by the extension Manager and the contained Controller and Modules etc. will be instantiated and handled accordingly.
The configuration that is stored in 'doap.n3' is available in all of the extensions.
The 'files.ini' in the parent folder can contain customized configurations that overrides the default settings; that way you have these local changes independent from our source code versioning.
The filename of that local ini must be the name of the extension.
Then you will notice the files ending in ".phtml": these are Zend templates.
They can reside in the main extension folder or - if specified in the ini - in a subfolder.
Action templates need to be wrapped in a folder named like their controller e.g., the listfiles template corresponds to a listfiles-action in the Files-Controller (this is a Zend convention).
An example for Module templates could be the relatedfiles template. 

### Components
Components are pluggable MVC controllers to which requests are dispatched.
Usually, but not necessarily, components provide the main window's content and, in that case, can register with the navigation to be accessible by the user.
In other cases components can function as controllers that serve asynchronous requests.
Components are statically configured by the doap.n3 file.

Components can be associated with a helper object that is instantiated on each request (instead of just requests the component serves).
Thus you can use a helper to do certain tasks like registering a menu or navigation component.
See also the component helper section of the RDFa Views page:
http://code.google.com/p/ontowiki/wiki/RDFaViews?ts=1243244705&updated=RDFaViews#Component\_Helper

In both cases, the component controller mus extend 'OntoWiki\_Controller\_Component' and has therefore a number of inherited variables and methods available.
If your component needs a helper, derive you helper class from 'OntoWiki\_Component\_Helper'.

Typical things you can do with a Controller:

* a new tab in the main window (e.g. with your special data view)
* a new webservice service endpoint (e.g. to export data in your special way)

Components, where you can sneak good code:

* https://github.com/AKSW/OntoWiki/tree/develop/extensions/datagathering

### Modules

Modules display little windows that provide additional user interface elements with which the user can affect the main window's content.
Since some modules are highly dynamic extensions, they can be configured both statically and dynamically.
Static configuration works in the same way as with other extensions; the configuration from the doap.n3 is available to the module.
In addition, a module class needs to extend 'OntoWiki\_Module' and can redefine several of its methods in order to allow for dynamic customization. 
If present, return values will overwrite static configuration settings in the 'doap.n3' file (
e.g. the method getTitle overwrites the title property).

Module classes must be named with an extension _Module_ appended to the module name with the first letter capitalized.

Typical things you can do with a module:

  * an additional top-left window with your specific navigation
  * an additional inner-window for your specific resource type

Modules, where you can sneak good code:

  * https://github.com/AKSW/files.ontowiki

## Plugins

Plug-ins are the most basic, yet most flexible types of extensions.
They consist of arbitrary code that is executed on certain events.
Plug-ins need to be registered for events in the 'doap.n3' config file.
There is no specific base-class required for a plug-in.
The only conventions are the class name and method names to catch events. The class name must end with the suffix _Plugin_, which is appended to the extensions's name (e.g. the folder) with the first letter in upper case (e.g. FilesPlugin). The method names are inspected by reflection, when a mehtod name matches a event name, that method is notified when this event is thrown.

Typical things you can do with a plugin:

  * an action which is executed every time a statement is added (e.g. for your specific rules)
  * just everything which is "accessible" via an event :-)

Plugins, where you can sneak good code:

  * https://github.com/AKSW/OntoWiki/tree/develop/extensions/linkeddataserver


## Events

Here is a list of events you can attach to:

### Events related to boot (occurs in this order)

  * onPostBootstrap (when ow is bootstrapped)
  * onRouteStartup
  * onRouteShutdown (when controller is found)
  * onBeforeInitController
  * onAfterInitController

  * onIsDispatchable

### Events related to things done mostly in controllers

related to changes to the ontology

  * beforeExportResource
  * onDeleteResources
  * onPreDeleteModel

related to the view

  * onDisplayMainWindowTitle
  * onBuildUrl
  * onCreateMenu
  * onCreateToolbar
  * onDisplayLiteralPropertyValue
  * onDisplayObjectPropertyValue
  
  * onPrePropertiesContentAction
  * onPreTabsContentAction
  * onPropertiesAction
  * onPropertiesActionData
  * onUpdateServiceAction

old page: http://ontowiki.net/Projects/OntoWiki/EventPluginArchitecture

## FAQ

**Q**: How do I create a new tab? 

**A**: A tab in OntoWiki needs to be registered with `OntoWiki_Navigation`. Main structure:

    OntoWiki_Navigation::register(
        $tabKey, 
        array(
            'controller' => $controllerName, 
            'action'     => $actionName, 
            'name'       => $displayedName, 
            'position'   => $position, 
            'active'     => $activeTab
        )
    );

With data:

    // Add entry in tab list
    OntoWiki_Navigation::register(
       'formgenerator', 
       array(
           'controller' => 'Formgenerator', 
           'action'     => 'overview', 
           'name'       => 'Formgenerator',
           'priority'   => 100
       )
    );

  This adds a tab entry which has the title Formgenerator and will called <http://OW_URL/Formgenerator/overview>. Put this into your Helper class. 

**Q**: How can I replace OntoWiki strings? 

**A**: Provide your own language CSV file that replaces OntoWiki language keys.

**Q**: How do I get the Theme Base Dir? 

**A**: In a phtml-file, you can use $this->themeUrlBase

## Extension Repository

We got a centralized Repository for extensions. Every OntoWiki can browse the available extensions and provides a install mechanism: in the [Extension-Configurator] or directly at http://your-ontowiki/exconf/explorerepo

The Repository is quite unique. It is basically a SPARQL-endpoint, which contains a repo model which imports multiple extension-models. A extension model contains DOAP data. The client within the Extension Configurator queries this model for all doap:Projects (which are extensions in our case).

This is what the list of available extenions looks like:
![repoclient](https://github.com/AKSW/OntoWiki/wiki/images/exconf-explore.png)

You can register new extensions [here](http://extensions.ontowiki.net). 
![reposerver](https://github.com/AKSW/OntoWiki/wiki/images/reposerver.png)

Registering a new or updated extension with our repo is basically just a import of its DOAP description into the repo model.
As the [short documentation](http://extensions.ontowiki.net/Help.html) says there are four steps to register a new extension, which we will explain a bit deeper here.

### Develop your OntoWiki extension and release it somewhere 
Develop the source files ([HowTo](Extensions)), test your extensions locally, package into a zip archive, put it on a accessable webserver. We recommend GitHub (you will have the autogenerated zip of the current state there).
### Create an RDF document which describes your extension 
"eat your semantic dogfood" - create a [DOAP](https://github.com/edumbill/doap/wiki) file (as Turtle, NTriple or RDF/XML). Have a look [here](https://github.com/AKSW/site.ontowiki/blob/master/doap.n3) for an example on what properties are required. For example: 
* name (doap:name - the internal id of the extension. e.g. the folder name), 
* title (rdfs:label - the human readable name, 
* author (doap:maintainer - a URI for the author), 
* description (doap:description - a short abstract of what the extension does), 
* link to the zip - either from the versions (property: doap:file-release) or from the project (property:  http://ns.ontowiki.net/SysOnt/ExtensionConfig/latestZip) (protip: if you use GitHub, this link can be omitted and the autogenerated zip of the master branch will be used), 
optional: 
* versions (older versions with each a zip), 
* extensions-internal config (look at the example - we came up with a rather complex way to encode multidimensional config arrays)
optional: if you already have a default.ini file you can convert it with the file `application/scripts/extensions-ini2n3.php` (which takes a extension folder as an argument) (the script is currently only in the feature/semantic-extensions branch). This script is especially usefull when you have many config options.

### Publish that description document as Linked Data on the web 
If you use GitHub, and you use the URL of the DOAP file as the URI of your extension (use that URI within the DOAP file), you will get pseudo-linked-data for free. for example the URI of the "site" extensions is https://github.com/AKSW/site.ontowiki/raw/master/doap.n3#site (notice the "raw", which delivers the file and not a html view on it)

#### Ping this registry to integrate your extension meta data here 
Either you enter this URI in the form on http://extensions.ontowiki.net and hit submit 

or (much more awesome) you "ping" the repository with a [semantic pingback](http://aksw.org/Projects/SemanticPingBack). The pingback should go to the pingback service at http://extensions.ontowiki.net/pingback/ping/ and should contain following data:

* source: _yourExtensionURI_ (e.g. https://github.com/AKSW/site.ontowiki/raw/master/doap.n3#site)
* target: https://github.com/AKSW/site.ontowiki/raw/master/doap.n3#site
* comment: _is ignored_

Your DOAP file should contain a triple which connects your extension with our repository e.g.:
`<yourExtensionURI> <http://ns.ontowiki.net/SysOnt/ExtensionConfig/registeredAt> <http://extensions.ontowiki.net/repository>`

The Repository listens to this event and will then retrieve your DOAP file and update its index. Your extensions becomes visible to millions of OntoWiki instances within seconds.

## HTTP Parameters

There are some HTTP parameters that are reserved by the base OntoWiki system. Hence these parameters should not be used for new functionality. The following table contains a enumeration of these parameters together with a short description.


| **HTTP Parameter** | **Description** |
| m | This parameter is used to set the model (graph) used for the request. |
| r | This parameter is used to identify the resource used for the request. |
| p | This parameter is used for paging purposes (pagenumber). |
| limit | This parameter is used for paging purposes (number of elements per page). |
| instancesconfig | This parameter is used for the configuration of resource lists (e.g. all instances of a class, and then filters etc). |
| init | This parameter is used to reset the current configuration of resource lists. |
| s | This parameter is used for search queries. |
| class | This parameter is used to get a resource lists containing all instances of a class - should be deprecated by instancesconfig. |
