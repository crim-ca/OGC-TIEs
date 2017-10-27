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
import errno


def print_hello_world(first_name, second_name):

    status_file = open("/status/status.xml",'w+')
    out_file = open("/outputs/out.txt",'w+')

    msg = 'Hello {} and {}'.format(first_name, second_name)
    print msg
    num_sleep = 5
    for i in range(0,num_sleep):
        time.sleep(5)
        status_file.write("Sleep 5 seconds, {0}/{1} \n".format(i,num_sleep))

    out_file.write(msg)

    status_file.close()
    out_file.close()

    return msg


hello_world_args = ['first_name', 'second_name']

def get_wps_input(var_name):
    return os.getenv('WPS_INPUT_{}'.format(var_name.upper()), 'env variable not found')

def pywrapper_app(**kwargs):

    dirs_to_create = ['/status', '/outputs']

    for curr_dir in dirs_to_create:
        if not os.path.exists(curr_dir):
            try:
                os.makedirs(curr_dir)
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

    first_name = get_wps_input('first_name')
    second_name = get_wps_input('second_name')
    msg = print_hello_world(first_name, second_name)


if __name__ == "__main__":
    PARSER = optparse.OptionParser()
    pywrapper_app()
