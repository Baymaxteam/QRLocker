# QRLocker

##OS 

Dev: x64 Ubuntu 14.04

Target: Rpi3 Ubuntu 16.01

##Software Version
python 3.5.2


##Install
### python3.5
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get -y install python3.5  python3.5-dev python3-pip
### pyQt5
sudo apt-get install python3.5-gdbm
sudo pip3 install pyqt5

#### for developing. QtDesigner and pyuic5
sudo apt-get install qttools5-dev-tools 
sudo apt-get install pyqt5-dev-tools

#### run QtDesigner
$ /usr/lib/x86_64-linux-gnu/qt5/bin/designer

###python QR decoder 
sudo pip3 install pillow pyqrcode libzbar-dev zbarlight


