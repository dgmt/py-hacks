#!/usr/bin/env bash

sudo apt-get update
sudo apt-get -y install --only-upgrade python

# install python
sudo apt-get -y install git python-dev python-pip

# install requirements
cd /code/src
# pip install -r requirements.txt
pip install pymongo
pip install requests
pip install requests[security]
pip install ujson
pip install python-telegram-bot