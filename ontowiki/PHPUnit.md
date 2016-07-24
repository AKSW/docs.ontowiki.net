---
title: PHPUnit
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_PHPUnit/
---
OntoWiki using PHPUnit.

## Ready ...

**Do not** use a XAMPP environment for testing. There a few things which makes problems. So use **native** OS packages for Apache2, MySQL, PHP5 etc. Execute the following commands over your terminal.

For **Ubuntu** 10.04 (Lucid Lynx):

- **Apache2**
```
sudo apt-get install apache2
```

For OntoWiki we need **mod\_rewrite**

```
sudo a2enmod rewrite
```

Give you full write access to webfolder

```
sudo chmod 777 /var/www
```

- **MySQL** If you would use Virtuoso or whatever ignore this part. 
```
sudo apt-get install mysql-server
```

for more information how to set up and configure a MySQL server please take a look at [http://wiki.ubuntuusers.de/MySQL](http://wiki.ubuntuusers.de/MySQL)

- **PHPMyAdmin** Not neccessary but useful for administrate your MySQL databases. If you would use Virtuoso or whatever ignore this part.
```
sudo apt-get install phpmyadmin
```

- **PHP5** , **PHPUnit** , PEAR
```
sudo apt-get install php5 php5-cli php-pear php5-curl php5-mysql php5-odbc phpunit
```

## .. steady, ...

Now start neccassary services

- Apache2
```
sudo service apache2 start
```

- MySQL
```
sudo service mysql start
```

Now put a copy of OntoWiki into ``*/var/www/myow*``! 

afterwards navigate into the directory

```
cd /var/www/myow
```

You will autmatically install PHPUnit per `make install`

## ... \*\*Go!\*\*

### Tests folder content

Please use your terminal for navigating and doing things because of PHPUnit has no GUI and is usable only via terminal. Get folder content

```
cd /var/www/myow
```

Now you can either use

`` make test`` or ``make test-[unit | extension | integration-virtuoso | integration-mysql]``

You should get something like:

```
PHPUnit 3.4.5 by Sebastian Bergmann.

.........

Time: 2 seconds, Memory: 16.25Mb
OK (9 tests, 27 assertions)
```

if you want to only execute certain tests you can find the binary in `*/OntoWiki/vendor/bin/phpunit` , if you don't have the vendor folder you need to run 
`make install` or `php composer.phar install`. How to run only certain tests (and write them) can be read in the phpunit [Documentation](https://phpunit.de/documentation.html)

Driven OntoWiki developers write every time tests for their new fancy stuff so this output can be changed in the future! But there should be \_no\_ errors by PHPUnit.


## Curiosities

### Percent symbol

If phpunit stop testing and breaks with an % like

```
PHPUnit 3.4.5 by Sebastian Bergmann.
..........%
```

in your tested code contains an **exit** call, which is reached (and the % indicates that your terminal complains about a missing newline). Use **return;** instead!
