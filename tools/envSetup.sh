#!/usr/bin/env bash

# MYSQL支持
apt-get install libmysqlclient-dev python3-dev

# 虚环境安装
sudo pip install virtualenv
sudo pip install virtualenvwrapper
mkdir $HOME/.virtualenvs

# 在~/.bash_profile 增加,然后 source ~/.bash_profile
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

# 新建虚环境
mkvirtualenv --python=/usr/bin/python3.5 --no-site-packages py3.5
mkvirtualenv --python=/usr/bin/python3.5 --no-site-packages newThunneycomb
mkvirtualenv --python=/usr/bin/python2.7 --no-site-packages py2.7
workon newThunneycomb
# workon 虚环境不能用字符，否则uwsgi会有寻址异常


pip install -r requirements.txt
pip install uwsgi
sudo apt-get install uwsgi-core uwsgi-plugin-alarm-curl uwsgi-plugin-alarm-xmpp uwsgi-plugin-curl-cron uwsgi-plugin-emperor-pg uwsgi-plugin-gccgo uwsgi-plugin-geoip uwsgi-plugin-glusterfs uwsgi-plugin-graylog2 uwsgi-plugin-ldap uwsgi-plugin-lua5.1 uwsgi-plugin-lua5.2 uwsgi-plugin-luajit uwsgi-plugin-mono uwsgi-plugin-php uwsgi-plugin-psgi uwsgi-plugin-python uwsgi-plugin-python3 uwsgi-plugin-rack-ruby2.3 uwsgi-plugin-rados uwsgi-plugin-router-access uwsgi-plugin-sqlite3 uwsgi-plugin-v8 uwsgi-plugin-xslt

# nginx
sudo apt-get install nginx