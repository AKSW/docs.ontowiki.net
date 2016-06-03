### addMultipleStatements($statements)
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