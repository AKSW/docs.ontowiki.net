---
title: How-to-test
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_How-to-test/
---
Make sure that you have a runnable test environment. Please check [[Setup an OntoWiki Test Environment|PHPUnit]]!

## Folder structure

## Extension test cases

Each extension can be tested automatically when you execute `make test-extensions`.

### Bootstrap

Create a file named **TestHelper.php** in the **tests** folder of your extension. 

## HowTo create a new TestCase

Naming should be oriented on OntoWiki's class names. For example

`Folder/To/FancyClass.php`

results in

`Folder_To_FancyClass`

