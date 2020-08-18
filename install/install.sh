#!/bin/bash

#Install or update relay.py

#Clone FrigatebirdPiRelay from Github
echo "Cloning FrigatebirdPiRelay from Github..."
mkdir /home/pi/testInstall
git clone https://github.com/decamun/FrigatebirdPiRelay /home/pi/testInstall

#Install FrigatebirdPiRelay autorun
echo "Installing FrigatebirdPiRelay autorun..."
cp /home/pi/testInstall/FrigatebirdPiRelay/install/relay /tmp/init.d
chmod +x /tmp/init.d/relay
update-rc.d /tmp/init.d/relay defaults

#Install dependencies
echo "Installing dependencies."
echo "User input will be required..."
apt-get install screen python-wxgtk3.0 python-matplotlib python-opencv python-numpy libxml2-dev libxslt-dev rpi-update

#Install LTE hat drivers
echo "Installing LTE hat drivers."
echo "User input will be required..."
wget https://raw.githubusercontent.com/sixfab/Sixfab_PPP_Installer/master/ppp_installer/install.sh
chmod +x install.sh
./install.sh
rm -rf install.sh

#Reboot after installation
echo "Installation complete!"
echo "Press enter to reboot..."
read;
reboot
