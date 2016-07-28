---
title: Ontowiki-model
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_Ontowiki-model/
editme_path: ontowiki/Ontowiki-model.md
---
## addMultipleStatements($statements)
```
$subject = "http://localhost/subjectUri";
$predicate = "http://localhost/predicateUri";

$statements = array();
$statements[$subject] = array();
$statements[$subject][$predicate] = array();
$statements[$subject][$predicate][] = array(
    'value' => 'valueUri',
    'type' => 'uri'
);
```