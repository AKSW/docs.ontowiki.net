## Virtuoso backup

Possibly, the easiest and most complete way to do backups is with the automated backup functionality built into Virtuoso conductor. This is documented at the [[Virtouso site|http://docs.openlinksw.com/virtuoso/backup.html]], and presumes that you are using the Virtuoso back-end. Conductor can schedule incremental backups, and manages everything on it's own.

Please note that this strategy backs up the whole Virtuoso database, and so this strategy is not well suited for rolling back the database to a previous state if you use it for other things than OntoWiki, or if you have multiple instances of OntoWiki. For backup purposes it should work great, though.

Other alternatives are detailed below.

## Dumping RDF data
The first thing needed for a backup is the RDF data.

### Option 1: Using the [[Command Line Interface|https://github.com/AKSW/owcli/]]
Make sure the CLI is [[setup correctly|https://github.com/AKSW/owcli/blob/master/README.md]]
Note: We actually use this script to back up [[http://data.lod2.eu]]

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

### Option 2: Export directly from the store
If the store can do SPARQL and has a command line, this should always work:

```
Construct {?s ?p ?o} {?s ?p ?o}
```

Depending on the store there are more options:

#### Virtuoso

  * [[http://docs.openlinksw.com/virtuoso/backup.html]] - Using this backup strategy will also backup the history and query cache
  
  * [[http://code.google.com/p/aksw-commons/wiki/Virtuoso_ISQL]]
  
  * [[http://www.openlinksw.com/uda/wiki/main//Main/VirtDumpLoadRdfGraphs]]

## Backup

One way to back up the files generated above is to make a Mercurial Repository and then do hourly commits. Mercurial is file based, so you can create it locally.

### Setup Mercurial

```
mkdir /var/backups/$BACKUPDIR
cd /var/backups/$BACKUPDIR
hg init .
```

### Commit

```
hg add * 2>/dev/null
hg commit . -m "..." -q
```

### Add a cronjob (Mentioned for completeness)

```
crontab mybackupscript.sh
```
