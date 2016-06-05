---
title: troubleshooting
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_troubleshooting/
---
# Troubleshooting
## In case OntoWiki isn't loaded correctly after you followed this tutorial
Go to `...\htdocs\elds\config.ini` and set `debug = true`. After a restart you should now see an error message in your browser which should hopefully point you to the source of the problem (if not, [create an issue](https://github.com/AKSW/OntoWiki/issues/new)). TODO: change to new url

## Error on bootstrapping application: Unable to connect to Virtuoso Universal Server via ODBC
Make sure that the Virtuoso service is started. If it does not start, look for files named `virtuoso.lck` in your Virtuoso folder under `database` or `virtuoso` and delete them if existing.
