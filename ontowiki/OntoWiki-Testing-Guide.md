# Structure

1. Setup environment
    1. Prerequisites
    2. General
    3. Vagrant
    4. LAMP?  
2. Unit tests
    2.1. Execute unit tests
    2.2. Write unit tests for classes
    2.3. Write unit tests for controllers
3. Integration tests
    3.1. Execute integration tests
    3.2. Write integration tests for classes
    3.3. Write integration tests for controllers
4. Extension tests
    4.1. Execute extensions tests
    4.2. Write extension tests for classes
    4.3. Write extension tests for controllers
5. Specialities
   5.1. Testing code that fetches something from the web
   5.2. Testing code that reads/writes to the triples store
6. FAQ
7. References

* [PHPUnit manual](http://www.phpunit.de/manual/current/en/)

# 1. Setup Environment

## 1.1. Prerequisites

* Install [PHPUnit](http://www.phpunit.de/manual/current/en/installation.html)
    * Min version 3.5.5
* OPTIONAL For code coverage support Xdebug needs to be installed
    * [Xdebug](http://xdebug.org/docs/install)
* OPTIONAL Vagrant
    * Download [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and install the package
    * Download [Vagrant](http://downloads.vagrantup.com/) and install the package
    * Install vbguest plugin: `vagrant gem install vagrant-vbguest`

## 1.2. General

1. Clone OntoWiki from Github: `git clone git@github.com:AKSW/OntoWiki.git`
2. Run `make install`
    * If you have Zend already in your include path, make sure to remove it from the `libraries` folder after running this command.
3. Run `make test`

The output should look something like this:

    make test-unit
    rm -rf cache/* logs/*
    mkdir -p logs cache
    chmod 777 logs cache extensions
    PHPUnit 3.7.13 by Sebastian Bergmann.

    ................................................................. 65 / 89 ( 73%)
    ........................

    Time: 3 seconds, Memory: 35.00Mb

    OK (89 tests, 158 assertions)

    -----------------------------------

    make test-integration-virtuoso
    rm -rf cache/* logs/*
    mkdir -p logs cache
    chmod 777 logs cache extensions
    PHPUnit 3.7.13 by Sebastian Bergmann.

    SSSSSSSSSSSSSSSSSSSSSSS

    Time: 11 seconds, Memory: 32.75Mb

    OK, but incomplete or skipped tests!
    Tests: 23, Assertions: 0, Skipped: 23.

    -----------------------------------

    make test-integration-mysql
    rm -rf cache/* logs/*
    mkdir -p logs cache
    chmod 777 logs cache extensions
    PHPUnit 3.7.13 by Sebastian Bergmann.

    SSSSSSSSSSSSSSSSSSSSSSS

    Time: 1 second, Memory: 34.25Mb

    OK, but incomplete or skipped tests!
    Tests: 23, Assertions: 0, Skipped: 23.

    -----------------------------------

    make test-extensions
    rm -rf cache/* logs/*
    mkdir -p logs cache
    chmod 777 logs cache extensions
    PHPUnit 3.7.13 by Sebastian Bergmann.

    ...........

    Time: 2 seconds, Memory: 39.75Mb

    OK (11 tests, 59 assertions)

## 1.3. Vagrant

0. Make sure you have Vagrant installed (see prerequisites)
1. Go to the root folder of your OntoWiki checkout
2. run `make vagrant`

This will symlink a default vagrant file from `application/scripts/Vagrantfile-dist`. If you copy this file to `application/scripts/Vagrantfile` prior of calling `make vagrant`, this file will be used instead. This enables you to make changes to your Vagrant setup (e.g. another IP) without creating a Git status.

3. Run `vagrant up`

The first time you call this command it may take a while, since the Guest additions may be updated to fit your Virtual Box version. It also needs to provision the base VM.

This command sometimes fails the first time you run it, e.g. with an error message like this:

    The following SSH command responded with a non-zero exit status.
    Vagrant assumes that this means the command failed!

    mount -t vboxsf -o uid=`id -u vagrant`,gid=`id -g vagrant` manifests /tmp/vagrant-puppet/manifests

Don't bother, just run `vagrant reload`. You may have to enter your password, since NFS is used for performance reasons.

4. Run `vagrant ssh`
5. Run `cd /vagrant`

This is where the OntoWiki root folder is mounted to.

6. Run `make test`

# 2. Unit tests

## 2.1. Execute unit tests

1. Use make
    * `make test-unit`
    * `make test-unit-cc``

2. Do it manually
    * `cd application/tests`
    * `phpunit --bootstrap Bootstrap.php unit/` (without code coverage report)
    * `cd application/tests/unit` and then `phpunit` (with code coverage report)

This way you can also test individual test classes, e.g. by issuing

    phpunit --bootstrap Bootstrap.php unit/controller/IndexControllerTest.php

Your code coverage report (if enabled) will be found in the `build/coverage` folder.

## 2.2. Write unit tests for classes

* e.g. unit/OntoWiki/NavigationTest.php

## 3. Integration Tests

## 3.1. Run

## 3.2. Write integration tests for classes

* e.g. 

## 3.2. Write integration tests for controllers


