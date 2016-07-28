---
title: JavaScriptEvents
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_JavaScriptEvents/
editme_path: ontowiki/JavaScriptEvents.md
---
overview about JavaScript events

- `data` contains objects associated with the event
- Register for an element-specific event: `$(<selector>).bind(<event\_name>, function(e, data) {/\* handler \*/});`.
- Register for a global event: `$('body').bind(<event\_name>, function(e, data) {/\* handler \*/});`
- Trigger an event: `$(<selector>).trigger(<event\_name>, data)`.

## Event List

### Global Events

- Instance list has been reloaded: `ontowiki.resource-list.reloaded`
- A resource has been selected in the list: `ontowiki.resource.selected`
- A resource has been deselected: `ontowiki.resource.unselected`
- The resource selection list has changed: `ontowiki.selection.changed`

### Element-specific Events
