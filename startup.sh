#!/bin/bash

sudo apt-get update
sudo apt-get install python3 -y
sudo apt-get install python3-venv -y
sudo apt-get install python3-pip -y


# Test Phase
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt


# pytest goes here
python3 -m pytest tests/test_unit.py --cov=application

# Deploy Phase
python3 create.py
python3 app.py


# Make the installation directory




# Give jenkins user permissions for the installation directory
sudo chown -R jenkins /opt/crud_app


sudo systemctl daemon-reload
sudo systemctl stop crud_app.service
sudo systemctl start crud_app.service