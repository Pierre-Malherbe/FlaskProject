#!/bin/bash

apt-get install python python-pip git
pip install flask
git clone git@github.com:Pierre-Malherbe/FlaskProject.git

python FlaskProject/test.py

