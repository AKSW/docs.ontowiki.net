## Installation for Users 

As a non developer there a three ways to get the OntoWiki source files.

### via archive
if you want a stable OntoWiki get our latest official release
[[archive|https://github.com/AKSW/OntoWiki/downloads]]

### via github repository
If you are a advanced user of OntoWiki and/or need the latest version, you can checkout our repo:

* clone the repository into your web folder (e.g. `/var/www/ontowiki`)
  * when you want to push (upload) changes you made back to us, you need to clone with ssh:
  * `git clone git@github.com:AKSW/OntoWiki.git`
  * if you want a read only copy you can do a
  * `git clone git://github.com/AKSW/OntoWiki.git`

### via Debian package

* install the LOD2 repository by downloading and adding the [lod2repository
  package](http://stack.lod2.eu/lod2repository_current_all.deb)
* update you package database (`sudo apt-get update`)
* install `ontowiki-mysql` or `ontowiki-virtuoso` (`sudo apt-get ontowiki-virtuoso`)
* open your browser, go to [your ontowiki URL](http://localhost/ontowiki/), login as `Admin` without pass and change the password

Now you have a copy of OntoWiki, but there are also some dependiencies (MySQL etc) and configuration necessary. You can look at [[Setup]] for these next steps.
