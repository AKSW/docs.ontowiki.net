---
title: HTTP-Parameters
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_HTTP-Parameters/
---
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

