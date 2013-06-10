There is a host of settings that can be used for the purpose of tuning the performance of a Virtuoso database server. Below is a short discussion of some of them.

# GNU/Linux system performance

If running Virtuoso on GNU/Linux some general system parameters might be adjusted in order to boost performance. Some important parmameters are listed below.

## vm.swappiness

This setting controls how aggressively the kernel swaps out unused memory blocks to disk. On many systems this setting will greatly influence the performance of Virtuoso.

Please see the [Virtuoso Wiki](http://virtuoso.openlinksw.com/dataspace/doc/dav/wiki/Main/VirtRDFPerformanceTuning#"swappiness") and e.g. [this blogpost](http://unixfoo.blogspot.no/2007/11/linux-performance-tuning.html) for more information.

The following might be a good recommendation:

```shell
# /sbin/sysctl -w vm.swappiness=10
# echo vm.swappiness=10 >> /etc/sysctl.conf
```