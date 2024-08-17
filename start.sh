#!/bin/bash

virtualenv --python=python3 .venv
source .venv/bin/activate
pip install requests
python3 main.py