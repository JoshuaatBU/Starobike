#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir="/home/josh/Documents/SD/21-29-Starobike/GNU/NewModule/gr-seniordesign/python"
export GR_CONF_CONTROLPORT_ON=False
export PATH="/home/josh/Documents/SD/21-29-Starobike/GNU/NewModule/gr-seniordesign/build/python":$PATH
export LD_LIBRARY_PATH="":$LD_LIBRARY_PATH
export PYTHONPATH=/home/josh/Documents/SD/21-29-Starobike/GNU/NewModule/gr-seniordesign/build/swig:$PYTHONPATH
/usr/bin/python3 /home/josh/Documents/SD/21-29-Starobike/GNU/NewModule/gr-seniordesign/python/qa_serialsource_b.py 
