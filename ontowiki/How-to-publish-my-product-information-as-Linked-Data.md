---
title: How-to-publish-my-product-information-as-Linked-Data
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_How-to-publish-my-product-information-as-Linked-Data/
---
## Good Relations Vocabulary
The best way to publish your product information is to model it with the [Good Relations Vocabulary](http://www.heppnetz.de/projects/goodrelations/) which is a popular E-Commerce vocabulary that is respected by Google and Yahoo, among others. Enriching your product web pages with the resulting RDF-a data is an effective means of Semantic Search Engine Optimization.
The next section describes this process for an exemplary product, but if you have any questions beyond that be sure to check out the [video recordings](http://www.ebusiness-unibw.org/wiki/Web_of_Data_for_E-Commerce_Tutorial_ISWC2009#Video_Recording_of_the_Event) of the excellent and comprehensive [ISWC 2009 Tutorial: The Web of Data for E-Commerce in Brief](http://www.ebusiness-unibw.org/wiki/Web_of_Data_for_E-Commerce_Tutorial_ISWC2009).

## Modelling your Product Data with an Example

### Import the Good Relations Vocabulary

First, you need to create a new knowledge base. Go to **Knowledge Bases**->**Edit**->**Create Knowledge Base**. Name it `http://exampleproducts.com`, select **Import From the Web** and enter `http://www.heppnetz.de/ontologies/goodrelations/v1.owl` into the location field. Click on **Save Model Configuration**. The knowledge base now contains the complete Good Relations vocabulary. 

### Identify Attributes

For simplicity we show the modelling for just one exemplary product:

![Example Product Neclace]({{ "/images/necklace_without_navigation.png" | prepend: site.baseurl }})

This product has the following attributes we want to model:
- Name
- Category
- Description
- Price

### Find matching Classes and Properties

We now need to find the classes and properties in the Good Relations vocabulary that are equivalent to these attributes. Consulting the [Product or Service section](http://wiki.goodrelations-vocabulary.org/Documentation/Product_or_Service) in the [Good Relations documentation](<http://wiki.goodrelations-vocabulary.org/Documentation>) yields the class [`gr:ProductOrServiceModel`](http://www.heppnetz.de/ontologies/goodrelations/v1.html#ProductOrServiceModel), which is "*A product model, i.e. a datasheet, like "Nikon T90", "iPod Nano 16 GB", or similar. This is basically the abstract definition of product features for mass-produced commodities.*".

Our product model now needs two classes, gr:ProductOrServiceModel being one, and one for *Neclace* being the other. First we look for a fitting class in Good Relations but fail to find any. The next place to go should be [eClassOWL - The Web Ontology for Products and Services](http://www.heppnetz.de/projects/eclassowl/) but even there we don't find a fitting class. Fortunately, Wikipedia, and thus its Semantic Web counterpart DBpedia, has up-to-date entries for nearly everything and we can use `http://dbpedia.org/resource/Necklace`.

[The documentation of `gr:ProductOrServiceModel`](http://www.heppnetz.de/ontologies/goodrelationsv1.html#ProductOrServiceModel) contains the following matching Properties (rdfs:domain):
- `gr:name`
- `gr:description`

### Model the Data

    @prefix ex: <http://exampleproducts.com/>.
    @prefix dbpedia: <http://dbpedia.org/resource/>.

    ex:GoldenNecklaceProductModel
     a gr:ProductOrServiceModel;
     a dbpedia:Necklace;
     gr:name "Golden Necklace";
     gr:description "a golden necklace".

For directions on how get this data into the knowledge base, see [How to create and publish a SKOS Taxonomy in 5 minutes - Add classes and properties using dialogs](http://docs.ontowiki.net/ontowiki_How-to-create-and-publish-a-SKOS-Taxonomy-in-5-minutes#dialog).

The remaining attribute, *price*, cannot be directly modelled as an attribute of the product model. The problems are:

- we don't want to sell our *product model* (which would be equivalent to selling the trademark) but a *product* instead
- there can be different prices at different shops and different times

Therefore we need the class [`gr:Offering`](http://www.heppnetz.de/ontologies/goodrelations/v1#Offering), which represents an announcement of an `gr:BusinessEntity` to provide (or seek) a `gr:BusinessFunction` for a certain `gr:ProductOrService`.

The business entity and the offering we model as:

     ex:myCompany
      a gr:BusinessEntity;
      gr:hasLegalName "My Company"^^xsd:string;
      gr:offers ex:GoldenNecklaceOffering.

    ex:GoldenNecklaceOffering
     a gr:Offering;
     gr:hasBusinessFunction gr:Sell;
     gr:includes ex:GoldenNecklaceProductModel;
     gr:hasPriceSpecification ex:GoldenNecklacePriceSpecification.

Now we just need to define the price specification:

    ex:GoldenNecklacePriceSpecification
     a gr:UnitPriceSpecification;
     hasCurrency "EUR";
     hasCurrencyValue "35".

You now have successfully modelled a product model and it's offering. Repeat this process for all your products.