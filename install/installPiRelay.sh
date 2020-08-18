#!/bin/bash

#Install or update relay.py

#Update and Upgrade
echo "Updating and Upgrading...\n\n"
apt-get update
apt-get upgrade

#enable Arduplane to run on boot
echo "Enabling aruplane to start on boot"
systemctl enable arduplane

#Clone FrigatebirdPiRelay from Github
echo "Cloning FrigatebirdPiRelay from Github...\n\n"
git clone https://github.com/decamun/FrigatebirdPiRelay /home/pi/FrigatebirdPiRelay/

#Install FrigatebirdPiRelay autorun
echo "Installing FrigatebirdPiRelay autorun...\n\n"
cp /home/pi/FrigatebirdPiRelay/install/relay /tmp/init.d
chmod +x /tmp/init.d/relay
/usr/sbin/update-rc.d relay defaults

#Install dependencies
echo "Installing dependencies."
echo "User input will be required...\n\n"
apt-get install screen python-wxgtk3.0 python-matplotlib python-opencv python-numpy libxml2-dev libxslt-dev rpi-update

#Install LTE hat drivers
echo "Installing LTE hat drivers."
echo "User input will be required...\n\n"
wget https://raw.githubusercontent.com/sixfab/Sixfab_PPP_Installer/master/ppp_installer/install.sh
chmod +x install.sh
./install.sh #system will reboot after install.sh runs
