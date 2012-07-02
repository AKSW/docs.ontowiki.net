OntoWiki has been extensible since version 0.8. In OntoWiki 1.x this goes even further and the extension architecture has been simplified.

# Extension Architecture

OntoWiki extensions are stored in the extensions folder. A extension can be composed four different types of extensions:

  * Components, 
  * Modules,
  * Wrapper and
  * Plug-ins.

Additionally, we have 2 kinds of non-developer (internal) extensions, namely

  * translations and
  * themes.  

# Extensions

An extension is a meta container that can contain any/multiple of the below explained extension types. An (made up) example could look like this:

ow-root/
* index.php
* extensions/
 * files/
  * FilesController.php
  * FilesModule.php
  * RelatedFilesModule.php
  * RemoteFilesPlugin.php
  * default.ini
  * templates/
   * navigation/
    * listfiles.phtml
    * relatedfiles.phtml
    * deletefile.phtml
  * ...

This example seems rather complex but this way you will get all possibilities of a extension.
You can see that one extension folder (files) contains a controller and multiple modules and a plugin.
The files ending in 'Controller.php', 'Module.php' etc will be included by the extension Manager and the contained Controller and Modules etc. will be instantiated and handled accordingly.
The configuration that is stored in 'default.ini' is available in all of the extensions.
The 'files.ini' in the parent folder can contain customized configurations that overrides the default settings; that way you have these local changes independent from our source code versioning.
The filename of that local ini must be the name of the extension.
Then you will notice the files ending in ".phtml": these are Zend templates.
They can reside in the main extension folder or - if specified in the ini - in a subfolder.
Action templates need to be wrapped in a folder named like their controller e.g., the listfiles template corresponds to a listfiles-action in the Files-Controller (this is a Zend convention).
An example for Module templates could be the relatedfiles template. 

## Components
Components are pluggable MVC controllers to which requests are dispatched.
Usually, but not necessarily, components provide the main window's content and, in that case, can register with the navigation to be accessible by the user.
In other cases components can function as controllers that serve asynchronous requests.
Components are statically configured by a 'component.ini' file within the component's folder.

Components can be associated with a helper object that is instantiated on each request (instead of just requests the component serves).
Thus you can use a helper to do certain tasks like registering a menu or navigation component.
See also the component helper section of the RDFa Views page:
http://code.google.com/p/ontowiki/wiki/RDFaViews?ts=1243244705&updated=RDFaViews#Component_Helper

In both cases, the component controller mus extend 'OntoWiki_Controller_Component' and has therefore a number of inherited variables and methods available.
If your component needs a helper, derive you helper class from 'OntoWiki_Component_Helper'.

Typical things you can do with a Controller:

* a new tab in the main window (e.g. with your special data view)
* a new webservice service endpoint (e.g. to export data in your special way)

Components, where you can sneak good code:

* https://github.com/AKSW/OntoWiki/tree/develop/extensions/datagathering

## Modules

Modules display little windows that provide additional user interface elements with which the user can affect the main window's content.
Since some modules are highly dynamic extensions, they can be configured both statically and dynamically.
Static configuration works in the same way as with other extensions; a module.ini file is placed in the module's root directory.
In addition, a module class needs to extend 'OntoWiki_Module' and can redefine several of its methods in order to allow for dynamic customization.
If present, return values will overwrite static configuration settings in the 'module.ini' file.

Module classes must be named with an extension _Module_ appended to the module name with the first letter capitalized.

Typical things you can do with a module:

  * an additional top-left window with your specific navigation
  * an additional inner-window for your specific resource type

Modules, where you can sneak good code:

  * https://github.com/AKSW/files.ontowiki

# Plugins

Plug-ins are the most basic, yet most flexible types of extensions.
They consist of arbitrary code that is executed on certain events.
Plug-ins need to be registered for events in the 'plugin.ini' config file that has to be placed in the same folder as the plug-in class.
There is no specific base-class required for a plug-in.
The only requirement is that the class name must end with the suffix _Plugin_, which is appended to the plug-in's name (e.g. the folder) with the first letter in upper case.

Typical things you can do with a plugin:

  * an action which is executed every time a statement is added (e.g. for your specific rules)
  * just everything which is "accessible" via an event :-)

Plugins, where you can sneak good code:

  * https://github.com/AKSW/OntoWiki/tree/develop/extensions/linkeddataserver


# Events

Here is a list of events you can attach to:

## Events related to boot (occurs in this order)

  * onPostBootstrap (when ow is bootstrapped)
  * onRouteStartup
  * onRouteShutdown (when controller is found)
  * onBeforeInitController
  * onAfterInitController

  * onIsDispatchable

## Events related to things done mostly in controllers

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

# FAQ

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

  This adds a tab entry which has the title Formgenerator and will called _http://OW_URL/Formgenerator/overview_. Put this into your Helper class. 

**Q**: How can I replace OntoWiki strings? 

**A**: Provide your own language CSV file that replaces OntoWiki language keys.

**Q**: How do I get the Theme Base Dir? 

**A**: In a phtml-file, you can use $this->themeUrlBase
