---
title: Events
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_Events/
editme_path: ontowiki/Events.md
---
Events are triggered by the OntoWiki application if some thing happens, where another part of the application or an extension can react to.

Events triggered by OntoWiki are:
  * **onPostBootstrap** triggered after the bootstrap processes are finished
  * **onCreateMenu** triggered when the menues are created. Should be used to add new entries to the menu
  * **onShouldLinkedDataRedirect** … can be used to resolve a request URI to a resource
  * **onIsDispatchable**
  * **onBuildUrl**
  * **onDisplayLiteralPropertyValue**

If an extension wants to react to an event it has to define a Helper or a Plugin class with the according methods.

All Events can be listed using the following command (supported by Sebastian Hellmann)

`grep -R "new Erfurt_Event" * 2> /dev/null | sed "s/.*new Erfurt_Event('//;s/');.*//"  | sort -u`

(best in OW root)

Currently following events are listed:

* beforeExportResource
* onAddMultipleStatements
* onAddStatement
* onAfterInitController
* onBeforeInitController
* onBeforeInitialisingStore
* onBeforeLinkedDataRedirect
* onBuildUrl
* onCreateMenu
* onCreateToolbar
* onDatagatheringComponentSearch
* onDeleteMatchingStatements
* onDeleteMultipleStatements
* onDeleteResources
* onDisplayLiteralPropertyValue
* onDisplayMainWindowTitle
* onDisplayObjectPropertyValue
* onIsDispatchable
* onNavigationEndOutput
* onNavigationStartOutput
* onNeedsGraphForLinkedDataUri
* onNeedsLinkedDataUri
* onPingReceived
* onPostBootstrap
* onPreDeleteModel
* onPrePropertiesContentAction
* onPreTabsContentAction
* onPropertiesAction
* onPropertiesActionData
* onRouteShutdown
* onRouteStartup
* onShouldLinkedDataRedirect
* onUpdateServiceAction
