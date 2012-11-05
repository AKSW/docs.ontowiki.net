siehe <Handbooks>

# Installation Guide

## Welcome

### Usage of this Documentation

- because it contains many external components there is no extensive tutorial on installing those components, but there are links to them (like php,...)
- image of installation resources, this document in the middle, others around it with lines

#### Structure of this Documentation

### Installation Resources

- table with two columns, "Task" and "Section"
----------------------      -------------------------------------------------------------------


## Understanding OntoWiki Installation Concepts

### Terminology
### Overview of Basic Concepts
### Introduction into the OntoWiki infrastructure
- explaining apache, php, sparql endpoint

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

## Carrying out the the OntoWiki Installation

- what are the operating systems used by Daimler?

## [Carrying out the Installation](Carrying-out-the-Installation)

### VAD
### OntoWiki Installation with the Windows Installer (müsste man noch bauen?)
### (später OntoWiki Installation with an Ubuntu Image vbox image)
### ... with an Ubuntu Package
### Manual Installation
#### Windows (XAMP)
##### Virtuoso
#### Linux
##### Apache, PHP and ODBC
##### Virtuoso
##### OntoWiki
##### [Custom Startup Script for Debian](Custom-startup-script-for-Debian)
### [OntoWiki on Microsoft IIS 7](Install-on-IIS)
-> siehe auch <GetOntoWikiUsers>
### <php.ini-recommendations>
## Troubleshooting
- one trouble shooting section or several ones?
<Setup>
<Setup-on-NGINX>
<SetupDevelopers>
<VirtuosoBackend>

# Administration Guide
## Creating and Managing Accounts
### Administrator Accounts
### User Accounts
## [Creating a Backup](Backup)
## [Activate, Deactivate and Configure Extensions](Extension-Configurator)
## Extension Configuration Files doap.n3 Syntax
## Extensions (verify list)
### List of Extensions
#### account
#### application
#### auth
#### autologin
#### bookmarklet
#### ckan
#### community
#### cors
#### csvimport
#### cubeviz -> bezieht sich <Graph-Visualization> darauf?
#### datagathering
#### defaultmodel
#### exconf
#### fancystyle
#### files
#### filter
#### googletracking
#### hideproperties
#### history
#### imagelink
#### imprint
#### jsonrpc
#### linkeddataserver
#### listmodules
#### literaltypes
#### mailtolink
#### manchester
#### markdown
#### modellist
#### [navigation](Navigation-Extension)
#### page
#### [pingback](SemanticPingback)
#### queries
#### resourcecreationuri
#### resourcemodules
#### savedqueries
#### selectlanguage
#### semanticsitemap
#### sendmail
#### sindice
#### sortproperties
#### source
#### themes
#### translations
#### weblink

## Migrating OntoWiki to a seperate (different, another?) Server
- how to move or copy OntoWiki to a new machine
## Importing and Exporting Data
## Performance Tuning


# Developers Guide
## Architecture?
## [Coding Standards](Coding-Standards)
[Starting point for developers](ExtensionDeveloperStart) // rewrite this
<How-to-test>
## Extensions
### [Extension Architecture](Extension-Architecture)
### [Extension Repository](Extension-Repository)
### <Wrapper-Example>

## [Reserved HTTP Parameters](HTTP-Parameters)
<Instance-Lists>
<JavaScriptEvents>
<PHPCodeSniffer>
<PHPUnit>
<Using-the-repository>
<Webservices>

# Users Guide
## <FAQ>
## siehe <Getting-Started-Users>OntoWiki 5 min to success user stories :-)
## Taxonomy Management
### [How to create and publish a SKOS taxonomy in 5 minutes?](How-to-create-and-publish-a-SKOS-taxonomy-in-5-minutes)
### [How to view and edit the concepts of my taxonomy?](How-to-view-and-edit-the-concepts-of-my-taxonomy)
### [How to use and consume other Linked Data resources?](How-to-use-and-consume-other-Linked-Data-resources)
## Linked Data Infrastructure
### [How to publish my product information as Linked Data?](How-to-publish-my-product-information-as-Linked-Data)
### [How to consume and link product information from the Linked Data web?](How-to-consume-and-link-product-information-from-the-Linked-Data-web)
### [How to setup a Linked Data notification and synchronisation hub?](How-to-setup-a-Linked-Data-notification-and-synchronisation-hub)
noch einordnen:
<LinkedData>



noch einordnen in irgendeinem Buch
<Naming-scheme-for-cloned-resources>
<SecurityIssues> - administration?
<TitleHelper>
<Tools>
