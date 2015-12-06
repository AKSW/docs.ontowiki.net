## Ubuntu Quick Install Guide

installing everything you need:

    sudo apt-get install git apache2 php5 php5-odbc
    cd /var/www/html
    sudo git clone https://github.com/AKSW/OntoWiki.git

Setting up ODBC:

You need to add things in 2 files: `odbc.ini` and `odbcinst.ini`.

On Linux systems they can be found under `/etc`

(standard path for **virtodbc.so** is **/usr/lib/odbc/**)

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

test it with:

    make odbctest

now you need to copy the **/var/www/html/OntoWiki/config.ini.dist** to **/var/www/html/OntoWiki/config.ini**
if you have changed username/password you need to change them in this file. all important lines for Virtuoso are:

    store.backend = virtuoso
    store.virtuoso.dsn = VOS
    store.virtuoso.username = dba
    store.virtuoso.password = dba

the last thing is to start virtuoso and restart apache

    sudo service virtuoso-opensource-6.1 start
    sudo service apache2 start/restart
