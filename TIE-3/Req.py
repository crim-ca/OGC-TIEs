#!/usr/bin/env python
# coding:utf-8


class Req(object):

    body = None
    registry_url = None
    dockerim_name = None
    dockerim_version = None
    input_data = {}
    
    def __init__(self,_b, _url, _imname, _ver,_indata):
        self.body = _b
        self.registry_url = _url
        self.dockerim_name = _imname
        self.input_data = _indata
        self.dockerim_version = _ver



