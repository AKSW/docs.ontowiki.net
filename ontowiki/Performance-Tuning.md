---
title: Performance-Tuning
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /ontowiki_Performance-Tuning/
editme_path: ontowiki/Performance-Tuning.md
---
There is a host of settings that can be used for the purpose of tuning the performance of a Virtuoso database server and OntoWiki in general. Below is a short discussion of some of them.

## GNU/Linux system performance

If running Virtuoso on GNU/Linux some general system parameters might be adjusted in order to boost performance. Some important parmameters are listed below.

### vm.swappiness

This setting controls how aggressively the kernel swaps out unused memory blocks to disk. On many systems this setting will greatly influence the performance of Virtuoso.

Please see the [Virtuoso Wiki](http://virtuoso.openlinksw.com/dataspace/doc/dav/wiki/Main/VirtRDFPerformanceTuning#"swappiness") and e.g. [this blogpost](http://unixfoo.blogspot.no/2007/11/linux-performance-tuning.html) for more information.

The following might be a good recommendation:

```shell
# /sbin/sysctl -w vm.swappiness=10
# echo vm.swappiness=10 >> /etc/sysctl.conf
```

## Settings in ```virtuoso.ini```

Settings for the Virtuoso server are generally done in the file ```virtuoso.ini```. Note that settings in this file overrides settings done via the 'Virtuoso Conductor' web interface. Some settings of interest are discussed below. Please see [this article](http://docs.openlinksw.com/virtuoso/rdfperformancetuning.html), among other things.

### SPARQL endpoint performance

Most notably the settings discussed [here](http://virtuoso.openlinksw.com/dataspace/doc/dav/wiki/Main/VirtSPARQLEndpointProtection) affect the SPARQL endpoint performance.

### General Virtuoso RDF performance

The Virtuoso RDF performande is discussed [here](http://virtuoso.openlinksw.com/dataspace/doc/dav/wiki/Main/VirtRDFPerformanceTuning) and [here](http://docs.openlinksw.com/virtuoso/rdfperformancetuning.html).

These articles deserve prudent reading, and the most prominent settings should be outlined herein.