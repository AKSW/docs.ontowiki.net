## Installation for Developer

* optional: fork the repository
* clone the repository into your web folder (e.g. `/var/www/ontowiki`)
* enable Apaches rewrite  module (e.g. `a2enmod rewrite`)
* run `make install` to download Zend, init git submodules as well as to create log and cache dir
* copy `config.ini-dist` to `config.ini` and modify it according to your store
* open your browser, go to your ontowiki URL, login as `Admin` without pass and change the password
* make sure you create your own feature branch
