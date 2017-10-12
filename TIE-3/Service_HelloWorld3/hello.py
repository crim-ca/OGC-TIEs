#!/usr/bin/env python
# coding:utf-8

"""
Face service module.
"""

# --Standard lib modules------------------------------------------------------
import os
import sys
import threading
import logging
import optparse



def main(**kwargs):

    log = open("/data/log.txt","w")
    log.write("Expecting OGC_INPUT_HWPARAM1, OGC_INPUT_HWPARAM2...")
    p1= ""
    p2= ""
    out=""
    if 'OGC_INPUT_HWPARAM1' in os.environ:
        p1=os.environ["OGC_INPUT_HWPARAM1"]
        print("Srv3 - p1 is {}".format(p1))

    if 'OGC_INPUT_HWPARAM2' in os.environ:
        p2=os.environ["OGC_INPUT_HWPARAM2"]
        print("Srv3 - p2 is {}".format(p2))
        
    log.close()

    print("Hello world - third service")


if __name__ == "__main__":
    PARSER = optparse.OptionParser()
    main()
