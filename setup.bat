@echo off
color 5

title Installing Requirements
cd /d "%~dp0"
echo Installing Requirements...
py -m pip install -r requirements.txt

cd tools
title Checking for updates
echo Checking for updates...
python update.py
