#!/bin/bash
sudo apt install python3
sudo apt install python3-venv
python3 -m venv entorno 
source entorno/bin/activate
pip install -r requirements.txt
entorno/bin/python manage.py runserver