---
title: Naming-scheme-for-cloned-resources
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_Naming-scheme-for-cloned-resources/
---
This is a writeup of the information contained in [this user group discussion](https://groups.google.com/forum/?hl=no&fromgroups=#!topic/ontowiki-user/BCssISSQoNk). Please help extend it.

# Configure extension resourcecreationuri

The extension called resourcecreationuri is responsible for selecting the naming scheme of cloned resources. It uses the literal of one or more configured propertiers from the used class to create the name.

## Tweaking the default setup 

The standard setup is to use a literal from the first type of the resource, and combine this with a literal from the resource itself. When trying to make a resource of type http://purl.org/NET/c4dm/event.owl#Event, OntoWiki will look in the namespace of your Knowledge Base for triples describing, and select a suitable literal thereof. Then OntoWiki will search the literals of the resource you are creating, and select one of them. These literals will be escaped, and combined to form a string such as "Event/The_Gathering", and this string will be appended to the base URI of your Knowledge Base. The new resource will thus be named "<name of knowledgebase>/Event/The_Gathering".

OntoWiki has a number of literals to choose from in this process. By default, prefLabel is the first choice in the ladder. For a list of possible choices, see the file ```extensions/resourcecreationuri/doap.n3``` in your OntoWiki installation directory.

To use your own naming scheme, i.e. to prioritize differently, you could create and use your own property in this file, or rearrange the order in which they appear in the list. It might be a property which is NOT used by the titleHelper and only used by the resourcecreationuri extension.
