---
title: FAQ
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_FAQ/
---
## How can I change the start screen and get rid of the news feed?

OntoWiki is organized in terms of controllers which provide actions.
The news feed is provided by the action `news` from the controller `index`.
You can change the start screen by configuring a new action/controller in `config.ini` by adding the following section:

    index.default.controller = "[controllername]"
    index.default.action = "[actionname]"

You can add any controller/action you want here but if you want to create a simple custom start screen, you can use the [page extension](https://github.com/AKSW/page.ontowiki).
This extensions provides a generic `page` controller, which can be used to display pages (= actions) which are created in its subdirectory `page`.
After installation only an example page exists so you can test the extension with:

    index.default.controller = "page"
    index.default.action = "example"

## Why doesn't work OntoWiki after installing it on OS X?

First of all, set debug = TRUE in the config.ini.
Maybe you get an error similar to "Can't connect to mysql database 'yourdatabase'." if you use mySQL.
Try adding Port 3306 to the host in the config.ini.

It should look like this:

    store.zenddb.host = localhost:3306