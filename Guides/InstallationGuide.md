siehe <Handbooks>

# Installation Guide

## Welcome

### Usage of this Documentation

This documentation describes the installation process of the OntoWiki and the requirements. OntoWiki relies on many external components like Apache and PHP for whose installation and configuration is not described in detail here. For those external components please refer to the manuals.

- table of external component and where to find the web documentation

- image of installation resources, this document in the middle, others around it with lines

#### Structure of this Documentation

### Installation Resources

- table with two columns, "Task" and "Section"
----------------------  ---------------------------------------------------------------
                  Task								Section
----------------------  ---------------------------------------------------------------
testtask		testsection
		

## Understanding OntoWiki Installation Concepts

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
