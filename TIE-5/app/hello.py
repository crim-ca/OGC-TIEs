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
import time


def print_hello_world(first_name, second_name):
    msg = 'Hello {} and {}'.format(first_name, second_name)
    print msg
    print 'sleep for some time'
    time.sleep(10)
    return msg

hello_world_args = ['first_name', 'second_name']



def get_wps_input(var_name):
    return os.getenv('WPS_INPUT_{}'.format(var_name.upper()), 'env variable not found')

def pywrapper_app(**kwargs):

    log = open("/data/log.txt","w")
    log.write("Starting pywrapper_app for print_hello_world:")
    
    first_name = get_wps_input('first_name')
    second_name = get_wps_input('second_name')

    msg = print_hello_world(first_name, second_name)
    log.write(msg)

    log.close()



if __name__ == "__main__":
    PARSER = optparse.OptionParser()
    pywrapper_app()
