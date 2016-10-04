# mergerfs-tools
Optional tools to help manage data in a mergerfs pool

## mergerfs.rebalance

A tool to rebalance the drives within a pool.

```
$ mergerfs.rebalance --help

usage: mergerfs_rebalance.py [-h] [-l] [--log LOGFILE] [--ping]
                             [--snapraid {drive,file}] [-v]
                             storagePool

Rebalance the drives within a mergerfs storage pool.

positional arguments:
  storagePool           the storage pool mount point

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            list drives with their usage
  --log LOGFILE         log activity to the file
  --ping                ping the drive for 15 seconds to help identify it, if
                        drive has an activity light
  --snapraid {drive,file}
                        run a snapraid sync after each file/drive is
                        rebalanced. Expects snapraid to be installed
  -v, --verbose         verbose mode

```
#### Instructions


#### Example

```
/tmp/files/b: OK
```

#### Automation

