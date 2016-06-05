---
title: Page-extension
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_Page-extension/
---
The Page Extension shows static HTML on OntoWiki and has to be manually installed.

## Installation

* requires access to AKSW db0 Server, please improve this if you know how to install it better

Copy the page folder from fts:

    scp -r root@db0:/var/www/fts.publicdata.eu/extensions/page . 

Add the following to `/var/www/myontowiki/config.ini`:

    index.default.controller = "page"
    index.default.action = "startpage"

Create the file `extensions/page.ini` and write "enabled = true" in it.

Clean the extension cache with `make clean`. You should now find the pages extension activated in your extension list and on the main page should be the content of your startpage.phtml.

## Configuration
Edit `myontowiki/extensions/page/page/startpage.phtml`.
