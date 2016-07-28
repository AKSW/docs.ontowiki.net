---
title: Editing, Creating and Merging Documentation Pages
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_Editing_Creating_Merging_Documentation_Pages/
editme_path: ontowiki/Editing_Creating_Merging_Documentation_Pages.md
---

As OntoWiki is an Open-Source Program and we gladly accept help in forms of pull requests, our Documentation does allow
others to edit pages.

**You need an existing Github Account for this**

## Editing Pages

Editing Pages is an easy procedure. You click on the Github Edit me button on the page you want to edit, with this you know the name of the file you want to edit later on. Now you fork the repository AKSW/docs.ontowiki.net (the button for this should be on the top right side). You apply your changes in the file, and make a pull request (you might need to rebase your fork onto the docs.ontowiki.net master branch). Someone of the AKSW Staff will review your change and accept it.

## Creating Pages

To create Pages you need to be a bit more carefull. First you will fork the AKSW/docs.ontowiki.net Repository from Github.
Now you can create your file in the ontowiki folder as a .md file (we only accept Markdown for Documentation Pages).

Every file needs a header. As example we will use the header for this file (the `---` are mandatory)

    ---
    title: Editing, Creating and Merging Documentation Pages
    tags: [ontowiki]
    sidebar: ontowiki_sidebar
    permalink: /ontowiki_Editing_Creating_Merging_Documentation_Pages/
    editme_path: ontowiki/Editing_Creating_Merging_Documentation_Pages.md
    ---

This header contains all necessary entries. Furthermore optional entries are:

    ---
    keywords: notes, tips, cautions
    last_updated: March 20, 2016
    summary: "These notes are stored as shortcodes made available through the linksrefs.html include"
    ---

The rest of the file should be conform to the Markdown rules.

After you finished writing your file, you will need to add the permalink as it's done for other files in the `_data/ontowiki_urls.yml` and the `_data/urls.yml`. files **spaces are important in yaml, use exactly the same amount of spaces as the other entries for this part use**

Afterwards you will add your file into the `_data/sidebars/ontowiki_sidebar.yml` were you think it belongs to (Install, Developer, etc.).

If you want to know which exist right now you can look at the files in the `tags/` folder. If you think a new tag would
make this Documentation better you can add them with creating a new file in the this folder and adding the code of another file with the correct header for yours into it. Afterwards you add the tag into the tag sidebar in `_data/sidebars/tags_sidebar.yml`

Then you will need to most likely rebase your fork onto our master branch and afterwards make a pull request

## Miscellaneous

Most other things you might want to do should be doable with knowing how to create and edit files propperly.

The `ontowiki_` for the links is necessary, as our jekyll theme would allow us to put a Documentation for other sites as well into this one (for example rdfauthor or Erfurt).
