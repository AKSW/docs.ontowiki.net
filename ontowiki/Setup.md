---
title: Setup
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_Setup/
---
After install (see [GetOntowikiUsers](Guide)), you will have to follow these steps to get OntoWiki up and running.

( [Ubuntu-Quick-Install-Guide](Quick+Install+for+Ubuntu))

# Requirements

In order to install OntoWiki you need:

- PHP 5.4 or higher
  - See our page for [php.ini-recommendations](recommended+PHP+settings).

- [http:_httpd.apache.org/docs/2.2/mod/mod\_rewrite.html_](mod_rewrite) allowed in target directory (<tt>AllowOverride FileInfo Limit Options</tt>, optional, used for nice URIs and LinkedData features)
  - <tt>a2enmod rewrite</tt>

- [http:_httpd.apache.org/docs/2.2/configuring.html#htaccess_](.htaccess) allowed in target directory
- git (The deploy target in the Makefile uses it)
- One of these:
  - An installed [http:_mysql.com_](MySQL+Server) or Virtuoso Server, a created database on that server and an account which is able to read and write that database or
  - An installed [http:_www.openlinksw.com/virtuoso/_](Virtuoso+Server) (see UsingOntoWikiWithVirtuoso for more information about OntoWiki and Virtuoso) 

- And of course the OntoWiki files. See [GetOntowikiUsers](GetOntowikiUsers)

to setup this LAMP environment you can for example use this [http:_www.howtoforge.com/installing-apache2-with-php5-and-mysql-support-on-ubuntu-12.04-lts-lamp_](guide)

# Installation

This installation guide is for MySQL Backend users. If you want to use OntoWiki with Apache and Virtuoso or within Virtuoso as a VAD Package please have a look at our Virtuoso Setup Guide: [VirtuosoBackend](VirtuosoBackend)

If you want to use OntoWiki with MySQL, here we go ... we assume, you have a copy of OntoWiki at your webdirectory.

1. create a mysql user for ontowiki (e.g. called "ontowiki")
2. create a mysql database which is writable for the ontowiki user
3. copy the config.ini-dist to config.ini and change the database config: in most cases, you have to change only these values store.zenddb.dbname, store.zenddb.username, store.zenddb.password
4. go to the ontowiki root dir, run 'make deploy' - sets up Zend etc.
5. open your OntoWiki Installation in your browser. On first run, all tables are created automatically and hopefully, you will see a starting screen containing a news area and a login window.

# After Installation / First Steps

Now you have a fresh new OntoWiki installation. If you are new to OntoWiki, maybe it is interesting for you to visit out first steps documentation: [Getting-Started-Users](Getting-Started-Users).

In case you need further help or want to communicate with other users and the developers, feel free use the OntoWiki User Mailinglist at Google Groups: [http://groups.google.com/group/ontowiki-user](http://groups.google.com/group/ontowiki-user).

