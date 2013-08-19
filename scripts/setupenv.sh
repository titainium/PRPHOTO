#!/bin/bash
apt-get install -y python-setuptools
apt-get install -y  libffi-dev
easy_install pip
pip install virtualenvwrapper

source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv prphoto
workon prphoto
pip install -r requirements.txt
