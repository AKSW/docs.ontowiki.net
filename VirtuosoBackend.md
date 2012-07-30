# Virtusoso Backend

This page explains the necessary steps to use OntoWiki with [OpenLink Virtuoso](http://virtuoso.openlinksw.com/wiki/main/Main/).
Especially, it covers the following topics:

* Install Virtuoso
* Configure OntoWiki to use Virtuoso
* Other Virtuoso backend specific details

## Overview
This is the basic procedure. For details see below.

* Check out the OntoWiki source code
* Download [Virtuoso Open-Source Edition](http://sourceforge.net/projects/virtuoso/) and compile it according to the instructions for your operating system. Make sure to get the latest stable branch available.
* Install and configure Virtuoso.
* [Set up ODBC](http://www.iodbc.org/dataspace/iodbc/wiki/iODBC/IODBCPHPHOWTO) and make sure, PHP can connect to Virtuoso via ODBC.
* Set up OntoWiki to be used with Vrituoso.

## Compiling Virtuoso
For some OS, e.g. Windows, binaries exist. If you have to compile it, it is recommended to give a `<prefix>`, which will be the path where Virtuoso will be installed.

**Debian/Ubuntu** recommendation: use `./configure --prefix=/opt/virtuoso`. Virtuoso also comes along with a good README with further instructions.

Debian/Ubuntu Tipp:  configuring with the libreadline library allows for better characters passing to isql command line client '--with-readline=path/to/libreadline' (use ` apt-get install libreadline5-dev` and '--with-readline=/usr/lib/libreadline.so').

    sudo ./configure --prefix=/opt/virtuoso-opensource-version --with-readline=/usr/lib/libreadline.so

Nethertheless, you have to configure the DirsAllowed variable and configure ODBC. Or get the official debian package from Debian:squeeze repository. See: http://packages.debian.org/squeeze/virtuoso-opensource

Compiling Virtuoso requires the following build tools be installed:
[autoconf 2.57](http://www.gnu.org/software/autoconf/),
[automake 1.7](http://www.gnu.org/software/automake/),
[libtool 1.5](http://www.gnu.org/software/libtool/),
[flex 2.5.33](http://flex.sourceforge.net/),
[bison 2.3](http://www.gnu.org/software/bison/),
[gperf 2.7.2](http://www.gnu.org/software/gperf/),
[gawk 3.1.1](http://www.gnu.org/software/gawk/),
[m4 1.4.1](http://www.gnu.org/software/m4/),
[make 3.79.1](http://www.gnu.org/software/make/) and
[OpenSSL 0.9.7](http://www.openssl.org/)

**Debian/Ubuntu**: 
`sudo apt-get install autoconf automake libtool flex bison gperf gawk m4 make openssl libssl-dev`

Having these tools, compiling and installing Virtuoso is just a matter of configure/make/make install.

You can skip section "Install Virtuoso" and go directly to **"Configuring Virtuoso"**!

## Install Virtuoso

**Only read further if you dont read section "Compiling Virtuoso"!** There is a good installation manual on Virtuoso's page: http://virtuoso.openlinksw.com/dataspace/dav/wiki/Main/VOSUbuntuNotes

## Configuring Virtuoso

In some cases you have to manually start the Virtuoso server.

In **Ubuntu** execute (Maybe you have to replace the 6.1 with the current version)
`sudo service virtuoso-opensource-6.1 start`

Virtuoso  keeps all the files for a database in a folder along with a configuration file. An example configuration file which we will use as a base for our configuration is provided with the default database. To create a Virtuoso database for OntoWiki perform the following steps:

* Create a folder named "ontowiki" under `<prefix>/var/lib/virtuoso/`.
* Copy the file `<prefix>/var/lib/virtuoso/db/virtuoso.ini` to `<prefix>/var/lib/virtuoso/ontowiki/virtuoso.ini`
* Open `<prefix>/var/lib/virtuoso/ontowiki/virtuoso.ini` in a text editor
* Find the option "DirsAllowed", it is a comma-separated list of dirs from which Virtuoso is allowed to open files. Add your PHP's temp directory (usually `/tmp`) and your OntoWiki directory under your webroot.

## Setting up ODBC
Database connection to Virtuoso happens through ODBC. ODBC is configured by two files, `odbc.ini` and `odbcinst.ini`.
On Linux systems they can be found under `/etc`, on Mac OS X systems under `/Library/ODBC`.
In case they don't exist, create them.

Add the following lines to the odbcinst.ini file:

    [virtuoso-odbc]
    Driver = <prefix>/lib/virtodbc.so

Add the following lines to the odbc.ini file:

    [ODBC Data Sources]
    VOS = Virtuoso
    
    [VOS]
    Driver = virtuoso-odbc
    Description = Virtuoso Open-Source Edition
    Address = localhost:1111

Now make sure, PHP can connect to Virtuoso via ODBC.
On some Linux systems you may have to install the ODBC package for PHP (`php5-odbc`).
To test the connection, create a file called `odbctest.php` in you webroot with the following PHP code in it:

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
* Optional 3: For the [Linked Data](http://linkeddata.org/) plug-in to work, copy the `htaccess-dist` file to `.htaccess` make sure your Apache's `mod_rewrite` module is installed and `AllowOverwrite` is set to `All` for your OntoWiki directory in your `httpd.conf`.

### FAQ
* SQL Error:
[unixODBC][OpenLink][Virtuoso iODBC Driver][Virtuoso Server]FA011: Access to /var/www/ontowiki/libraries/Erfurt/include/SysOntLocal.rdf is denied due to access control in ini file (37000)
**Solution:** do Configuring Virtuoso Step 4
* Uncaught exception
    'Zend_Cache_Exception' with message 'Cannot use SQLite storage because the 'sqlite' extension is not loaded in the current PHP
**Solution:** go to ibraries/Erfurt/config/config.ini and set cache.enable = 0

### Platform-specific Notes
#### GNU/Linux
To start Virtuoso, switch to `<prefix>/bin` and run:
    ./virtuoso-t -f -c /opt/virtuoso/var/lib/virtuoso/ontowiki/virtuoso.ini

(Virtuoso runs in foreground using the created OntoWiki specific configuration file.)

Cave: Run Virtuoso with enough rights. When importing knowledge bases from file, they are first copied to tmp. Virtuoso needs a sufficiently high user like root or www-data to read it (besides adding the tmp dir to DirsAllowed). 
Otherwise you will get the error:

    Error importing knowledge base: Graph '<http://inserttesst.org>' could not be imported: Error importing statements: SQL Error: [unixODBC][OpenLink][Virtuoso iODBC Driver][Virtuoso Server]FA012: Can't open file '/tmp/phpWH20k0', error (13) : Permission denied (37000) CALL DB.DBA.RDF_LOAD_RDFXML(FILE_TO_STRING_OUTPUT('/tmp/phpWH20k0'), '', 'http://inserttesst.org'

##### Debian/Ubuntu
If you install Virtuoso from the .deb-Package you have to change in '/etc/init.d/virtuoso-opensource' the line
    DBBASE=/var/lib/virtuoso/db
to
    DBBASE=/var/lib/virtuoso/ontowiki
while virtuoso is not running.

Also, make sure your Virtuoso is at least [[version 6.1.4|Deployment-Recommendations]].

#### Mac OS X
To auto-start Virtuoso on Mac OS X 10.5 use a config file for the `launchd` service. It should be placed under `/Library/LaunchDaemons`. The following is an example file, replace the paths with your settings where necessary.

    $ cat ~/Library/LaunchDaemons/com.openlinksw.virtuoso.plist 
    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>UserName</key>
        <string>root</string>
        <key>GroupName</key>
        <string>wheel</string>
        <key>RunAtLoad</key>
        <true/>
        <key>Label</key>
        <string>com.openlinksw.virtuoso</string>
        <key>OnDemand</key>
        <false/>
        <key>ProgramArguments</key>
        <array>
            <string>/usr/local/bin/virtuoso-t</string>
            <string>-f</string>
            <string>-c</string>
            <string>/usr/local/var/lib/virtuoso/ontowiki/virtuoso.ini</string>
        </array>
    </dict>
    </plist>

#### Windows
Follow [these instructions](http://virtuoso.openlinksw.com/dataspace/dav/wiki/Main/VOSUsageWindows) in order to set up Virtuoso as an ODBC data source on Windows.

### Known Problems
#### Debian/Ubuntu
If you want to install virtuoso from the .deb and have installed virtuoso before (for instance on an update) it hast to run and has to be configured correctly during the installation, because the pre/pos-removal script tries to start/stop virtuoso.