# Readme

# Introduction:
FrigateBirdPiRelay is a program intended to allow a Raspberry Pi computer to serve as a communication link between an Azure server and a Navio2 unit on a drone. This program is designed to run on a Raspberry Pi connected to a [Sixfab 4g/LTE](https://sixfab.com/product/raspberry-pi-base-hat-3g-4g-lte-minipcie-cards/) HAT with a [Twilio Programmable Wireless](https://www.twilio.com/wireless) SIM installed and an [Emlid Navio2 HAT](https://navio2.emlid.com/). Modifications will be necessary for other configurations.


# Setup Instructions:
1. Follow [instructions](https://docs.emlid.com/navio2/common/ardupilot/configuring-raspberry-pi/) to flash the latest Emlid Navio2 img and connect the board to WiFi
2. Assemble the 4G/LTE HAT and the Navio2 HAT to the Raspberry Pi
3. SSH into the Raspberry Pi
4. Run the following commands to install FrigatebirdPiRelay:

       wget https://raw.githubusercontent.com/decamun/FrigatebirdPiRelay/master/install/installPiRelay.sh
       sudo chmod +x installPiRelay.sh
       sudo ./installPiRelay.sh

5. Follow instructions and provide input as necessary.
  * When prompted to choose your Sixfab Sheild, respond with *'2'*
  * If asked whether your Kernel is up to date, respond with *'n'*
  * When prompted to enter you carrier APN, enter *'wireless.twilio.com'*
  * When prompted to enter your port name, enter *'ttyUSB3'*
  * When asked if you would like to activate autoconnect/reconnect service at RPi boot up, enter *'Y'*

If all steps are followed correctly and installation succeeds, your Raspberry Pi will be properly configured to connect to the internet via LTE and run FrigatebirdPiRelay at boot.

# Usage:

To start/stop/restart Arduplane run:
    sudo systemctl *start/stop/restart* arduplane

To stop FrigateBirdPiRelay run:

    sudo /etc/init.d/relay stop

To start FrigateBirdPiRelay run:

    sudo /etc/init.d/relay start

FrigateBirdPiRelay logfiles can be found at **/tmp/relay.py.*start_timestamp*.log**
