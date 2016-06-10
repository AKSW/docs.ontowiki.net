---
title: GetOntoWikiUsers
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_GetOntoWikiUsers/
---
# Installation for Users

As a non-developer there a three ways to install OntoWiki (Developers look [here](SetupDevelopers)).

* For Windows user we suggest to install via the archive.
* The smoothest way is to use the debian package.
* The latest development version can be installed only from the repository.

You will also find further details at: [Carrying out the Installation](ontowiki_Carrying out the Installation).

## via archive
if you want the latest official and most stable release of OntoWiki

* download the [7zip](http://www.7-zip.org/download.html)-packed [archive from github](https://github.com/AKSW/OntoWiki/downloads)
* unpack it in your web directory.

## via Debian package
If you use a Debian or Ubuntu linux distribution, you can use the debian package instead of the archive.

* install the LDStack repository by downloading and adding the [ldstackrepository
  install Guide](http://stack.linkeddata.org/getting-started/installing-components/)
* update your package database (`sudo apt-get update`)
* install `ontowiki-mysql` or `ontowiki-virtuoso` (`sudo apt-get ontowiki-virtuoso virtuoso-vad-conductor`)

Please note that OntoWiki works best with a recent version of Virtuoso. At the time of writing, OntoWiki requires version 6.1.4 or greater. Debian stable/squeeze comes with version 6.1.2, Debian testing/wheezy comes with 6.1.4, and Ubuntu 12.04 LTS comes with 6.1.4. Building virtuoso from source on a Debian based system, however, is [quite easy|VirtuosoBackend]]. Using a [[custom startup script](ontowiki_CustomDebianStartupScript) on Debian, you can even install the package for virtuoso and use your own locally compiled version.

## via github repository
If you are a advanced user of OntoWiki and/or need the latest (sometimes unstable) version, you can checkout our repo:

* clone the repository into your web folder (e.g. `/var/www/ontowiki`)
  * `git clone https://github.com/AKSW/OntoWiki.git`
* run `make deploy` to download Erfurt, RDFAuthor and Zend
  * If Zend Libraries are already present on your system and you get errors about not being able to instantiate Zend classess, move the 'libraries/Zend' folder out of the way.

# setup
[setup OntoWiki](ontowiki_Setup)
