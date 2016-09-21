# mergerfs-tools
Optional tools to help manage data in a mergerfs pool

## mergerfs.rebalance

A tool to rebalance the drives within a pool.

```
$ mergerfs.rebalance --help
usage: mergerfs.rebalance [-h] [--help]
                          [-l] [--list]
                          [--snapraid {file,drive}]
                          storagepool

A tool to rebalance the files within a storagepool so the drive have equal remaining percentages.

positional arguments:

optional arguments:
  -h, --help show this help message and exit
  -l, --list list the drives in the pool with their current usage
  --snapraid {file,drive} do a snapraid sync when each file/drive has completed it's rebalance

```
#### Instructions


#### Example

```
/tmp/files/b: OK
```

#### Automation

