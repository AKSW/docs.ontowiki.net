# Preface

This page explains the necessary steps to use OntoWiki with [OpenLink Virtuoso](http://virtuoso.openlinksw.com/wiki/main/Main/).
Especially, it covers the following topics:

* Install Virtuoso
* Download and install OntoWiki
* Configure OntoWiki to use Virtuoso

## Overview
This is the basic procedure. For details see below.

* download and install [homebrew](https://github.com/Homebrew/homebrew/wiki/Installation)
* run `brew update` to update the dependencies
* execute `brew install virtuoso` to get installed Virtuoso
* there have to be installed PHP with ODBC support `brew install php5 --with-unixodbc`
* [Set up ODBC](VirtuosoBackend#setting-up-odbc)
* Check out the OntoWiki source code 
* Set up OntoWiki to be used with Virtuoso.

## Setting up ODBC
Database connection to Virtuoso happens through ODBC. ODBC is configured by two files, `odbc.ini` and `odbcinst.ini`.
On Mac OS X systems they can be found under `/Library/ODBC`.
In case they don't exist, create them.

Add the following lines to the **odbcinst.ini** file:

    [virtuoso-odbc]
    Driver = <prefix>/lib/virtodbc.so

Add the following lines to the **odbc.ini** file:

    [ODBC Data Sources]
    VOS = Virtuoso
    
    [VOS]
    Driver = virtuoso-odbc
    Description = Virtuoso Open-Source Edition
    Address = localhost:1111

Now make sure, PHP can connect to Virtuoso via ODBC.

Newer versions of OntoWiki come with a script to test the connectivity to Virtuoso. Just type the following on the command-line while in the OntoWiki root directory:

    make odbctest

If this gives you an error like

    make: *** No rule to make target `odbctest'.  Stop.

try the following to test the connection: Create a file called `odbctest.php` in you webroot with the following PHP code in it:

    <?php
    $conn   = odbc_connect('VOS', 'dba', 'dba');
    echo odbc_errormsg();
    $query  = 'SELECT DISTINCT ?g WHERE {GRAPH ?g {?s ?p ?o.}}';
    $result = odbc_exec($conn, 'CALL DB.DBA.SPARQL_EVAL(\'' . $query . '\', NULL, 0)');
    ?>
    <ul>
    <?php while (odbc_fetch_row($result)): ?>
        <li><?php echo odbc_result($result, 1) ?></li>
    <?php endwhile; ?>
    </ul>

Execute it by clicking on this link: [http://localhost/odbctest.php](http://localhost/odbctest.php).
You should see  a list of graphs stored in your Virtuoso RDF store.
On a vanilla Virtuoso installation this list should include the following two graphs:

* http://www.openlinksw.com/schemas/virtrdf#
* http://localhost:8890/DAV

If you see this list and no error messages along the way, go ahead configuring OntoWiki.

## Configuring OntoWiki
Perform the following steps to set up OntoWiki:

* Copy `config.ini.dist` to `config.ini` and open it in a text editor
* Under `[private]`, set the following options: 

    store.backend = virtuoso
    store.virtuoso.dsn = VOS
    store.virtuoso.username = dba
    store.virtuoso.password = dba

* Optional 1: to enable OntoWiki's debug mode, add the line `debug = yes`
* Optional 2: If you didn't change any other config option, create the following directories relative to your OntoWiki installation and make them writable to the web-server user: `/cache`, `/logs`, `/uploads`.