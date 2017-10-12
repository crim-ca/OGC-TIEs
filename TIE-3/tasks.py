#!/usr/bin/env python
# coding:utf-8


# --Standard lib modules------------------------------------------------------
import os
import sys
import threading
import logging
import optparse
import Req
# --Project specific----------------------------------------------------------
#from VestaService.request import Request

# --3rd party modules----------------------------------------------------------
from celery import Celery
#from celery import current_task
#from celery.utils.log import get_task_logger

# -- Configuration -----------------------------------------------------------
#PROCESS_NAME = 'tie3'
APP = Celery('tasks') #PROCESS_NAME)


def create_composefile(req):
    content = "version: \"2\" \n\
services:\n\
\n\
 hw1:\n\
    image: {}:{}\n\
    env_file:\n\
    - ./h1.env\n\
    #restart: always\n\
    environment:\n\
      C_FORCE_ROOT: \"True\"\n\
    volumes:\n\
      - ./data1:/data\n\
    working_dir: /data\n\
\n\
# For performance issues.\n\
networks:\n\
  default:\n\
    driver: bridge\n\
    driver_opts:\n\
      com.docker.network.driver.mtu: 1450\n".format(req.dockerim_name,req.dockerim_version)

    fl=open('docker-compose.yml','w')
    fl.write(content)
    fl.close()
    print("Launching compose with {}".format(req.dockerim_name))
    retcode = os.system('docker-compose up --exit-code-from hw1')
    print("retcode={}".format(retcode))
    
    fl = open('h1.env',"w")
    if isinstance(req.input_data,dict):
        for key,val in req.input_data.iteritems():
            print("data: var={} value={}".format(key,val)) 
	    fl.write('OGC_INPUT_{} = {}\n'.format(key,val))



@APP.task #(name=PROCESS_NAME)
def process(req):
#    logger = get_task_logger('Service_VideoSummary')
#
#    if not current_task:
#        logger.warning(u"Could not get handle on current task instance")
#    else:
#        logger.debug(u"Got handle on current task instance")

#    # The video filename is available here : request.document
#    request = Request(body, current_task)
#    request.process_version = __version__

    # Check that submitted document exists locally
#    if not os.path.exists(request.document.local_path):
#        logger.error(u"VideoSummary lib didn't find the given video : '{0}'"
#                     .format(request.document.local_path))
#        raise InvalidDocumentPath("File not found : {0}"
#                                  .format(request.document.local_path))

    # Listeners will know that we are starting processing
 #   logger.debug(u"Set progress to 0% in celery")
 #   request.set_progress(0)
#    logger.debug(u"Set progress done in celery")

    # The ThreadManager class will:
    # 1 - Launch the processing on a worker thread
    # 2 - Synchronize the progress between the progress thread and the main one
    # 3 - Forward the updated progress to celery from the main thread
#    thread_manager = ThreadManager(request)

    # The process function can either return the annotation or re-raise any
    # exceptions that could occur in the processing thread
#    annotations = thread_manager.process()

#    request.store_annotations(annotations)

    # conf = 0
    # if len(annotations) > 0:
    #     conf = sum([annot['fConfidence'] for annot in annotations]) \
    #         / len(annotations)
    #
    # return {'confidence': conf, 'annotations': annotations}
    
    if isinstance(req,Req.Req):
        print("image name is {}".format(req.dockerim_name)) 
    else:
        print("unknown request")
    
    create_composefile(req)

    return []


