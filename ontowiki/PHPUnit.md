---
title: PHPUnit
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_PHPUnit/
---
OntoWiki using PHPUnit.

# Ready ...

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

# .. steady, ...

Now start neccassary services

- Apache2
```
sudo service apache2 start
```

- MySQL
```
sudo service mysql start
```

Now put a copy of OntoWiki into \*/var/www/myow\*! ( [InstallFromGit](InstallFromGit) )

Currently the testability of OntoWiki is getting refactored so change your current branch

```
cd /var/www/myow && hg update OntoWiki-RefactoringTestability
```

If you type

```
hg branch
```

you should be get

```
hg branch 
OntoWiki-RefactoringTestability
```

Be sure that your **Zend** version is >= **1.9.5**. If you dont know the version execute

```
cd /var/www/myow && make zend
```

# ... \*\*Go!\*\*

### Tests folder content

Please use your terminal for navigating and doing things because of PHPUnit has no GUI and is usable only via terminal. Get folder content

```
cd /var/www/myow/application/tests && ls
```

You should get something like:

    controllers DropErrorMails.php OntoWiki Selenium test\_base.php TestSuite.php

Now take a test

```
phpunit TestSuite
```

You should get something like:

```
PHPUnit 3.4.5 by Sebastian Bergmann.

.........

Time: 2 seconds, Memory: 16.25Mb
OK (9 tests, 27 assertions)
```

Driven OntoWiki developers write every time tests for their new fancy stuff so this output can be changed in the future! But there should be \_no\_ erros by PHPUnit.

For a **easierer way** to execute PHPUnit go back to OntoWiki root folder

```
cd /var/www/myow
```

and execute

```
make test
```

It executes \_phpunit TestSuite\_ too.

# Curiosities

### Percent symbol

If phpunit stop testing and breaks with an % like

```
PHPUnit 3.4.5 by Sebastian Bergmann.
..........%
```

in your tested code contains an **exit** call, which is reached (and the % indicates that your terminal complains about a missing newline). Use **return;** instead!

### Strange PHPUnit installation

I had problems with PHP telling me:

```
PHP Fatal error: Call to undefined function php_codecoverage_autoload() in /usr/share/php/PHPUnit/Util/GlobalState.php on line 380
```

Which I could solve by un-installing phpunit and its related packages (using apt-get purge …) and installing phpunit with pear ( [http://pear.phpunit.de/](http://pear.phpunit.de/)).

This problem occurred on debian testing in my case.

