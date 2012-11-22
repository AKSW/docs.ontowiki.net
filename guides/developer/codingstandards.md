---
layout: page
title: Codingstandards
---

# Codingstandards

This document provides guidelines for code formatting and documentation to individuals and teams contributing to OntoWiki.

This page makes heavy use of the [Zend Framework coding standards](http://framework.zend.com/manual/en/coding-standard.html).

## Goals
Coding standards are important in any development project, but they are particularly important when many developers are working on the same project. Coding standards help ensure that the code is high quality, has fewer bugs, and can be easily maintained.

## PHP File Formatting
### General
For files that contain only PHP code, the closing tag ("`?>`") is never permitted. It is not required by PHP, and omitting it prevents the accidental injection of trailing white space into the response.

### Indentation
Indentation should consist of 4 spaces. Tabs are not allowed. Search them with:
    grep -P '\t' *

For all Vim users, use this modeline if you don't want to set it for your whole system.
    // vim: sw=4:sts=4:expandtab

### Maximum Line Length
The target line length is 80 characters. That is to say, OntoWiki developers should strive keep each line of their code under 80 characters where possible and practical. However, longer lines are acceptable in some circumstances. The maximum length of any line of PHP code is 120 characters.

### Naming Conventions

#### Classes
OntoWiki API standardizes on a class naming convention whereby the names of the classes directly map to the directories in which they are stored. The root level directory of the OntoWiki API classes "OntoWiki/" directory located under "application/classes/". All OntoWiki classes are stored hierarchically under these root directories.

Class names may only contain alphanumeric characters. Numbers are permitted in class names but are discouraged in most cases. Underscores are only permitted in place of the path separator; the filename "OntoWiki/Controller/Base.php" must map to the class name "OntoWiki_Controller_Base".

If a class name is comprised of more than one word, the first letter of each new word must be capitalized. Successive capitalized letters are not allowed, e.g. a class "OntoWiki_URL" is not allowed while "OntoWiki_Url" is acceptable.

These conventions define a pseudo-namespace mechanism for OntoWiki. OntoWiki will adopt the PHP namespace feature when it becomes available.

#### Filenames
For all other files, only alphanumeric characters, underscores, and the dash character ("-") are permitted. Spaces are strictly prohibited.

Any file that contains PHP code should end with the extension ".php", with the notable exception of view scripts. The following examples show acceptable filenames for OntoWiki classes:
    OntoWiki/Application.php
    OntoWiki/Controller/Base.php
    OntoWiki/Controller/Exception.php

#### Function and Method Naming
Function names may only contain alphanumeric characters. Underscores are not permitted. Numbers are permitted in function names but are discouraged in most cases.

Function names must always start with a lowercase letter. When a function name consists of more than one word, the first letter of each new word must be capitalized. This is commonly called "camelCase" formatting.

Verbosity is generally encouraged. Function names should be as verbose as is practical to fully describe their purpose and behavior.

These are examples of acceptable names for functions:
    appendMessage()
    setEntry()
    getControllerClass()
File names must map to class names as described above.

#### Variables
Variable names may only contain alphanumeric characters. Underscores are not permitted. Numbers are permitted in variable names but are discouraged in most cases.

For instance variables that are declared with the `private` or `protected` modifier, the first character of the variable name must be a single underscore. This is the only acceptable application of an underscore in a variable name. Member variables declared `public` should never start with an underscore.

As with function names (see above) variable names must always start with a lowercase letter and follow the "camelCaps" capitalization convention.

Verbosity is generally encouraged. Variables should always be as verbose as practical to describe the data that the developer intends to store in them. Terse variable names such as "$i" and "$n" are discouraged for all but the smallest loop contexts. If a loop contains more than 20 lines of code, the index variables should have more descriptive names.

#### Constants
Constants may contain both alphanumeric characters and underscores. Numbers are permitted in constant names.
All letters used in a constant name must be capitalized, while all words in a constant name must be separated by underscore characters.

For example, EMBED_SUPPRESS_EMBED_EXCEPTION is permitted but EMBED_SUPPRESSEMBEDEXCEPTION is not.
Constants must be defined as class members with the "const" modifier. Defining constants in the global scope with the "define" function is permitted but strongly discouraged.

#### Components
Components provide a controller that is named like the component (first letter uppercase) immediately followed by  the word "Controller". For more information on developing components, see the [[Extensions]].

#### Modules
Modules provide a class that is named like the module with the first letter in upper case immediately followed by the word "Module". For more information on developing components, see the [[Extensions]].

#### Plug-ins
A plug-in class is called like the plug-in (again the first letter must be upper case) immediately followed by the word "Plugin". For more information on developing components, see the [[Extensions]].

## Coding Style
### Strings
#### String Literals
When a string is literal (contains no variable substitutions), the apostrophe or "single quote" should always be used to demarcate the string:
    $a = 'Example String';

#### String Literals Containing Apostrophes
When a literal string itself contains apostrophes, it is permitted to demarcate the string with quotation marks or "double quotes". This is especially useful for Messages:
    OntoWiki_Application::getInstance()->appendMessage(new OntoWiki_Message(
        "The graph with the URI '$graphUri' could not be loaded.", 
        OntoWiki_Message::WARNING
    ));
This syntax is preferred over escaping apostrophes as it is much easier to read.

#### String Concatenation
When concatenating strings with the "." operator, it is encouraged to break the statement into multiple lines to improve readability. In these cases, each successive line should be padded with white space such that the "."; operator is aligned under the "=" operator:
    $this->view->moduleUrl = $this->_config->staticUrlBase 
                           . $this->_config->extensions->modules
                           . $this->_name . '/';

### Associative Arrays
When declaring associative arrays with the array construct, breaking the statement into multiple lines is encouraged. In this case, each successive line must be padded with white space such that both the keys and the values are aligned:
    $sampleArray = array('firstKey'  => 'firstValue',
                         'secondKey' => 'secondValue');

### Null Values
In order to keep the code consistent, `null` values are written in lower case:

    if (null === $someVar) {
        doSomething();
    }

### Classes
#### Class Declarations
Classes must be named according to OntoWiki's naming conventions.

The brace should always be written on the line underneath the class name with no indentation.

Every class must have a documentation block that conforms to the PHPDocumentor standard.

All code in a class must be indented with four spaces.

Only one class is permitted in each PHP file.

Placing additional code in class files is permitted but discouraged. In such files, two blank lines must separate the class from any additional PHP code in the class file.

The following is an example of an acceptable class declaration:
    /**
     * Documentation Block Here
     */
    class SampleClass
    {
        // all contents of class
        // must be indented four spaces
    }
#### Class Member Variables
Member variables must be named according to OntoWiki's variable naming conventions.

Any variables declared in a class must be listed at the top of the class, above the declaration of any methods.

The var construct is not permitted. Member variables always declare their visibility by using one of the `private`, `protected`, or `public` modifiers. Giving access to member variables directly by declaring them as `public` is permitted but discouraged in favor of accessor methods (set/get).

### Functions and Methods
#### Function and Method Declaration
Functions must be named according to the OntoWiki function naming conventions.

Methods inside classes must always declare their visibility by using one of the `private`, `protected`, or `public` modifiers.

As with classes, the brace should always be written on the line underneath the function name. Space between the function name and the opening parenthesis for the arguments is not permitted. 

Functions in the global scope are strongly discouraged.

The following is an example of an acceptable function declaration in a class:
    /**
     * Documentation Block Here
     */
    class Foo
    {
        /**
         * Documentation Block Here
         */
        public function bar()
        {
            // all contents of function
            // must be indented four spaces
        }
    }

NOTE: Pass-by-reference is the only parameter passing mechanism permitted in a method declaration.
    /**
     * Documentation Block Here
     */
    class Foo
    {
        /**
         * Documentation Block Here
         */
        public function bar(&$baz)
        {}
    }
    
Call-time pass-by-reference is strictly prohibited.

The return value must not be enclosed in parentheses. This can hinder readability, in additional to breaking code if a method is later changed to return by reference.
    /**
     * Documentation Block Here
     */
    class Foo
    {
        /**
         * WRONG
         */
        public function bar()
        {
            return($this->bar);
        }
    
        /**
         * RIGHT
         */
        public function bar()
        {
            return $this->bar;
        }
    }

#### Function and Method Usage
Function arguments should be separated by a single trailing space after the comma delimiter. The following is an example of an acceptable invocation of a function that takes three arguments:
    threeArguments(1, 2, 3);

Call-time pass-by-reference is strictly prohibited. See the function declarations section for the proper way to pass function arguments by-reference.

In passing arrays as arguments to a function, the function call may include the "array" hint and may be split into multiple lines to improve readability. In such cases, the normal guidelines for writing arrays still apply:
    threeArguments(array(1, 2, 3), 2, 3);
    
    threeArguments(array(1, 2, 3, 'Zend', 'Studio',
                         $a, $b, $c,
                         56.44, $d, 500), 2, 3);
    
### Control Statements
#### If/Else/Elseif
Control statements based on the if and elseif constructs must have a single space before the opening parenthesis of the conditional and a single space after the closing parenthesis.

Within the conditional statements between the parentheses, operators must be separated by spaces for readability. Inner parentheses are encouraged to improve logical grouping for larger conditional expressions.

The opening brace is written on the same line as the conditional statement. The closing brace is always written on its own line. Any content within the braces must be indented using four spaces.
    if ($a != 2) {
        $a = 2;
    }

For "if" statements that include "elseif" or "else", the formatting conventions are similar to the "if" construct. The following examples demonstrate proper formatting for "if" statements with "else" and/or "elseif" constructs:
    if ($a != 2) {
        $a = 2;
    } else {
       $a = 7;
    }
    
    if ($a != 2) {
        $a = 2;
    } else if ($a == 3) {
       $a = 4;
    } else {
       $a = 7;
    }
PHP allows statements to be written without braces in some circumstances. This coding standard makes no differentiation- all "if", "elseif" or "else" statements must use braces.

Use of the "elseif" construct is permitted but strongly discouraged in favor of the "else if" combination.

#### Switch
Control statements written with the "switch" statement must have a single space before the opening parenthesis of the conditional statement and after the closing parenthesis.

All content within the "switch" statement must be indented using four spaces. Content under each "case" statement must be indented using an additional four spaces.
    switch ($numPeople) {
        case 1:
            break;
    
        case 2:
            /* fallthrough */
    
        default:
            break;
    }

The construct default should never be omitted from a switch statement.

NOTE: It is sometimes useful to write a case statement which falls through to the next case by not including a break or return within that case. To distinguish these cases from bugs, any case statement where break or return are omitted should contain a comment indicating that the break was intentionally omitted.

### Inline Documentation
#### Documentation Format
All documentation blocks ("docblocks") must be compatible with the phpDocumentor format. Describing the phpDocumentor format is beyond the scope of this document. For more information, visit: [[http://phpdoc.org/]]

All class files must contain a "file-level" docblock at the top of each file and a "class-level" docblock immediately above each class. Examples of such docblocks can be found below.

All class files must contain a "file-level" docblock at the top of each file and a "class-level" docblock immediately above each class. Examples of such docblocks can be found below.

#### Files
Every file that contains PHP code must have a docblock at the top of the file that contains these phpDocumentor tags at a minimum:

    /**
     * This file is part of the {@link http://ontowiki.net OntoWiki} project.
     *
     * @copyright Copyright (c) 2009, {@link http://aksw.org AKSW}
     * @license http://opensource.org/licenses/gpl-license.php GNU General Public License (GPL)
     */

For files that belong to Erfurt this docblock will look slightly different.

    /**
     * This file is part of the {@link http://aksw.org/Projects/Erfurt Erfurt} project.
     *
     * @copyright Copyright (c) 2009, {@link http://aksw.org AKSW}
     * @license http://opensource.org/licenses/gpl-license.php GNU General Public License (GPL)
     */
    
#### Classes
Every class must have a docblock that contains these phpDocumentor tags at a minimum:

    /**
     * Short description for class
     *
     * Long description for class (if any) ...
     *
     * @copyright Copyright (c) 2008, {@link http://aksw.org AKSW}
     * @license http://opensource.org/licenses/gpl-license.php GNU General Public License (GPL)
     * @category OntoWiki or Erfurt, respectively
     * @package example
     * @subpackage subpackage
     * @author Carl Committer <carl.committer@gmail.com>
     */
#### Functions
Every function, including object methods, must have a docblock that contains at a minimum:
* A description of the function
* All of the arguments
* All of the possible return values

Multiple parameter or return values should be separated by a dash (pipe):

    @param string|null $paramOne Parameter one

It is not necessary to use the "@access" tag because the access level is already known from the `public`, `private`, or `protected` modifier used to declare the function.

If a function/method may throw an exception, use @throws for all known exception classes:

    @throws exceptionclass [description]
