This class handles one resource. 

## Example

This example shows a simple usage of the class. It assumes that you are in a OntoWiki controller action and have a model selected.

```
// you are in a controller action!
$r = new OntoWiki_Model_Resource (
   $this->_owApp->selectedModel->getStore(),
   $this->_owApp->selectedModel,
   'http://data.lod2.eu/scoreboard/'
);
```

Now $r is fully initialized. Now we override $r with the return value of **getValues()**. This function returns all predicates and objects which are associated with the given resource.

```
$r = $r->getValues();
```

Now $r is a multi dimensional array. Here an example how it could looks like:

```
array(1) {
  ["http://data.lod2.eu/scoreboard/"]=>
  array(7) {
    ["http://purl.org/dc/elements/1.1/creator"]=>
    array(1) {
      [0]=>
      array(8) {
        ["content"]=>
        string(13) "Max Mustermann"
        ["object"]=>
        string(13) "Max Mustermann"
        ["object_hash"]=>
        string(32) "c824e9b77c049d5055adf0b784e985b8"
        ["datatype"]=>
        NULL
        ["lang"]=>
        NULL
        ["url"]=>
        NULL
        ["uri"]=>
        NULL
        ["curi"]=>
        NULL
      }
    }
...
```

In this example **http://data.lod2.eu/scoreboard/** is the resource uri. In one subarray **http://purl.org/dc/elements/1.1/creator** is a predicate and contains a couple of information about the object.