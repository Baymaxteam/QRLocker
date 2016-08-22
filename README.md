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

## RPi3 Wallpaper

#####ref: https://www.maketecheasier.com/nitrogen-a-background-setter-for-lightweight-desktop-manager/

sudo apt-get install nitrogen

nitrogen ~/wallpaper

###### another choise: Fbsetbg



## remotelty start GUI program

1. need auto login RPi 

###### ref:https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=127042

sudo vim /etc/systemd/system/getty@tty1.service.d/autologin.conf

paste:

[Service]

ExecStart=

ExecStart=-/sbin/agetty --autologin pi --noclear %I 38400 linux

save and exit..

sudo systemctl enable getty@tty1.service

2. start x11 server

need keyboard... 

startx -- -nocursor

3. run programs

DISPLAY=:0 python3 <your program>



## Touch Screen
###### office website: http://www.eleduino.com/7-0-Inch-1024x600-Pixel-IPS-Hdmi-Input-Capacitive-Touch-Screen-Support-Raspberry-pi-Banana-Pi-Pro-Be-p10533.html

modify /boot/config.txt：

hdmi_group=2

hdmi_mode=1

hdmi_mode=87

hdmi_cvt 1024 600 60 6 0 0 0

max_usb_current=1


Driver: https://github.com/derekhe/waveshare-7inch-touchscreen-driver

## screen - keep processes running after ending ssh session
###Installation:
sudo apt-get install screen

###Using:
$ screen

do things...

key in "Ctrl + a" "d" (detach)

you will see the output like "[detached from 5326.pts-0.seal-home]" 

and then you can close the ssh connection


### Reconnection:

$ screen -r



## Troubleshooting
1. Python: locale.Error: unsupported locale setting

Solution: 

a. export LC_ALL=C

b. export LC_ALL="en_US.UTF-8"
   export LC_CTYPE="en_US.UTF-8"
   sudo dpkg-reconfigure locales


## QT ui to py
pyuic5 -o mainwindow_nonnameing.py mainwindow_nonnameing.ui 

pyuic5 -o qrcode_nonnameing.py qrcode_nonnameing.ui
 
