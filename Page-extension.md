The Page Extension shows static HTML on OntoWiki and has to be manually installed.

## Installation (requires access to AKSW db0 Server, please improve this if you know how to install it better)

Copy the page folder from fts:.

    scp -r root@db0:/var/www/fts.publicdata.eu/extensions/page . 

Add the following to `/var/www/myontowiki/config.ini`:

    index.default.controller = "page"
    index.default.action = "startpage"

## Configuration
Edit `myontowiki/extensions/page/page/startpage.phtml`.
