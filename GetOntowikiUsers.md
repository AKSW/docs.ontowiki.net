## Installation for Users 

As a non-developer there a three ways to install OntoWiki (Developers look [here](SetupDevelopers)).
For Windows user we suggest to install via archive

### via archive
if you want the latest official release of OntoWiki, download the
[7zip](http://www.7-zip.org/download.html)-packed
[[archive from github|https://github.com/AKSW/OntoWiki/downloads]] and unpack it in your web directory.
Then copy `config.ini-dist` to `config.ini` and [[setup OntoWiki|Setup]].

### via github repository
If you are a advanced user of OntoWiki and/or need the latest version, you can checkout our repo:

* clone the repository into your web folder (e.g. `/var/www/ontowiki`)
  * `git clone https://github.com/AKSW/OntoWiki.git`
* go to the newly created directory and run `make deploy`
  * This will create some directories for log/cache/ ..., fetch Zend as well clone Erfurt and RDFauthor into `./libraries`
* copy `config.ini-dist` to `config.ini` and setup OntoWiki.

### via Debian package

* install the LOD2 repository by downloading and adding the [lod2repository
  package](http://stack.lod2.eu/lod2repository_current_all.deb)
* update your package database (`sudo apt-get update`)
* install `ontowiki-mysql` or `ontowiki-virtuoso` (`sudo apt-get ontowiki-virtuoso`)
* open your browser, go to [your ontowiki URL](http://localhost/ontowiki/), login as `Admin` without pass and change the password

Now you have a copy of OntoWiki, but there are also some dependiencies (MySQL etc) and configuration necessary. You can look at [[Setup]] for these next steps.