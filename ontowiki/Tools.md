---
title: Tools
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /Tools.html
editme_path: ontowiki/Tools.md
---
We made some developer tools like cwm and owcli that help you during work with semantic data.

## Install & Config

First, all statements and commands are tested on a Ubuntu, so please use the equivalent for your system.

### CWM

There are 2 ways for install it. First, you can use the following command:

```
sudo apt-get install swap-cwm
```

Otherwise, go to [http://www.w3.org/2000/10/swap/doc/cwm.html#dev](http://www.w3.org/2000/10/swap/doc/cwm.html#dev) and download it over CVS. (I save it in /home/Foo/opt )

\_After minutes of waiting ...\_

```
cd /home/Foo/opt/2000/10/swap
```

In the swap folder you find many files, one of them named "README".

```
{$INSERT YOUR FAVOURIT EDITOR$} README
```

Read it, it describes the installation.

### OWCLI

The OntoWiki CommandLineInterface is featured on its own wiki page ...

After installation, you should be able to use the "owcli" command over the console.

## Use it, luke!

Now you should be able to use the "cwm" and "owcli" in the console. \*Did you know other tools and scenarios for using it, please add it or write a comment!\*

### Scenario 1

You write n3-code and you will import it into Ontowiki. For example your n3-File named \*FOOBAR.n3\*. Switch into his folder.

```
cd /path/to/FOOBAR.n3
```

With the following makefile you are be able to automate it.

```
default:
	@echo "If you wanna install these models via owcli, type 'make install'"

install:
	cwm FOOBAR.n3 --rdf >FooBar.rdf
	owcli -m http://ns.foo.bar/FooBar/ -e model:drop model:create model:add -i FooBar.rdf

uninstall:
	owcli -m http://ns.foo.bar/FooBar/ -e model:drop
```

For using it, create a new file named \*Makefile\* and save the code above.

Execute in the console:

```
make install
```

Now go into your OntoWiki. Left you should see the new model \*FooBar\*. As you can see in the makefile, you need cwm and owcli. CWM transform a file into another, e.g. n3 to rdf. Over OWCLI you execute commands.

## Known problems

- Dont use blank spaces or special characters as a folder name like ö, ä or ü in german. For example Python doesn't likes it.

- If you getting errors like the following check your root-access. With phpMyAdmin open "Privileges" and set for \*root@localhost\* the same password as you set in /.owcli and ontowiki config.ini!
```
JSONRPC Error -32000: Model <http://ns.foo.bar/> is not available and therefore not removable.
JSONRPC Error -32000: Failed creating the model. Action not allowed!
```

- If you getting errors like the following, check that you have a working \*.htaccess\* and \*mod\_rewrite\* activated:
```
The command "listModels" has no valid Service Mapping Description from the server.
Something went wrong, response was not json encoded (turn debug on to see more)
```

- If you getting errors like the following, check that you have the \*php5-cli\* package installed:
```
/usr/bin/env: php5: No such file or directory
```

- If you getting errors like the following, check that you have the \*php-pear\* package installed:
```
owcli -m [...] -e model:drop model:create model:add -i namespace.rdf examples.rdf
make: *** [install] Fehler 255
```
