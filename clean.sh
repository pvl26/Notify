#!/bin/bash
sudo systemctl reset-failed    #  daca serviciul a dat fail

sudo systemctl stop notifyapp    

sudo rm /etc/systemd/system/notifyapp.service 

sudo rm /usr/local/lib/notifyapp/service_source.py

sudo rmdir /usr/local/lib/notifyapp/