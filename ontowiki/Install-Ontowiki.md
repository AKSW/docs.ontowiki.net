---
title: Install-Ontowiki
tags: [ontowiki, install]
sidebar: ontowiki_sidebar
permalink: /Install-Ontowiki.html
editme_path: ontowiki/Install-Ontowiki.md
---

## Installation

### General Tips
* For Windows user we suggest to install via the archive.
* The latest development version can be installed only from the repository.

### Installation via Archive
If you want the latest official and most stable release of OntoWiki

* Download the [archive from github](https://github.com/AKSW/OntoWiki/releases)
* Unpack it in your web directory.

**If you have no `vendor` folder in your root directory you need to run make install, running it in general might be a good idea in any case**


### Installation via Github repository
If you are a advanced user of OntoWiki and/or need the latest (sometimes unstable) version, you can checkout our repo:

* Clone the repository into your web folder (e.g. `/var/www/ontowiki`)
  * `git clone https://github.com/AKSW/OntoWiki.git`
* Run `make install` to download Erfurt, RDFAuthor, Zend and more

#### Github installation for Windows

Compiling the source code in windows can be rather tricky. You need to fullfill the requirements below, and the commands
should be in your Path. If you can't get `make` to run (the commands are mostly not windows combatible right now anyway),
you can get by with only php and git, downloading the composer.phar manually from [here](https://getcomposer.org/download/).
afterwards you run `composer install` and composer should install everything you need to run OntoWiki on Virtuoso/MySQL.
  
### Installation via composer

* If you have composer installed
  * Execute `composer create-project aksw/ontowiki --stability dev`
* If you don't have composer installed
  * Download the `composer.phar` from [the composer website][https://getcomposer.org/download/]
  * Execute `php composer.phar create-project aksw/ontowiki --stability dev`

### Installation via Debian package
If you use a Debian or Ubuntu Linux distribution, you can use the debian package instead of the archive.

* Install the LDStack repository by downloading and adding the [ldstackrepository
  install Guide](http://stack.linkeddata.org/getting-started/installing-components/)
* Update your package database (`sudo apt-get update`)
* Install `ontowiki-mysql` or `ontowiki-virtuoso` (`sudo apt-get ontowiki-virtuoso virtuoso-vad-conductor`)

Please note that OntoWiki works best with a recent version of Virtuoso. At the time of writing, OntoWiki requires version 6.1.4 or greater. Debian stable/squeeze comes with version 6.1.2, Debian testing/wheezy comes with 6.1.4, and Ubuntu 12.04 LTS comes with 6.1.4. Building virtuoso from source on a Debian based system, however, is [quite easy]({{ "VirtuosoBackend.html" | prepend:site.baseurl }}). Using a [custom startup script]({{ "Custom-startup-script-for-Debian.html" | prepend:site.baseurl }}) on Debian, you can even install the package for virtuoso and use your own locally compiled version.

## Requirements
In order to install OntoWiki you need:

* PHP 5.4 or higher (PHP 7.x isn't completely supported at the moment)
  * See this page for [recommended PHP settings]({{ "php.html" | prepend:site.baseurl }}) .
* [mod_rewrite](http://httpd.apache.org/docs/2.2/mod/mod_rewrite.html) allowed in target directory (`AllowOverride FileInfo Limit Options`, optional, used for nice URIs and LinkedData features)
  * `a2enmod rewrite`
* [.htaccess](http://httpd.apache.org/docs/2.2/configuring.html#htaccess) allowed in target directory
* git (in case you want to install it from the repository)
* make (on Linux systems usually installed) to use the Makefile
* One of these:
  * An installed [MySQL Server](http://mysql.com) or Virtuoso Server, a created database on that server and an account which is able to read and write that database or
  * An installed [Virtuoso Server](http://www.openlinksw.com/virtuoso/]]) 
* And of course the OntoWiki files.

## Setup for MySQL

If you want to use OntoWiki with MySQL, here we go ... we assume, you have a copy of OntoWiki at your webdirectory.

 1.    Create a mysql user for ontowiki (e.g. called "ontowiki")
 2.    Create a mysql database which is writable for the ontowiki user
 3.    Copy the config.ini-dist to config.ini and change the database config: in most cases, you have to change only these values store.zenddb.dbname, store.zenddb.username, store.zenddb.password
 4.    Go to the ontowiki root dir, run 'make install' - sets up Zend etc.
 5.    Open your OntoWiki Installation in your browser. On first run, all tables are created automatically and hopefully, you will see a starting screen containing a news area and a login window.

## Setup for Virtuoso
This part explains the necessary steps to use OntoWiki with [OpenLink Virtuoso](http://virtuoso.openlinksw.com/wiki/main/Main/).
For the Setup please look at the [VirtuosoBackend-site]({{ "VirtuosoBackend.html" | prepend:site.baseurl }})

## Links for Special Installations

[Install for Windows IIS]({{ "Install-on-IIS.html" | prepend:site.baseurl }})

-> The instructions above assume you already have PHP installed with IIS. If not [install PHP here](http://php.iis.net/) or [read this](http://learn.iis.net/page.aspx/246/using-fastcgi-to-host-php-applications-on-iis/) to install manually.

[Installation-Guide-Mac-OSX]({{ "Installation-Guide-Mac-OSX.html" | prepend:site.baseurl }})

[Setup-on-NGINX]({{ "Setup-on-NGINX.html" | prepend:site.baseurl }})

[Quick Install Guide for Ubuntu]({{ "Ubuntu-Quick-Install-Guide.html" | prepend:site.baseurl }})

[Custom startup script for Debian]({{ "Custom-startup-script-for-Debian.html" | prepend:site.baseurl }})
