---
title: Backup-your-data
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_Backup-your-data/
---
# Virtuoso backup

Possibly, the easiest and most complete way to do backups is with the automated backup functionality built into Virtuoso conductor. 

 - Documented at the [Virtuoso site](http://docs.openlinksw.com/virtuoso/backup.html)

 - Presumes that you are using the Virtuoso back-end

 - Conductor can schedule incremental backups, and manages everything on it's own

 - The history and query cache will also be backed up

Please note that this strategy backs up the whole Virtuoso database. As such, it is not well suited for rolling back the database to a previous state if you use it for other things than OntoWiki, or if you have multiple instances of OntoWiki. For backup purposes it should work great, though.

Other alternatives are detailed below.

# Dumping RDF data
The first thing needed for a backup is the RDF data.

## Option 1: Using the [Command Line Interface](https://github.com/AKSW/owcli/)
Make sure the CLI is [setup correctly](https://github.com/AKSW/owcli/blob/master/README.md)
Note: We actually use this script to back up <http://data.lod2.eu> **dead link**

Backing up with owcli is limited to the memory resources of the php-cli process so for huge models, direct backend backup should be used.
```
    BACKUPDIR=/var/backups/data.lod2.eu
    ONTOWIKIURL=data.lod2.eu
    cd $BACKUPDIR
    
    #iterate all models in OntoWiki
    for model in `owcli -w $ONTOWIKIURL -l`
    do
        #the filename here is using a hash over the graphname
        filename=`echo "$model" | md5sum | cut -d " " -f 1`
        #extract the rdf data from the ontowiki
        owcli -w $ONTOWIKIURL -m "$model" -e model:export >$filename.rdf
    done

```

## Option 2: Export directly from the store
If the store can do SPARQL and has a command line, this should always work:

```
Construct {?s ?p ?o} {?s ?p ?o}
```

Depending on the store there are more options:

### Virtuoso

  * <http://docs.openlinksw.com/virtuoso/backup.html> - Using this backup strategy will also backup the history and query cache
  
  * <http://code.google.com/p/aksw-commons/wiki/Virtuoso_ISQL>
  
  * <http://www.openlinksw.com/uda/wiki/main//Main/VirtDumpLoadRdfGraphs>
