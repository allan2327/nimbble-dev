#!/usr/bin/env bash

apt-get update > /dev/null

echo "Installing python3 and virtualenv"
apt-get install -y python3  > /dev/null
apt-get install -y python-virtualenv > /dev/null

echo "creating virtual environment with python 3"
cd /

virtualenv -p /usr/bin/python3 nimbble-dev

echo "activating virtual environment"
source nimbble-dev/bin/activate

echo "Installing requirements"
cd nimbble-dev
pip install -r requirements.txt