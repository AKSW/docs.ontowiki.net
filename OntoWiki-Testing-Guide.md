# Structure

1. Setup environment
    1. Prerequisites
    2. General
    3. Native packages
    4. Vagrant
    5. LAMP?  
2. Unit tests
3. Integration tests
4. Extensions tests
5. FAQ

# 1. Setup Environment

## 1.1. Prerequisites

## 1.2. General

1. Clone OntoWiki from Github: `git clone git@github.com:AKSW/OntoWiki.git`
2. Run `make install`
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
