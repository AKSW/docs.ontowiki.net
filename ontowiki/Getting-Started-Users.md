# Introduction
This guide is intended to provide support for first time OntoWiki users.

It assumes that you have a [working installation](GetOntowikiUsers).

For a longer and more visual introduction, [watch our webinar](http://www.youtube.com/watch?v=vP1UDKeZsQk).

## First Login
If you start with a new ontowiki installation, you have only one pre-configured account, the `SuperAdmin`. This has the same username and password as the one you set up in config.ini for accessing the database backend.

The `Admin` user exist, but has no `password`, and hence you cannot use this to log in. To enable the account, set a plain-text password for it when logged in with the `SuperAdmin` account. 

* Select the `OntoWiki System Configuration` in the `Knowledge Bases` menu
* Select `User` in the `Navigation: Classes` menu
* Select the `Admin` user from the list of resources
* Use the `Add Property` button and select `password` from the list
* Enter a plain-text temporary password for the user

Then log out `SuperAdmin` and log in with the `Admin` account. Change the password and e-mail. Then the password should now be encrypted.

* Login with `Admin` and empty password
* Click on `User > Preferences` in the Main Box (upper left side)
* Change the password and email

## Other users
* Everyone should have their own user
* Access rights for users and groups are managed with the `SuperAdmin` account

## First Model
After that, you should create a new knowledge base.
A good example is the AKSW webpage knowledge base which consists of persons, projects and other related material from the AKSW research group.

* Login with `Admin` user (if not already done), or another user with `admin` rights
* Click on the menu entry `Edit > Create Knowledge Base` in the Knowledge Bases box
* Download the [dataset](https://raw.github.com/AKSW/aksw.org/master/site/data.rdf)
* Select "Upload from file"
* Fill in the Model URI `http://aksw.org/` and select the downloaded file
* Submit

After importing the knowledge base, you can browse persons, projects and other classes.

By default, every new user (and the anonymous user) can read every model but the two system models.
So if you logout now, you have anonymous access to your new model.
If you don't like that, you need to change that in your configuration model, using the `SuperAdmin` account.

## Preconfigured Knowledge Bases
A new OntoWiki has two installed Knowledge Bases:

* `http://ns.ontowiki.net/SysOnt/` is the global system ontology which describe OntoWiki configuration concepts.
* `http://localhost/OntoWiki/Config/` is your local configuration model. It imports the global system ontology. Registered Users and ((AccessControl access control configuration)) will be saved here.

## common work flows (todo)

_Here should be an overview which work flows are exists. For everyone a picture and a lightweight description. Maybe let base workflows on concepts from Introduction_

* create an empty model + a class + instances
* view instance lists and single instances: _explain what you will see_ 
* modify an instance using rdfauthor
* browse the data using our cool modules and _show as list_ buttons
* how to use the query editor
* how to use the community features
* how to use the versioning
* enable and configure extensions: for example datagathering and linked data server (?)