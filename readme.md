# Readme

# Introduction:
FrigateBirdPiRelay is a program intended to allow a Raspberry Pi computer to serve as a communication link between an Azure server and a Navio2 unit on a drone. This program is designed to run on a Raspberry Pi connected to a Sixfab 4g/LTE HAT with a Twilio Programmable Wireless SIM installed and an Emlid Navio2 HAT. Modifications will be necessary for other configurations.


# Setup Instructions:
1. Download Emlid's latest [Navio2 Raspberry Pi img file] and follow [instructions] to flash the img and connect the board to WiFi
2. Assemble the 4G/LTE HAT and the Navio2 HAT to the Raspberry Pi
SSH into the Raspberry Pi
3. Run the following commands to install FrigatebirdPiRelay:

       wget https://raw.githubusercontent.com/decamun/FrigatebirdPiRelay/master/install/installPiRelay.sh
       sudo chmod +x installPiRelay.sh
       sudo ./installPiRelay.sh

4. Follow instructions and provide input as necessary.
  * When prompted to choose your Sixfab Sheild, respond with *'2'*
  * If asked whether your Kernel is up to date, respond with *'n'*
  * When prompted to enter you carrier APN, enter *'wireless.twilio.com'*
  * When prompted to enter your port name, enter *'ttyUSB3'*
  * When asked if you would like to activate autoconnect/reconnect service at RPi boot up, enter *'Y'*

If all steps are followed correctly and installation succeeds, your Raspberry Pi will be properly configured to connect to the internet via LTE and run FrigatebirdPiRelay at boot.

# Usage:


To stop FrigateBirdPiRelay run:

    sudo /etc/init.d/relay stop

To start FrigateBirdPiRelay run:

    sudo /etc/init.d/relay start

FrigateBirdPiRelay logfiles can be found at **/tmp/relay.py.*start_timestamp*.log**
