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

1. Install Apache

        $ sudo pacman -S apache

2. Install Virtuoso

        $ sudo pacman -S virtuoso
3. [Download OntoWiki](https://github.com/AKSW/OntoWiki/downloads) (choose "Download as tar.gz")
4. Unpack OntoWiki into your document root (the end of the file name may differ)

        $ sudo tar -xzf download/AKSW-OntoWiki-v0.9.6-21-367-g062a14e.tar.gz --directory /srv/http/
5. (Re-)start Apache
`$ sudo /etc/rc.d/httpd restart`
6. Open localhost

`download$ tar -xzf dpkg.tar.gz
