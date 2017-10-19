#!/bin/sh
source /opt/conda/bin/activate emu
cd /opt/birdhouse/src
pip install ./emu
celery -A pywps.processing.celery_joblauncher worker --loglevel=info