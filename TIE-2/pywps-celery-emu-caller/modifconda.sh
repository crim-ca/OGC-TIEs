#!/bin/sh
source /opt/conda/bin/activate emu
pip uninstall pywps -y
cd pywps
python setup.py install