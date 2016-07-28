---
title: Deployment-Recommendations
tags: [ontowiki, install]
sidebar: ontowiki_sidebar
permalink: /ontowiki_Deployment-Recommendations/
editme_path: ontowiki/Deployment-Recommendations.md
---
## Operating System

Ubuntu and Debian (latest release), any other Linux distributions should be fine too. (If you have tried a setup on other Linux distributions or even other Operating systems, reports about special issues would be interesting for us too. Please report them at our mailing list: ontowiki-user@googlegroups.com.)

## Webserver

Most developers are using Apache but there is also a [Setup-on-NGINX](http://docs.ontowiki.net/ontowiki_Setup-on-NGINX/). lighttpd should be possible too, but uses a different rewrite rule language and we don't have ported ours yet.

## PHP

5.2 or higher, more details for PHP configuration [php.ini-recommendations](http://docs.ontowiki.net/ontowiki_php/)

## Backend

- Virtuoso Opensource Version 6.1.4 or higher, more details for installation [VirtuosoBackend](http://docs.ontowiki.net/ontowiki_VirtuosoBackend/)
- A MySQL backend is also available but slower and it should be seen as experimental

## Browser

Current Google Chrome, Safari and Firefox Browsers are tested. Current MS-IE are not always tested but should work. Older browser are not fully compatible. More details [Browser-Compatibility](http://docs.ontowiki.net/ontowiki_Browser-Compatibility/)

## OntoWiki Version

We recommend the installation of a current snapshot release (e.g. from the [releases](https://www.github.com/AKSW/OntoWiki/releases)) or directly via from the [repository](https://www.github.com/AKSW/OntoWiki).

## Professional Support

AKSW gives professional support for deployment and customization. Please ask [Natanael Arndt](http://aksw.org/NatanaelArndt) [Philipp Frischmuth](http://aksw.org/PhilippFrischmuth) or regarding this.
