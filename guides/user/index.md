---
layout: page
title: Users Guide
---

# Users Guide

## Introduction
This guide is intended to provide support for first time OntoWiki users.
It assumes that you have a working installation.
For a longer and more visual introduction, [watch our webinar](http://www.youtube.com/watch?v=vP1UDKeZsQk).

## First Login
If you start with a new ontowiki installation, you have only one pre-created account: `Admin`.
This account does not have a password, so you need to change this!!

* Login with `Admin` and empty password
* Click on `User > Preferences` in the Main Box (upper left side)
* Change the password and email

## First Model
After that, you should create a new knowledge base.
A good example is the AKSW webpage knowledge base which consists of persons, projects and other related material from the AKSW research group.

* Login with `Admin` user (if not already done)
* Click on the menu entry `Edit > Create Knowledge Base` in the Knowledge Bases box
* Download the [dataset](https://raw.github.com/AKSW/aksw.org/master/site/data.rdf)
* Select "Upload from file"
* Fill in the Model URI `http://aksw.org/` and select the downloaded file
* Submit

After importing the knowledge base, you can browse persons, projects and other classes.

By default, every new user (and the anonymous user) can read every model but the two system models.
So if you logout now, you have anonymous access to your new model.
If you don't like that, you need to change that in your configuration model.

## Preconfigured Knowledge Bases
A new OntoWiki has two installed Knowledge Bases:

* `http://ns.ontowiki.net/SysOnt/` is the global system ontology which describe OntoWiki configuration concepts.
* `http://localhost/OntoWiki/Config/` is your local configuration model. It imports the global system ontology. Registered Users and ((AccessControl access control configuration)) will be saved here.
