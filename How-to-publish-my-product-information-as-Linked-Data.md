## Under construction

## Assumptions
We assume that your company has a set of products for which information is available in some structured form, but not as Linked Data (if it is, follow [How to use and consume other Linked Data resources](How-to-use-and-consume-other-Linked-Data-resources) instead).

## Good Relations Vocabulary
We will use [Good Relations](http://www.heppnetz.de/projects/goodrelations/) which is a popular E-Commerce vocabulary that is respected by Google and Yahoo, among others. Enriching your product data with RDF-a is a means of Semantic SEO and increases your search engine ratings and preview information.

## Modelling your Product Data with an Example

First, you need to create a new knowledge base. Go to **Knowledge Bases**->**Edit**->**Create Knowledge Base**. Name it `http://myproducts.com`, select **Import From the Web** and enter `http://www.heppnetz.de/ontologies/goodrelations/v1.owl` into the location field. Click on **Save Model Configuration**. The knowledge base now contains the complete Good Relations vocabulary. 

For simplicity we show the modelling with just two exemplary products:

![Example Product Neclace](images/necklace_without_navigation.png)
![Example Product Ring](images/brilliant_ruby_ring_without_navigation.png)

These products share a common set of attributes:
- Name
- Category
- Description
- Price



## From a Database

publish as rdfa