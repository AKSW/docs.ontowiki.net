OntoWiki is not tested for security yet...

## SPARQL-Injection

HTTP Parameters should be validated for their expected type. For example if you use a parameter r that should contain a URI and is used in a SPARQL query, you should make sure it does not contain something like <tt>"&gt; } UNION {[bad]} UNION {&lt;http://notexisting"</tt>. We plan to use Zend\_Validator's in Ontowiki\_Request::getParam.

## CRLF Injection Attack

[http://www.acunetix.com/websitesecurity/crlf-injection.htm](http://www.acunetix.com/websitesecurity/crlf-injection.htm) PHP has several functions that take filenames as one of their arguments: fopen(), file() and some others. If allow\_url\_fopen is set to On in php.ini, those functions also accept URLs instead of regular files, and they connect to the server in question with the correct protocol. This functionality is vulnerable to some CRLF Injection attacks.

One solution is to make sure that all variables that are used in this type of URL are clean, by including this command in your PHP scripts:

```
$var = preg_replace('/\\s+/', '', $var);
```
