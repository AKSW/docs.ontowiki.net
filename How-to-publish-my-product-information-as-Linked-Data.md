## Under construction

## Good Relations Vocabulary
The best way to publish your product information is to model it with the [Good Relations Vocabulary](http://www.heppnetz.de/projects/goodrelations/) which is a popular E-Commerce vocabulary that is respected by Google and Yahoo, among others. Enriching your product web pages with the resulting RDF-a data is an effective means of Semantic Search Engine Optimization.
The next section describes this process for an examplary product but if you have any questions beyond that be sure to check out the [video recordings](http://www.ebusiness-unibw.org/wiki/Web_of_Data_for_E-Commerce_Tutorial_ISWC2009#Video_Recording_of_the_Event) of the excellent and comprehensive [http://www.ebusiness-unibw.org/wiki/Web_of_Data_for_E-Commerce_Tutorial_ISWC2009](*ISWC 2009 Tutorial: The Web of Data for E-Commerce in Brief*).

## Modelling your Product Data with an Example

First, you need to create a new knowledge base. Go to **Knowledge Bases**->**Edit**->**Create Knowledge Base**. Name it `http://myproducts.com`, select **Import From the Web** and enter `http://www.heppnetz.de/ontologies/goodrelations/v1.owl` into the location field. Click on **Save Model Configuration**. The knowledge base now contains the complete Good Relations vocabulary. 

For simplicity we show the modelling for just one exemplary product:

![Example Product Neclace](images/necklace_without_navigation.png)

These products share a common set of attributes:
- Name
- Category
- Description
- Price

We now need to find the classes and properties in the Good Relations vocabulary, that are equivalent to these attributes. Consulting the [Product or Service section](http://wiki.goodrelations-vocabulary.org/Documentation/Product_or_Service) in the [Good Relations documentation](<http://wiki.goodrelations-vocabulary.org/Documentation>) yields the class [`gr:ProductOrServiceModel`](http://www.heppnetz.de/ontologies/goodrelations/v1.html#ProductOrServiceModel), which is "*A product model, i.e. a datasheet, like "Nikon T90", "iPod Nano 16 GB", or similar. This is basically the abstract definition of product features for mass-produced commodities.*".

Our product model now needs two classes, gr:ProductOrServiceModel being one and and one for the *category* or *type of product* being the other.

[The documentation of `gr:ProductOrServiceModel`](http://www.heppnetz.de/ontologies/goodrelationsv1.html#ProductOrServiceModel) contains the following matching Properties (rdfs:domain):
- `gr:name`
- `gr:description`

The remaining attribute, *price* is .

## From a Database

publish as rdfa

see the [The GoodRelations vocabulary in detail (video tutorial)](http://vimeo.com/8118439)

ex:myCompany
 a gr:BusinessEntity;
 gr:hasLegalName "My Company"^^xsd:string;
 gr:offers ex:GoldenNecklaceOffering.

ex:BrilliantRubyRingOffering
a gr:Offering;
gr:hasBusinessFunction gr:Sell;

ex:GoldenNecklaceOffering
a gr:Offering;
gr:hasBusinessFunction gr:Sell;

ex:GoldenNecklaceProducts
 a gr:ProductOrServiesSomeInstancesPlaceholder

 a gr:ProductOrServiceModel
 gr:name "Golden Necklace";
 gr:description "a golden necklace".

http://dbpedia.org/resource/Necklace