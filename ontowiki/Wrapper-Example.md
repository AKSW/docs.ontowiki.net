---
title: Wrapper-Example
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_Wrapper-Example/
---
The Erfurt Data Wrapper extension type was introduced in order to allow for lightweight extension on the data level. In most cases a wrapper will hanlde a certain URI and return additional data for that URI if available. A good example for this is the Linked Data Wrapper, that retrieves LinkedData URIs. Nevertheless a wrapper could also do more sophisticated things like e.g. adding and removing statements internally. This tutorial will enable you as a extension devoloper to develop such data wrapper and test them within OntoWiki.

# The Erfurt Wrapper Architecture

There are two classes that are important for you as a developer:

```
abstract class Erfurt_Wrapper
{
// ...
}
```

and

```
class Erfurt_Wrapper_Exception extends Erfurt_Exception
{
}
```

Your wrapper class need to extend the abstract class `Erfurt\_Wrapper`. Whenever an something unintended happens inside your code, you should throw an exception of the type `Erfurt\_Wrapper\_Exception`.

There are five methods, that a wrapper needs to implement. Two of them are straightforward and return only metadata about the wrapper, such as a human readable name and description. These methods are called `getDescription()` and `getName()`.

The remaining three methods are best explained by going through the process of wrapping data. This process consists of three steps:

1. Check, whether the wrapper handles a certain URI (`isHandled`)
2. If a wrapper handles a certain URI, check whether there is data available for this URI (`isAvailable`).
3. If data is available, fetch and handle that data (`run`).

The following sections will explain the three steps in more detail.

## `isHandled($uri, $graphUri)`

This method will be called first by an application that uses wrapper. In most cases this will be called without user interaction and for a bunch of URIs. Therefore this method should answer the question as quick as possible.

For example:

```
public function isHandled($uri, $graphUri)
{
    if (preg_match("/^(http:\/\/twitter.com\/)(\w+)$/", $uri)) {
        return true;
    } else {
        return false;
    }
}
```

Of course it is in some cases not sufficient to do a match against a pattern only. Your wrapper could also do a SPARQL query against the graph.

For example:

```
public function isHandled($uri, $graphUri)
{
    require_once 'Erfurt/Sparql/SimpleQuery.php';
    $query = new Erfurt_Sparql_SimpleQuery();
            
            
    $query->setProloguePart('PREFIX foaf: <http://xmlns.com/foaf/0.1/> SELECT ?o');
    $query->addFrom($graphUri);
            
            
    $wherePart = "WHERE { 
         <$uri> foaf:accountName ?o . 
         <$uri> foaf:accountServiceHomepage <http://twitter.com/home>
    }";
        
        
    $query->setWherePart($wherePart);
        
        
     $store = Erfurt_App::getInstance()->getStore();
     $result = $store->sparqlQuery($query);
            
            
     if (count($result) > 0) {
         return true;
     }
}
```

## `isAvailable($uri, $graphUri)`

This method checks, whether there is data available for the URI. In many cases this will imply to do the request, that will contain the data. Therefore it is important, that your wrapper caches the data over multiple requests (see section about caching).

For example:

```
public function isAvailable($uri, $graphUri)
{
    $retVal = false;
    $data = array();
        
        
    $match = array();
    if (preg_match($this->_pattern, $uri, $match)) {
        $name = $match[2];
        
        
        // Currently not supported twitter uris.
        $notAllowedNames = array('home', 'users', 'statuses', 'direct_messages', 'friendships', 'friends');
            
            
        if (!in_array($name, $notAllowedNames)) {
            $url1 = 'http://twitter.com/statuses/user_timeline/' . $name . '.json';

            require_once 'Zend/Http/Client.php';
            $client = new Zend_Http_Client($url1, array(
                'maxredirects' => 0,
                'timeout' => 30
            ));
                
                
            if (isset($this->_config->username) && isset($this->_config->password)) {
                    $client->setAuth($this->_config->username, $this->_config->password);
            }
                
                
            $response = $client->request();

            if ($response->getStatus() === 200) {
                $result = json_decode($response->getBody(), true);
                $data['status'] = $result;
                $retVal = true;
            }
        } 

        // Cache the retrieved data if possible.        
    }

    return $retVal;    
}
```

## `run($uri, $graphUri)`

This method will do whatever the wrapper is intended to do. In most cases this will return an array containing statements that the application could add to the garph or statements that should be deleted. It is also possible that the wrapper itself does such operations. Therefore the result of this method is an array containing a list of status codes (defined in `Erfurt\_Wrapper`), a description, an optional array containing statements to be added, an optional array containing a pattern to match statements that should be deleted. If the wrapper adds/removes statements itself, the result may contain the number of statements added/removed.

Please have a look at [http://docs.ontowiki.net/api/erfurt/wrapper/Erfurt\_Wrapper.html](http://docs.ontowiki.net/api/erfurt/wrapper/Erfurt_Wrapper.html) for more detailed informations about the status codes.

A result could for example look like this:

```
array(
    'status_codes' => array(Erfurt_Wrapper::NO_MODIFICATIONS, Erfurt_Wrapper::RESULT_HAS_ADD),
    'status_desc' => "There were $count statements found for <$uri>",
    'add' => $statementsArray 
);
```

## Caching

Every wrapper has its own caching object. To access it in your code use `$this->\_cache`

For example:

```
$id = $this->_cache->makeId($this, 'isAvailable', array($uri, $graphUri));
$result = $this->_cache->load($id);

if ($result !== false) {
    if (!isset($this->_cachedData[$graphUri])) {
        $this->_cachedData[$graphUri] = array($uri => $result['data']);
    } else {
        $this->_cachedData[$graphUri][$uri] = $result['data'];
    }
            
            
    return $result['value'];
}
```

- Note:\* Caching only works, if the `tmp` directory under the Erfurt tree is writable.

Please have a look at the [[http://framework.zend.com/manual/en/zend.cache.html](http://framework.zend.com/manual/en/zend.cache.html) Zend documentation] for further informations regarding `Zend\_Cache`.

## Make your wrapper configurable

You can access your private configuration (private section in the ini file) by doing the following:

```
$test = $this->_config->key->subkey;
```

Please have a look at the [[http://framework.zend.com/manual/en/zend.config.html](http://framework.zend.com/manual/en/zend.config.html) Zend documentation] for further informations regarding `Zend\_Config`.

## Use PHP librariers inside your Wrapper

You can use custom PHP libraries in your code, by putting them into a subdirectory, e.g. `libraries`. You can access them in your code by doing the following:

```
// Use your own libs.
require_once 'libraries/TestPhpLibrary.php';
$libObj = new TestPhpLibrary();

if ($libObj->testLibMethod()) {
    // Do something...
}
```

# Develop a Wrapper from the scratch

## Create the requires files and directories

Let us assume your wrapper will be called `superwrapper`.

You need to create a directory that is called `superwrapper` as well as a file `superwrapper.php` and a ini file called `wrapper.ini` inside your directory.

To make the wrapper active, the ini file looks like this:

```
enabled = true

[private]
; Your private configuration here...
```

The `superwrapper.php`file contains the following:

```
require_once 'Erfurt/Wrapper.php';

class SuperwrapperWrapper extends Erfurt_Wrapper
{
   // ...
}
```

## Implement the requires methods

For example:

```
require_once 'Erfurt/Wrapper.php';

class SuperwrapperWrapper extends Erfurt_Wrapper
{
    public function getDescription()
    {
        return 'This is Super Wrapper. A wrapper for everything but nothing.';
    }

    public function getName()
    {
        return 'Super Wrapper';
    }

    public function isHandled($uri, $graphUri)
    {
        return true;
    }

    public function isAvailable($uri, $graphUri)
    {
        return true;
    }

    public function run($uri, $graphUri)
    {
        return array(
            'status_codes' => array(Erfurt_Wrapper::NO_MODIFICATIONS, Erfurt_Wrapper::RESULT_HAS_ADD),
            'status_desc' => 'One cool statements found.',
            'add' => array(
                $uri => array(
                                   'http://example.org/superwrapper/prop1' => array(
                                    array(
                                    'value' => 'Wrapped with Super wrapper', 
                                    'type' => 'literal')))
            )
        );
    }
}
```

# Activate your Wrapper with OntoWiki

The extension is located in the

```
extensions/datagathering
```

directory. In order to activate it you need to open the Extension Manager (in the Extras menu or <tt>&lt;your-ow&gt;/exconf</tt>).

The last step to take is to add your wrapper in the config of the datagathering extension and make sure you have URIs in context that are handled by your wrapper.

Now we will explain how the extension is composed to handle your wrapper.

## `DatagatheringPlugin`

The Datagathering plugin is a helper, that connects your wrapper to ontowiki, by listening to events fired by ontowiki. These events contain URIs and the plugin passes them to the wrapper and puts the result back in the event and sets it to the _handled_ state. It handles two events fired by OntoWiki.:

```
[events]
1 = onDisplayObjectPropertyValue
2 = onPropertiesAction
```

The first one is triggered, whenever a object property value (URI) is displayed. The second on is fired, when the properties view for a resource is going to be displayed.

## `DatagatheringModule`

The Datagathering module displays a small inner window inside the properties main view. It contains all active wrapper and for each wrapper the URIs in context, which are handled by a wrapper. In order to test, whether there is data available for a certain URI you need to expand the list of URIs by clicking on the small arrow. The next step is to click on a URI (maybe displayed with a label for it).

You then have to wait some time (depending on the wrapper). If you see the a green checkmark, then there is data available. Another click will the run the wrapper, which can mean whatever the wrapper does internally. In the most cases however, the wrapper will return a list of statements found and the component will add them to the graph.

## `DatagatheringComponent`

The Datagathering component does the heavy lifting. It adds two actions, a test and a import action. Both of them are called via an AJAX request. The import action takes all the statements returned by the wrapper and adds them to the graph.

