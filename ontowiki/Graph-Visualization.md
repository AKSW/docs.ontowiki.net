---
title: Graph-Visualization
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /Graph-Visualization.html
editme_path: ontowiki/Graph-Visualization.md
---
In the branch named "QuickAdd" you can find a new component which visualizes a graph based structure. It based on few libraries: Raphael, Graph Dracula, jQuery and jQuery SVG Plugin. In the course of this page the component and their parts will be described. Additional you get an overview how to wrote own stuff on top of that or extend the existing code. Enjoy!

\_Warning: This component is under heady development so functions, files or whatever can be changed from today to tomorrow.\_

## Before we start

There must be an executable Ontowiki installation. If you havent it you can check [this]({{ "Install-Ontowiki.html" | prepend:site.baseurl }}). The database backend is indifferent, MySQL or Virtuoso are usable. At this point the Ontowiki installation is accessible via [http://localhost/myow](http://localhost/myow) and the files are in \*/opt/lampp/htdocs/myow\*. If your paths differ please modify the posted ones.

## Get the current development snapshot

Check out the current snapshot over git. If you are new to Git please read [the+git+documentation](https://git-scm.com/documentation).

```
cd /opt/lampp/htdocs/myow
```

and check out current git state

```
git pull
```

Update all files agains QuickAdd branch.

```
git update Feature-QuickAdd
```

Warning: The branch is now activated and commits go to this branch!

The following command should show you a file - and folder list.

```
ls /opt/lampp/htdocs/myow/extensions/components/iowaviz
```

If you see a list you have successfully get the snapshot. Next the parts of iowaViz will be described.

## Parts of iowaViz

The component is named iowaViz. They contains Javascript libraries, PHP classes and Ontowiki related stuff (Controller and Helper).

The foreign Javascript libraries in iowaviz component scripts folder ( iowaviz/scripts ) are

- raphael ( [http://raphaeljs.com/](http://raphaeljs.com/) )
- dracula ( [http://www.graphdracula.net](http://www.graphdracula.net) )
- jquery.svg ( [http://keith-wood.name/svg.html](http://keith-wood.name/svg.html) )

Raphael is the heart of this component. It draws the SVG elements like circles, ellipses or paths. It uses SVG for non IE browsers and VML for IE.

Dracula Graph Library is build on top of Raphael and provides an easier way for creating graph based visualizations. As Raphael draws many kinds of SVG elements like diagrams, plots and charts, Dracula is specialized on graphs.

jQuery's SVG Plugin is build on top of jQuery which is used in Ontowiki too. This plugin provides a fancy way for accessing SVG elements using jQuery's $().

The PHP classes are

- WeightedGraph.php
- WeightedEdge.php
- Node.php

In general you only need WeightedGraph class. It provides all related stuff for creating and maintain a graph structure. It allows you to import an Erfurt-SPARQL-Result into the WeightedGraph structure, implements Iterator interface so you can interate over it in a standardized way and additional it provides functions for weighted statements and publish them as drawable SVG elements.

## To introduce iowaViz

Its build on top of dracula. There are to Javascript files which are provides different functionality:

- iowaviz/scripts/iowaViz.js
- iowaviz/scripts/iowaViz.events.js

The iowaViz.js provides base functionality. Following a short function overview:

### iowaViz.js - init

It encapsules dracula init code and setting object variables e.g. drawing area name.

### iowaViz.js - get

A help function for providing a cleaner way to access a SVG element. With SVG Plugin you need

```
$( element, $( '#svgDiv' ).svg () );
```

element is a reference of a SVG element. For later using its easier if you use

```
iowaViz.get ( element );
```

There are two pros:

- dont need to set everywhere the #svgDiv id new if it will be changed sometimes
- wrote less code and because of that you get an easly readable code

### iowaViz.js - addEdge

Creating an edge between two nodes. If the two nodes arent exists they will be created. Parameter e contains information about connecting nodes and so on:

- sourceNodeTitle : Uri of source node.
- sourceNodeTitle : Title of source node.
- targetNodeTitle : Uri of target node.
- targetNodeTitle : Title of target node.
- isDirected : True if directed, otherwise false.
- fillColor : A color value.
- lineWidth : A number for line width.
- connectionTitle : Title of the connection.

## How to set up your own visualization

This section describes how to set up own implementations. The \*guiAction\* function in IowavizController.php is used as an example.

First we initialize the graph and load config from component.ini. For that we need a part of the \*init\* function.

```
public function init ( )
{
   // ...

   require ( 'WeightedGraph.php' );
        
        
        
        
   $this->_standard_weight = (float) $this->_privateConfig->standard_weight;
   $this->_weight_min = (float) $this->_privateConfig->weight_min;
   $this->_weight_max = (float) $this->_privateConfig->weight_max;
   $this->_threshold = (float) $this->_privateConfig->threshold;
        
        
   $this->_privateConfig->model = $this->_model;
            
            
   // Create graph instance.
   $this->_graph = new WeightedGraph ( );
        
        
   // Initialize instance
   $this->_graph->init ( $this->_privateConfig->toArray() );
}
```

Next we get a list of all models, setting up graph related stuff like area size and execute a sample query.

```
public function guiAction ()
{
    // Disable OW layout stuff
    $this->_helper->layout()->disableLayout();
            
            
    // Getting all available not hidden models -----------------------------
    $models = Erfurt_App::getInstance()->getStore()->getAvailableModels ( false );
    
    
    $this->view->models = array ();
    
    
    foreach ( $models as $model => $value ) $this->view->models [] = $model;
    
    
    // Initialize graph instance -------------------------------------------
    $this->_graph->setAreaName ( 'drawingArea' );
    $this->_graph->setAreaWidth ( '700' );
    $this->_graph->setAreaHeight ( '300' );
    
    
    // Set weight threshold
    $this->_graph->setThreshold ( 0.0 );
    
    
    // Questioning model and save result and add result-elements to $_graph
    $res = $this->_model->sparqlQuery ( 'SELECT ?s ?p ?o WHERE { ?s ?p ?o. } LIMIT 5;' );
    $this->_graph->addResultSetArray ( $res );
            
            
    // Weights all edges in edges-list.
    $this->_graph->weightAllEdges ( );
    
    
    // Register instances in view
    $this->view->graph = $this->_graph;
    $this->view->urlBase = $this->_componentUrlBase;
}
```

Following a short overview about the main parts.

This code get the all available not hidden models. After getting them its necessary to extract the model names from the array keys.

```
// Getting all available not hidden models -----------------------------
$models = Erfurt_App::getInstance()->getStore()->getAvailableModels ( false );
    
    
$this->view->models = array ();
    
    
foreach ( $models as $model => $value ) $this->view->models [] = $model;
```

Following code setting main settings of the later drawing graph. \*drawingArea\* is the name of the div container which later contains the SVG elements. It has a \*width\* and \*height\* too. \*Threshold\* is important if you would like to weight your statements.

```
$this->_graph->setAreaName ( 'drawingArea' );
$this->_graph->setAreaWidth ( '700' );
$this->_graph->setAreaHeight ( '300' );
    
    
// Set weight threshold
$this->_graph->setThreshold ( 0.0 );
```

For example data we questioning the knowledge base selecting few triples. After that we import them into our graph instance. The graph convert array elements into edges and nodes. For more information please look at function \*add\* and \*addResultSetArray\* in WeightedGraph.php.

```
// Questioning model and save result and add result-elements to $_graph
$res = $this->_model->sparqlQuery ( 'SELECT ?s ?p ?o WHERE { ?s ?p ?o. } LIMIT 10;' );
$this->_graph->addResultSetArray ( $res );
            
            
// Weights all edges in edges-list.
$this->_graph->weightAllEdges ( );
```

At this point guiAction function is complete. At the end we need an HTML file. In iowaviz/templates/iowaviz you found a file namend \*gui.html\*.

First the complete file

```
<html>
    <head>
        <title>iowaViz GUI</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        
        
        <!-- Needed libraries ---------------------------------------------- -->
        <!-- jQuery ( modified version of jQuery's SVG plugin) -->
        <script type="text/javascript" src="<?php echo $this->urlBase; ?>../../themes/silverblue/scripts/libraries/jquery.js"></script>
        
        
        <!-- jQuery Plugin - SVG Plugin - http://keith-wood.name/svg.html -->
        <script type="text/javascript" src="<?php echo $this->urlBase; ?>scripts/jquery.svg/jquery.svg.min.js"></script>
        <script type="text/javascript" src="<?php echo $this->urlBase; ?>scripts/jquery.svg/jquery.svgdom.min.js"></script>
        
        
        <!-- Raphael lib - http://www.raphaeljs.com -->
        <script type="text/javascript" src="<?php echo $this->urlBase; ?>scripts/raphael/raphael-min.js"></script>
        
        
        <!-- Graph Dracula - http://www.graphdracula.net -->
        <script type="text/javascript" src="<?php echo $this->urlBase; ?>scripts/dracula/js/dracula_graffle.js"></script>
        <script type="text/javascript" src="<?php echo $this->urlBase; ?>scripts/dracula/js/dracula_graph.js"></script>
                
                
        <!-- Our JS code -->
        <script type="text/javascript" src="<?php echo $this->urlBase; ?>scripts/iowaViz.js"></script>
        <script type="text/javascript" src="<?php echo $this->urlBase; ?>scripts/iowaViz.events.js"></script>
        
        
        
        
        <!-- CSS stuff ----------------------------------------------------- -->
        <link rel="stylesheet" href="<?php echo $this->urlBase; ?>css/iowaViz.css" type="text/css" media="screen">
        
        
    </head>
    <body>
    
    
        <div id="statistic_panel">
            
            
            <!-- Selecting one of available models and browse it after reload -->
            <form name="statistic_panel_form" action="" method="post">
                <select name="m">
            
            
                    <?php if ( isset ( $_REQUEST ['m'] ) ) { ?>             
                        <option value="<?php echo $_REQUEST ['m']; ?>"><?php echo $_REQUEST ['m']; ?></option>
            
            
                    <?php }            
                          foreach ( $this->models as $m ) { ?>
                        <option label="<?php echo $m; ?>" value="<?php echo $m; ?>">
                            <?php echo $m; ?>
                        </option>
                    <?php } ?>
            
            
                </select>
                <input type="submit" value="select" />
            </form>
            
            
            Number of nodes: <div id="number_of_nodes"><?php echo $this->graph->getNodeCount (); ?></div>
            <table>
                <tr><td colspan="2">Current node</td></tr>
                <tr>
                    <td>Name</td>
                    <td><div id="current_node_name"></div></td>
                </tr>
            </table>
            
            
        </div>
        
        
        <hr>
    
    
        <!-- SVG code -->
        <div id="drawingArea"></div>

        <script language="javascript" type="text/javascript">
            
            
            // Initialize iowaViz
            <?php 
            echo $this->graph->getInitJS (); 
            ?>
            
            
            
            
            // Generate edges and nodes.
            <?php 
            echo $this->graph->toGraphDraculaJsCode (); 
            ?>                 
            
            
            
            
            // Draw graph.
            <?php 
            echo $this->graph->getDrawJS (); 
            ?>
            
            
        </script>
    </body>
</html>
```

In head section needed libraries are included.

```
<!-- ... -->

   <!-- Our JS code -->
   <script type="text/javascript" src="<?php echo $this->urlBase; ?>scripts/iowaViz.js"></script>
   <script type="text/javascript" src="<?php echo $this->urlBase; ?>scripts/iowaViz.events.js"></script>
        
        
        
        
   <!-- CSS stuff ----------------------------------------------------- -->
   <link rel="stylesheet" href="<?php echo $this->urlBase; ?>css/iowaViz.css" type="text/css" media="screen">
```

The CSS file contains all style settings for the nodes.

The content of div container named \*statistic\_panel\* is unimportant for this demonstration. It only contains tools for setting up a new model and show few information about the nodes.

Following code contains a div container which will be named as the drawingAreaName was set in the guiAction before. The Javascript section contains only three functions. \*getInitJS\* wrote dracula init code and setting up iowaViz object. The function toGraphDraculaJsCode convert saved edges and nodes in graph instance into SVG elements, but nothing will be drawed at this point! Not before the function getDrawJS is executed the graph will be drawed in the div container.

```
<!-- SVG code -->
    <div id="<?php echo $this->graph->getAreaName (); ?>"></div>

    <script language="javascript" type="text/javascript">
        
        
        // Initialize iowaViz
        <?php 
        echo $this->graph->getInitJS (); 
        ?>
        
        
        
        
        // Generate edges and nodes.
        <?php 
        echo $this->graph->toGraphDraculaJsCode (); 
        ?>                 
        
        
        
        
        // Draw graph.
        <?php 
        echo $this->graph->getDrawJS (); 
        ?>
        
        
    </script>
```

At this point you have learn how to create a graph, put data into it and drawing SVG elements. But theres more to come. In the file \*iowaviz/scripts/iowaViz.events.js\* you found Javascript events which will be executed after special user actions.

One of them

```
// TOGGLE ------------------------------------------------------------------
    $('ellipse').toggle(
    
    
        function() // After click
        {            
            // Add CSS class
            iowaViz.get ( this ).addClass ( 'iV_node_click' );
            $( '#current_node_name' ).html ( iowaViz.get ( this ).attr ( 'about' ) );
        },
        
        
        function () // After unclick
        {
            iowaViz.get ( this ).removeClass ( 'iV_node_click' );      
            $( '#current_node_name' ).html ( "&nbsp;" );      
        }
    );
```

is the toggle one. After a click on a node it gets a new CSS class named \*iV\_node\_click\* and in div container \*current\_node\_name\* the about attribute value will be shown. If you click on the same node again the CSS class and about value will be removed from the div.

Here you can put any events you know from jQuery. With jQuery's SVG Plugin its possible to use them for SVG too.

