## Under construction

## Assumptions
We assume that your company has a set of products for which information is available in some structured form, but not as Linked Data (if it is, follow [How to use and consume other Linked Data resources](How-to-use-and-consume-other-Linked-Data-resources) instead).

## Good Relations Vocabulary
We will use [Good Relations](http://www.heppnetz.de/projects/goodrelations/) which is a popular E-Commerce vocabulary that is respected by Google and Yahoo, among others. Enriching your product data with RDF-a is a means of Semantic SEO and increases your search engine ratings and preview information.

## Modelling your Product Data with an Example

First, you need to create a new knowledge base. Go to **Knowledge Bases**->**Edit**->**Create Knowledge Base**. Name it `http://myproducts.com`, select **Import From the Web** and enter `http://www.heppnetz.de/ontologies/goodrelations/v1.owl` into the location field. Click on **Save Model Configuration**. The knowledge base now contains the complete Good Relations vocabulary. 

For simplicity we show the modelling for just two exemplary products:

![Example Product Neclace](images/necklace_without_navigation.png)
![Example Product Ring](images/brilliant_ruby_ring_without_navigation.png)

These products share a common set of attributes:
- Name
- Category
- Description
- Price

We now need to find the classes and properties in the Good Relations vocabulary, that are equivalent to these attributes. Consulting the [Product or Service section](http://wiki.goodrelations-vocabulary.org/Documentation/Product_or_Service) in the [Good Relations documentation](<http://wiki.goodrelations-vocabulary.org/Documentation>) yields the class [`gr:ProductOrServiceModel`](http://www.heppnetz.de/ontologies/goodrelations/v1.html#ProductOrServiceModel), which is "*A product model, i.e. a datasheet, like "Nikon T90", "iPod Nano 16 GB", or similar. This is basically the abstract definition of product features for mass-produced commodities.*".

We thus create a new Resource 



## From a Database

publish as rdfa