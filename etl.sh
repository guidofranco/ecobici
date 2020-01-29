#!/bin/bash
# Comandos que ejecutará el cron job
# La configuración pensada para el cron job es: 0 8-20 * * 1-5
PROJECT_DIR=~/datadev/ecobici/
PYTHON_DIR=~/miniconda3/envs/dataeng/bin/python
(cd $PROJECT_DIR && $PYTHON_DIR etl.py) >> file.log