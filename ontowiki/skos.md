---
title: skos
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_skos/
---
# Taxonomy Management
## How to create and publish a SKOS taxonomy in 5 minutes?
In a real world case you would have deployed OntoWiki on a server reachable by some specific URL. Lets assume that URL is `http://www.products.com`. After the following steps the resources created in this examples would then be resolvable by accessing them with a browser, for example by visiting `http://www.products.com/owl_Class/Jewellery`. This means that all resources created in OntoWiki are automatically published.

### <a id="taxonomy"></a>The example taxonomy

    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns##> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core##> .
    @prefix ex: <http://www.products.com/>.
    @prefix owl: <http://www.w3.org/2002/07/owl##>.

    ex:Product rdf:type owl:Class;
      a skos:Concept;
      skos:prefLabel "Product"@en;

    ex:Jewellery rdf:type owl:Class;
      a skos:Concept;
      skos:prefLabel "Jewellery"@en;
      skos:altLabel "Jewelry"@en;
      skos:altLabel "Jewelery"@en;
      skos:broader ex:Product.                                                  

*Note: In a real world case it would be better to reuse an existing product class. for example `http://schema.org/Product`*.

### Create the knowledge base
- Open OntoWiki and log in as "Admin" or some other user that can create knowledge bases.
- Go to **Knowledge Bases**->**Edit**->**Create Knowledge Base**.
- Set the **Knowledge Base URI** to `http://www.products.com/`.

Now you have several options:
#### <a id="dialog"></a>Add classes and properties using dialogs
- Select **Create Empty Knowledge Base** and click on **Create Knowledge Base**.
- Go to **Navigation: Classes**->**Edit**->**Add resource here**.
- Click on **Add Property** and choose **rdf:Type**. Type `skos:Concept` in the text box.
- Click on **Add Property** and choose **preferred label**. Type `Product` in the text box and choose `en` as a language. Click on **CreateResource**.

![Create new Resource - Jewellery](https://github.com/AKSW/OntoWiki/wiki/images/ontowiki-screenshot-create-new-resource-jewellery.png)
- On the right you should see the window "Properties of Product". Click on **Clone** in the **Properties** tab. Replace the values of the preferedLabel with `Jewellery`.
- Click on **Add Property**, type `skos:altLabel` in the text field and hit enter. Type `Jewelery` in the text box and choose `en` as a language.
- Click on the plus symbol **+** of the alternative label, type `Jewelry` in the text box and choose `en` as a language.
- Click on **Add Property** and type `skos:broader`. Select **Resource** and type `http://www.products.com/owl_Class/Product` in the text field. Click on **Create Resource**.

#### <a id="upload-file"></a>Upload a file
- Copy the example taxonomy and save it as a file named `example.n3`.
- Select **Upload a File**, File Type **Autodetect** and browse for the file `example.n3`.
- Click on **Create Knowledge Base** and then **Save Model Configuration**.

#### Paste source
- Select **Paste Source**.
- Select Format **n3**, copy the example taxonomy and paste it into the text box..
- Click on **Create Knowledge Base** and then **Save Model Configuration**.

Go to the **Knowledge Bases** widget and select **products.com**. Under **Model info** click on **Actions**->**view all resources**. You should now see a list of the created instances.
![OntoWiki Screenshot with the Jewellery taxonomy resource list](https://github.com/AKSW/OntoWiki/wiki/images/ontowiki-screenshot-taxonomy-jewellery-resource-list.png)

## How to view and edit the concepts of my taxonomy?
For this tutorial we will edit the taxonomy created in [How to create and publish a SKOS Taxonomy in 5 minutes](How-to-create-and-publish-a-SKOS-Taxonomy-in-5-minutes).

Log in and select the knowledge base you want to view and edit. Click on **Actions**->**View all Resources**.

### Add Classes and Properties
See [How to create and publish a SKOS Taxonomy in 5 minutes - Add classes and properties using dialogs](How-to-create-and-publish-a-SKOS-Taxonomy-in-5-minutes##dialog)

### Edit Properties
![Screenshot Edit Properties](https://github.com/AKSW/OntoWiki/wiki/images/ontowiki-screenshot-edit-properties.png)

Click on **Actions**->**View all Resources** and select the resource you want to edit. Alternatively you can click on **Actions**->**Jump to Resource** and type the name of the resource in the text field (prefix not required, e.g. "Jewellery" would be sufficient in our [example taxonomy](How-to-create-and-publish-a-SKOS-Taxonomy-in-5-minutes##taxonomy)). Click on **Edit Properties** and edit the values. Click on **Save Changes**.

### Rename the URI of a Resource
*There is no official rename functionality so this is just a workaround.*
*This will break all existing links from other resources to the renamed resource.*

Go to the **Source** tab. In the text box search for the line containing the name of the resource, e.g. `ex:Dog rdf:type skos:Concept;`. Change it to a new value, for example `ex:Wolf rdf:type skos:Concept;` and click on "Save Source". You have to reselect your knowledge base on the left in order to refresh the view.

## How to use and consume other Linked Data resources?
### Import from a file
See [How to create and publish a SKOS Taxonomy in 5 minutes - Upload a file](#upload-file)

### Import from the Web
![Screenshot Import from the Web](https://github.com/AKSW/OntoWiki/wiki/images/ontowiki-screenshot-import-from-the-web.png)

Go to **Knowledge Bases**->**Edit**->**Create Knowledge Base**.
Set the **Knowledge Base URI** and select **Import From the Web**.
Set the location field to the URL of the file containing the RDF data and click on *Create Knowledge Base*.

### Import from a SPARQL endpoint - unfortunately not possible
