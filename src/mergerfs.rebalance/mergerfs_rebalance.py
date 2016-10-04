#!/usr/bin/env python
#
# mergerfs.rebalance
#
""" Rebalance drives within a mergerfs storage pool """
import argparse


def cmdLineArgs():
    """Setup the commandline argument parser"""
    argsParser = argparse.ArgumentParser(description="""Rebalance the drives within
                                         a mergerfs storage pool.""",
                                         add_help=True)
    argsParser.add_argument(dest="storagePool",
                            action="store",
                            help="the storage pool mount point")
    argsParser.add_argument("-l", "--list",
                            dest="drive_list",
                            action="store_true",
                            help="list drives with their usage")
    argsParser.add_argument("--log",
                            dest="logFile",
                            action="store",
                            help="log activity to the file")
    argsParser.add_argument("--ping",
                            dest="ping",
                            action="store_true",
                            help="""ping the drive for 15 seconds to help
                                 identify it, if drive has an activity light""")
    argsParser.add_argument("--snapraid",
                            dest="snapraid",
                            action="store",
                            choices={"file", "drive"},
                            help="""run a snapraid sync after each file/drive is rebalanced.
                                 Expects snapraid to be installed""")
    argsParser.add_argument("-v", "--verbose",
                            dest="verbose",
                            action="store_true",
                            help="verbose mode")

    return argsParser.parse_args()


if __name__ == "__main__":

    line_args = cmdLineArgs()
    print(line_args.drive_list)
    print(line_args.snapraid)
    print(line_args.verbose)
