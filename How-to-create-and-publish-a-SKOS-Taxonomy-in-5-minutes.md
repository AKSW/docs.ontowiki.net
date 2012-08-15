## The example taxonomy

    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
    @prefix ex: <http://www.example2.com/>.

    ex:Animal rdf:type skos:Concept;
      skos:prefLabel "Animal"@en;
      skos:hiddenLabel "Annimal"@en.

    ex:Dog rdf:type skos:Concept;
      skos:prefLabel "Dog"@en;
      skos:hiddenLabel "Dogg"@en;
      skos:broader ex:Animal.

    ex:Pluto rdf:type ex:Dog;
     skos:prefLabel "Pluto".                                                              

## Create the knowledge base
- Open OntoWiki and log in as "Admin" or some other user that can create knowledge bases.
- Go to **Knowledge Bases**->**Edit**->**Create Knowledge Base**.
- Set the **Knowledge Base URI** to `http://www.example.com/`.

Now you have several options:

1.  Add classes and properties using dialogs
    - Select **Create Empty Knowledge Base** and click on **Create Knowledge Base**.
    - Go to **Navigation: Classes**->**Edit**->**Add resource here**.
    - Set the **Type** to `skos:Concept`.
    - Click on **Add Property** and choose **preferred label**. Type `Animal` in the text box and choose `en` as a language.
    - Click on **Add Property** again, type `skos:hiddenLabel` in the text field and hit enter. Type `Annimal` in the text box and choose `en` as a language. Click on **Create Resource**.
    - On the right you should see the window "Properties of Animal". Click on **Clone** in the **Properties** tab. Replace the values of the preferedLabel and hiddenLabel with `Dog` and `Dogg`, respectively.
    - Click on **Add Property** and type `skos:broader`. Select **Resource** and type `http://www.example.com/Class/Animal` in the text field.
    - Go to **Navigation: Classes**->**Edit**->**Add resource here**. Click on **Add Property**->**Preferred Label** and put `Pluto` into the text field. Click on the small triangle and select "en" as the language. Click on **Create Resource**. Under the tab **Properties**, go to the row **rdf:type** and click on the pencil symbol on the right (**Edit Values**). Change the type to `http://www.example.com/skos_Concept/Dog` and click on **Save Changes**.

2. Upload a file
    - Copy the example taxonomy and save it as a file named `example.n3`.
    - Select **Upload a File**, File Type **Autodetect** and browse for the file `example.n3`.
    - Click on **Create Knowledge Base** and then **Save Model Configuration**.

3. Paste source
    - Select **Paste Source**.
    - Select Format **n3**, copy the example taxonomy and paste it into the text box..
    - Click on **Create Knowledge Base** and then **Save Model Configuration**.