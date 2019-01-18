#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Script needs to run as root!"
  exit
fi

apt install libusb-1.0.0 swig qt5-qmake qt5-default g++ python-dev
