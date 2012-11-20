---
layout: page
title: Available Extensions
---

# Available Extensions

eLDS can be extended by various different extensions. They enable you to tune it as you want to fit you needs.

# Extension Documentation
You will find some information what a particular extension does, how it works and which possibilities you have to configure it.

## Core Extensions
Extensions which are delivered with a vanilla OntoWiki. (Some extensions are required for OntoWiki to run, you can't disable them.)

* [Navigation Extension](Navigation Extension) _required_
* [Resource Creation Extension](Resource Creation Extension)

# Extension API and Development
[Extension Architecture](Extension Architecture),
[Extension Configurator](Extension Configurator),
[Extension Repository](Extension Repository),
[ExtensionDeveloperStart](ExtensionDeveloperStart)

In eLDS 0.9.6 we introduced a graphical backend to configure extensions. The site admin can enable and disable extensions, set configuration values and browse a central repository of additional extensions and install them into his eLDS instance.

When you are logged in as Admin or SuperAdmin, you will notice the "Configure Extensions" menu item in the Extras menu:
![the configurator](https://github.com/AKSW/OntoWiki/wiki/images/exconf-open.png)

Alternatively you can open http://your-ontowiki/exconf
you will see a overview of which extension are installed and which are activated:
![the configurator](https://github.com/AKSW/OntoWiki/wiki/images/exconf-list.png)
by clicking on the name or the edit button, you will see the detailed config of that extension:
![the configurator](https://github.com/AKSW/OntoWiki/wiki/images/exconf-configure.png)
you can changes values here. If you do so, a special file will be created in the extension folder named "extension-name.ini" also called local ini. This file is a copy of the default.ini (which should not be changed) and overwrite these settings. That means your local config is independent from the (versioned) default.ini. A current limitation is that is you delete a config key in your local config, the value from the default config is still present and thus sets the value to its default value. You can also change the structure of the config (which is usefull for example in the navigation config), but if the extension does not expect to a (partly) arbitrary config, you will get unexpected behaviour.

If you click the "Explore Repo" tab, you will see a list of extensions present in our repository at http://extensions.ontowiki.net. Read more about [here](Extension-Repository).
![the configurator](https://github.com/AKSW/OntoWiki/wiki/images/exconf-explore.png)

# Available Extensions
TODO: get documentation from submodules
## account
## application
## auth
## autologin
## bookmarklet
## ckan
## community
## cors
## csvimport
## cubeviz
## datagathering
## defaultmodel
## exconf
## fancystyle
## files
## filter
## googletracking
## hideproperties
## history
## imagelink
## imprint
## jsonrpc
## linkeddataserver
## listmodules
## literaltypes
## mailtolink
## manchester
## markdown
## modellist
## [navigation](Navigation-Extension)
## page
## [pingback](SemanticPingback)
## queries
## resourcecreationuri
## resourcemodules
## savedqueries
## selectlanguage
## semanticsitemap
## sendmail
## sindice
## sortproperties
