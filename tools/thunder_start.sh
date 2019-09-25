#!/usr/bin/env bash
# -*- coding: utf-8 -*-

echo "Find current work space..."
cd ~/webapp/current/
sleep 1
echo ""
echo "Start Thunneycomb Service..."
ps -eaf | grep thunder | grep uwsgi | awk '{print $2}' | xargs kill -9
sleep 2
uwsgi -i uwsgi_py.ini &
echo "Thunndycomb Started."
echo ""

# su - thunderbee -s /home/thunderbee/bin/thunder_start.sh