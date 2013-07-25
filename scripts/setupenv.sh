#!/bin/bash
easy_install pip
pip install virtualenvwrapper

source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv prphoto
workon prphoto
pip install -r requirements.txt
