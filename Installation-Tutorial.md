## System Requirements

### Hardware
unknown? (please edit how much cpu, ram and free harddrive space needed at minimum)

#### Software

- Also, have a look at [[the 'Getting Started'|Getting-Started-Users]] document.

- Windows, Mac OS or Linux 
- [Apache HTTP Server](http://www.apache.org/)
- either [Virtuoso](http://download.openlinksw.com/virtwiz/virtuoso.php) or [MySQL](http://www.mysql.com/downloads/)

## Installation

1. Download [the newest version of OntoWiki from github](https://github.com/AKSW/OntoWiki/downloads).
    _If you are unsure about the archive format, click "Download as zip" if you use Windows or Mac OS and "Download as tar.gz" if you use Linux._
2. Unpack the OntoWiki 

### Arch Linux

1. Apache, PHP and ODBC
    - Install Apache and PHP with the package manager

            $ sudo pacman -S apache php apache-php php-odbc
    - Configure PHP by following the PHP section of the [LAMP entry in the Archlinux Wiki](https://wiki.archlinux.org/index.php/LAMP#PHP) (also consult that page if you have any problems installing Apache and PHP)
    - Compile the libraries

            AKSW-OntoWiki-062a14e$ sudo make deploy
    - Activate the iconv and ODBC extensions in `/etc/php/php.ini`

        Uncomment the following lines:

            extension=iconv.so
            extension=odbc.so
    - Install ODBC

            $ sudo pacman -S php-odbc

        Add the following lines to the file `/etc/odbcinst.ini`: (create it if it doesn't exist, see [VirtuosoBackend](VirtuosoBackend))

            [virtuoso-odbc]
            Driver = /usr/lib/virtodbc.so

        Add the following lines to the file `/etc/odbc.ini`: (create it if it doesn't exist)

            [ODBC Data Sources]
            VOS = Virtuoso
    
            [VOS]
            Driver = virtuoso-odbc
            Description = Virtuoso Open-Source Edition
            Address = localhost:1111
    - (Re-)start Apache

            $ sudo /etc/rc.d/httpd restart
2. Virtuoso
    - Please note that Virtuoso-opensource should be at least in [version 6.4](https://github.com/AKSW/OntoWiki/wiki/Deployment-Recommendations)
    - Install Virtuoso with the package manager

            $ sudo pacman -S virtuoso
    - Create the Virtuoso OntoWiki directory and add the virtuoso.ini to it (see [https://github.com/AKSW/OntoWiki/wiki/VirtuosoBackend](Virtuoso Backend))

            $ sudo mkdir /var/lib/virtuoso/ontowiki
            $ sudo cp /var/lib/virtuoso/db/virtuoso.ini /var/lib/virtuoso/ontowiki
    - Add the temporary and OntoWiki directories to the _DirsAllowed_ entry in `/var/lib/virtuoso/ontowiki/virtuoso.ini`

            DirsAllowed  = ., /usr/share/virtuoso/vad,/tmp,/srv/http/AKSW-OntoWiki-062a14e
    - Start Virtuoso (add the option _+foreground_ if you want to check if it starts correctly)

            $ sudo virtuoso-t -f -c /var/lib/virtuoso/ontowiki/virtuoso.ini

3. [Download OntoWiki](https://github.com/AKSW/OntoWiki/downloads) (choose "Download as tar.gz")
4. Unpack OntoWiki into your document root (the end of the file name may differ)

        $ sudo tar -xzf download/AKSW-OntoWiki-v0.9.6-21-367-g062a14e.tar.gz --directory /srv/http/

6. Open http://localhost
The OntoWiki should now be shown after selection of the folder `AKSW-OntoWiki-#somenumber`

### Windows

1. Apache

    1. Download Apache 2

        Go to `http://httpd.apache.org/download.cgi` and choose the latest stable release version that provides Windows binaries. Download the MSI Installer for this version. The line should look like _"Win32 Binary including OpenSSL 0.9.8t (MSI Installer): httpd-2.2.22-win32-x86-openssl-0.9.8t.msi"_.
    2. Run the Apache Installer

        When you arrive at the "Server Information" dialog box, enter "localhost" (without the quotes) for the Network Domain as well as for the Server Name and whatever email address you wish for the "Administrator's Email Address" field. The installer uses the information you enter to create a default Apache configuration file for you. You can always go back and manually change these values in your configuration file if you change your mind later. Leave the default setting of "for All Users, on Port 80, as a Service" as it is. Click "Next" when you're done (see [How to Install and Configure Apache 2 on Windows](http://www.thesitewizard.com/apache/install-apache-2-windows.shtml)).
Go to `http://localhost/` and confirm that it shows "It works!".
2. PHP
    - Stop the Apache service
        - Type `services.msc` into the search field in your start menu and click on "services"
        - Rightclick on "Apache2._X_" and click on "Stop"          
    - Go to <http://sourceforge.net/projects/phpinstallermsi/files/latest/download> and execute the MSI file that will automatically be downloaded.
    - Choose the default options presented by the wizard.
    - When prompted "Select a Web Server Setup" choose "Other CGI"
    - Add the following lines to the file `C:\Program Files\PHP\conf\httpd.conf`: (you may need to change the owner of that file to the current user in order to modify it) (see <http://windows.fyicenter.com/73_Apache_PHP_Getting_HTTP_403_Forbidden_Error_on_PHP_Scripts.html>)

            ScriptAlias /php/  "C:/Program Files/PHP/"
            AddHandler x-httpd-php .php
            Action x-httpd-php "/php/php-cgi.exe"
    
            <Directory "C:/Program Files/PHP/">
                AllowOverride None
                Options None
                Order allow,deny
                Allow from all
            </Directory>
    - Set the recommended https://github.com/AKSW/OntoWiki/wiki/php.ini-recommendations
    - Start the Apache service again
        - Type `services.msc` into the search field in your start menu and click on "services".
        - Rightclick on "Apache2._X_" and click on "Start".
    - Confirm that PHP works and is successfully integrated in Apache.
        - create the file `C:\Program Files\Apache Software Foundation\Apache2.2\htdocs\test.php` and set its content to `<?php phpinfo(); ?>`
        - Go to `http://localhost/test.php` and confirm that it shows a big table of PHP settings.

### As a Virtual Machine

...