#!/usr/bin/env bash

echo ""
echo "apt-get update"
echo ""
apt-get update

echo ""
echo "Python utils"
echo ""
apt-get install -y python3 python3-setuptools python-dev libpq-dev
apt-get build-dep -y python-psycopg2

echo ""
echo "nodejs"
echo ""
curl -sL https://deb.nodesource.com/setup | sudo bash -
apt-get -y install build-essential
apt-get -y install nodejs

npm install -g grunt-cli

echo ""
echo "apt-get cleanup"
echo ""
apt-get clean

echo ""
echo "pip, ipython and virtualenv"
echo ""
easy_install3 pip
pip3 install virtualenv
pip3 install virtualenvwrapper

echo ""
echo "Configuring .bashrc"
echo ""
cat <<EOF >> /home/vagrant/.bashrc

export WORKON_HOME=/home/vagrant/.virtualenvs
export PROJECT_HOME=/home/vagrant/dev
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'
source /usr/local/bin/virtualenvwrapper.sh

mkvirtualenv nimbble-dev
cd /nimbble-dev
npm install

EOF
