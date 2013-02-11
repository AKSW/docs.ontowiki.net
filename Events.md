Events are triggered by the OntoWiki application if some thing happens, where another part of the application or an extension can react to.

Events triggered by OntoWiki are:
  * **onPostBootstrap** triggered after the bootstrap processes are finished
  * **onCreateMenu** triggered when the menues are created. Should be used to add new entries to the menu
  * **onShouldLinkedDataRedirect** … can be used to resolve a request URI to a resource
  * **onIsDispatchable**
  * **onBuildUrl**
  * **onDisplayLiteralPropertyValue**

If an extension wants to react to an event it has to define a Helper or a Plugin class with the according methods.