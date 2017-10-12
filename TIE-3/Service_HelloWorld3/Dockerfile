FROM centos:7
MAINTAINER marc.lalonde@crim.ca

#Environment variables
ENV SERVICE_DIR /tmp/service-HW
ENV PYTHON_MODULE Service_HelloWorld

#Prepare required files
RUN mkdir $SERVICE_DIR
RUN mkdir /data
COPY ./ $SERVICE_DIR/
   
#Setup the working dir and config
#COPY celeryconfig.py $WORKING_DIR/celeryconfig.py

CMD python $SERVICE_DIR/hello.py
