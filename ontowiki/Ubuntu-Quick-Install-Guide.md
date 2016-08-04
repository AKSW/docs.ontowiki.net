---
title: Ubuntu-Quick-Install-Guide
tags: [ontowiki, install]
sidebar: ontowiki_sidebar
permalink: /Ubuntu-Quick-Install-Guide.html
editme_path: ontowiki/Ubuntu-Quick-Install-Guide.md
---
## Ubuntu Quick Install Guide

Installing everything you need:

    sudo apt-get install git apache2 php5 php5-odbc
    cd /var/www/html
    sudo git clone https://github.com/AKSW/OntoWiki.git

Install the newest stable Virtuoso-Opensource Version and use the guide from [here](http.//virtuoso.openlinksw.com/dataspace/doc/dav/wiki/Main/VOSUbuntuNotes) and look at **Building Virtuoso from Source**

Setting up ODBC:

You need to add things in 2 files: `odbc.ini` and `odbcinst.ini`.

On Linux systems they can be found under `/etc`

(standard path for **virtodbc.so** is **/usr/lib/odbc/**)

Add the following lines to the **odbcinst.ini** file:

    [virtuoso-odbc]
    Driver = <prefix>/lib/virtodbc.so

Add the following lines to the **odbc.ini** file:

    [ODBC Data Sources]
    VOS = Virtuoso

    [VOS]
    Driver = virtuoso-odbc
    Description = Virtuoso Open-Source Edition
    Address = localhost:1111

Test it with:

    make odbctest

Now you need to copy the **/var/www/html/OntoWiki/config.ini.dist** to **/var/www/html/OntoWiki/config.ini**
if you have changed username/password you need to change them in this file. All important lines for Virtuoso are:

    store.backend = virtuoso
    store.virtuoso.dsn = VOS
    store.virtuoso.username = dba
    store.virtuoso.password = dba

The last thing is to start virtuoso and restart apache (the virtuoso service name is an example, most likely if you installed virtuoso through the guide on the virtuoso-opensource site you will start it manually in a terminal)

    sudo service virtuoso-opensource-6.1 start
    sudo service apache2 start/restart
