#!/usr/bin/env bash
BACKEND_PATH=$( cd $(dirname $0) ; pwd -P )
export PYTHONPATH=$BACKEND_PATH
python $BACKEND_PATH/hello_webapp/app.py