## System Requirements

### Hardware
unknown? (please edit how much cpu, ram and free harddrive space needed at minimum)

#### Software

- Windows, Mac OS or Linux 
- [Apache HTTP Server](http://www.apache.org/)
- either [Virtuoso](http://download.openlinksw.com/virtwiz/virtuoso.php) or [MySQL](http://www.mysql.com/downloads/)

## Installation

1. Download [the newest version of OntoWiki from github](https://github.com/AKSW/OntoWiki/downloads)

_If you are unsure about the archive format, click "Download as zip" if you use Windows or Mac OS and "Download as tar.gz" if you use Linux._
2. Unpack the OntoWiki 

### Arch Linux

1. Apache and PHP
    - Install Apache and PHP with the package manager

            $ sudo pacman -S apache php apache-php
    - Configure PHP by following the PHP section of the [LAMP entry in the Archlinux Wiki](https://wiki.archlinux.org/index.php/LAMP#PHP) (also consult that page if you have any problems installing Apache and PHP)
    - Compile the libraries

            AKSW-OntoWiki-062a14e$ sudo make deploy
    - (Re-)start Apache

            $ sudo /etc/rc.d/httpd restart
2. Virtuoso
    - Install Virtuoso with the package manager

            $ sudo pacman -S virtuoso
    - Create the virtuoso ontowiki directory and add the virtuoso.ini to it (see [https://github.com/AKSW/OntoWiki/wiki/VirtuosoBackend](Virtuoso Backend))

            $ sudo mkdir /var/lib/virtuoso/ontowiki
            $ sudo cp /var/lib/virtuoso/db/virtuoso.ini /var/lib/virtuoso/ontowiki
    - Add the temporary and OntoWiki directories to the _DirsAllowed_ entry in `/var/lib/virtuoso/ontowiki/virtuoso.ini`

            DirsAllowed  = ., /usr/share/virtuoso/vad,/tmp,/srv/http/AKSW-OntoWiki-062a14e
    - Start Virtuoso (add the option _+foreground_ if you want to check if it starts correctly)

            $ sudo virtuoso-t -f -c /var/lib/virtuoso/db/virtuoso.ini

3. [Download OntoWiki](https://github.com/AKSW/OntoWiki/downloads) (choose "Download as tar.gz")
4. Unpack OntoWiki into your document root (the end of the file name may differ)

        $ sudo tar -xzf download/AKSW-OntoWiki-v0.9.6-21-367-g062a14e.tar.gz --directory /srv/http/

6. Open localhost

`download$ tar -xzf dpkg.tar.gz
