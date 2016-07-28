---
title: PHPCodeSniffer
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_PHPCodeSniffer/
editme_path: ontowiki/PHPCodeSniffer.md
---
This section describes the use of the PHPCodeSniffer to check if your coding style complies to the Ontowiki/Erfurt Coding standard.

## Installation

Go to your Ontowiki/Erfurt directory and run (composer installs it automatically):

`make install`


This will install the latest version of the CodeSniffer.

### Summary View
(Depending on the codesniffer configfile `phpcs.xml` either summary or Detail view is the standard view for `make codesniffer`, if you want to change the standard you need to configure the configfile and add or delete the line
`<arg name="report" value="summary"/>`)
If you run `make codesniffer` or `vendor/bin/phpcs -s --report=summary [special flags] [path to files]` and your code not match the coding standard you will get something like that:

    E.E.EE


    PHP CODE SNIFFER REPORT SUMMARY
    --------------------------------------------------------------------------------
    FILE                                                            ERRORS  WARNINGS
    --------------------------------------------------------------------------------
    /home/lars/Uni/BA/OW_default/TestClass.php                      6       0
    /home/lars/Uni/BA/OW_default/TestClass3.php                     6       0
    /home/lars/Uni/BA/OW_default/TestClass5.php                     6       0
    /home/lars/Uni/BA/OW_default/TestClass6.php                     6       0
    --------------------------------------------------------------------------------
    A TOTAL OF 24 ERROR(S) AND 0 WARNING(S) WERE FOUND IN 4 FILE(S)
    --------------------------------------------------------------------------------

    Time: 0 seconds, Memory: 2.50Mb

    make: *** [cs-check-commit] errors 1

This is a summary of all files, that have been checked. You can see how many files were checked and how many errors or warnings every file have caused.

<a id="detailview"></a>
### Detail View
(Depending on the codesniffer configfile `phpcs.xml` either summary or Detail view is the standard view for `make codesniffer`, if you want to change the standard you need to configure the configfile and add or delete the line
`<arg name="report" value="summary"/>`)
To correct your code you need a more detailed view, so you can rn either
`make codesniffer` or `vendor/bin/phpcs [special flags] [path to files]`
If you have problems understanding the errors for a single file you might only test the single file and add as flag [-v,-vv,-vvv] to get extra output.

and get something like that for every file that have been checked:

    FILE: /home/lars/Uni/BA/OW_default/TestClass.php
    --------------------------------------------------------------------------------
    FOUND 6 ERROR(S) AFFECTING 5 LINE(S)
    --------------------------------------------------------------------------------
      6 | ERROR | Protected member variable "test" must contain a leading
        |       | underscore
      9 | ERROR | Variable "test_variable" is not in valid camel caps format
     11 | ERROR | Variable "Test" is not in valid camel caps format
     13 | ERROR | Opening brace should be on a new line
     14 | ERROR | No space found after comma in function call
     14 | ERROR | Space before opening parenthesis of function call prohibited
    --------------------------------------------------------------------------------

Now you can see the description of the errors and the line where they occur.
So you have the possibility to correct your code and check it again.

**Note:** If there are less than six files to check, you get the detail view automatically and not the summary view.

<a id="ideintegration"></a>
## IDE Integration
If you want a easier way to correct your coding standard violations, you can integrate the Code Sniffer Check in your IDE. 

* For VIM  
You find a solution on this 
[Site](http://joncairns.com/2012/03/vim-with-php-code-sniffer-mess-detector-and-code-coverage/)
or on this
[Site](http://www.koch.ro/blog/index.php?/archives/62-Integrate-PHP-CodeSniffer-in-VIM.html).
 
If you have a better solution, feel free to write it here or if you need another Makefile command open a new issue
and assign it to me (larseidam)

* For Komodo Edit  
Make a new command in your Toolbox and give it a name. After that, add the makefile command 
to the command field and to the 'Start in' field
write the full path to or ontowiki project. Now make a hook at the 'Parse with output'
Field an write this  
`^(?P<file>.*):(?P<line>\d+):(?P<column>\d+):(?P<content>.*)`  
in the textfield. In the final step make a hook at the 'Show output as a list' field.
Push 'OK' and check the new created command.

**Note:** You must have some Code in the root of the git-repository, otherwise the CodeSniffer have no files to check and you can't to see, if it runs or not.

<a id="tips"></a>
## Tips
For **git**:

The CodeSniffer checks all files or fileparts that have been added to the index (with **git add**). If you fix some issues that were reported, you have to re-add these changes, otherwise CS will complain again and again.
