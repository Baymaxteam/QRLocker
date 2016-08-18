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
sudo pip3 install PyQt5

##### on Raspberry
sudo apt-get install python3-pyqt5

###### for GUI
sudo apt-get install xorg openbox

### for developing. QtDesigner and pyuic5
sudo apt-get install qttools5-dev-tools 
sudo apt-get install pyqt5-dev-tools

#### run QtDesigner
$ /usr/lib/x86_64-linux-gnu/qt5/bin/designer


###python QR decoder 
sudo pip3 install pillow pyqrcode libzbar-dev zbarlight

### Pygame  
sudo apt-get install mercurial 

hg clone https://bitbucket.org/pygame/pygame

cd pygame

sudo apt-get install libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libfreetype6-dev

sudo apt-get install libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev

sudo apt-get install python3-dev 

sudo pip3 install numpy

python3 setup.py build 

sudo python3 setup.py install

## RPi3 GPIO
sudo apt-get install python3-rpi.gpio

## RPi3 Chinese
sudo locale-gen zh_TW zh_TW.UTF-8
sudo apt-get install fonts-noto-cjk
sudo fc-cache -fv
reboot

## Troubleshooting
1. Python: locale.Error: unsupported locale setting
Solution: 

a. export LC_ALL=C

b. export LC_ALL="en_US.UTF-8"
   export LC_CTYPE="en_US.UTF-8"
   sudo dpkg-reconfigure locales

