#!/usr/bin/env bash

wget -q -O - https://apt.mopidy.com/mopidy.gpg | sudo apt-key add - 
&& sudo wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/stretch.list 
&& wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/adafruit-pitft.sh
&& curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/retrogame.sh >retrogame.sh
&& sudo apt-get update && sudo apt-get upgrade && sudo apt-get install python3-dev python3-pip python-dev python-pip python-PIL python-imaging -y
&& pip install Mopidy-Iris
if [$? -eq 0]; then
	echo OK
	sudo python3 ./Installer.py
else
	echo FAIL
fi