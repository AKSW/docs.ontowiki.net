For this tutorial we will edit the taxonomy created in [How to create and publish a SKOS Taxonomy in 5 minutes](How-to-create-and-publish-a-SKOS-Taxonomy-in-5-minutes).

Log in and select the knowledge base you want to view and edit. Click on **Actions**->**View all Resources**.

## Add Classes and Properties
See [How to create and publish a SKOS Taxonomy in 5 minutes - Add classes and properties using dialogs](How-to-create-and-publish-a-SKOS-Taxonomy-in-5-minutes#dialog)

## Edit Properties
Click on **Actions**->**View all Resources** and select the resource you want to edit. Alternatively you can click on **Actions**->**Jump to Resource** and type the name of the resource in the text field (prefix not required, e.g. "Pluto" would be sufficient in our [example taxonomy](How-to-create-and-publish-a-SKOS-Taxonomy-in-5-minutes#taxonomy)). Click on **Edit Properties** and edit the values. Click on **Save Changes**.

## Rename the URI of a Resource
There is no official rename functionality but a possible workaround.
Go to the **Source** tab. In the text box search for the line containing the name of the resource, e.g. `ex:Dog rdf:type skos:Concept;`. Change it to a new value, for example `ex:Wolf rdf:type skos:Concept;` and click on "Save Source". You have to reselect your knowledge base on the left in order to refresh the view.

*This will break all existing links from other resources to the renamed resource.*

