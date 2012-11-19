---
layout: page
title: Concepts
---

# Understanding OntoWiki Installation Concepts

### Terminology
### Overview of Basic Concepts
### Introduction into the OntoWiki infrastructure
- explaining apache, php, sparql endpoint
- image of the stack

## Planing the OntoWiki Software System Base (wie kann man das eleganter formulieren?)

- tasks of the ontowki servers (showing wiki, doing sparql queries, storage, import, export,...)
- what are the ontowiki hardware and software minimum requirements (cpu, ram, harddrive/ssd size and speed, network bandwith, operating system type name and versions)
### Operating System

Ubuntu (latest release), any other linux distro should be fine too. Windows is possible as well.

### Webserver
Most developers are using Apache but there is also a [[setup guide for NGINX|Setup-on-NGINX]]. lighttpd should be possible too, but uses a different rewrite rule language and we don't have ported ours yet.

### PHP
5.2 or higher, more details for PHP configuration [[here|php.ini-recommendations]]

### Backend
Virtuoso Opensource Version 6.1.4 or higher, more details for installation [[here|VirtuosoBackend]]. MySQL backend is also posible but slower.

### Browser
Current Google Chrome, Safari and Firefox Browser tested, current MSIE not always tested but should work. Older browser are not fully compatible. More details [[here|Browser-Compatibility]]

### OntoWiki Version
We recommend the installation of a current snapshot release or directly from the repository.

- how does ontowiki scale with number of users and data? 
- reference to virtuoso documentation
4 gb ram
- example deployments (real life examples aksw.org, Caucasus Spiders maybe with number of accesses and data size)
<Setup>
