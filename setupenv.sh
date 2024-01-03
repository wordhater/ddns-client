#!/bin/bash

# This script was created to make the setup process easier
virtualenv --python=python3 .venv
source .venv/bin/activate
pip install requests