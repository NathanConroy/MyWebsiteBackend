#!/bin/bash
# This runs on the production server: fetches new code,
# Installs needed packages, and restarts the server.

echo "Rebuilding in $PWD ..."
touch rebuild

echo "pulling code from main branch"
git pull origin main

echo "Install packages"
pip install --upgrade -r requirements.txt

echo "Going to reboot the webserver"
API_TOKEN=$API_TOKEN pa_reload_webapp.py nathanconroydev.pythonanywhere.com

# go back to root project dir
cd $PROJ_DIR
touch reboot
echo "Finished rebuild."
