# Setting up RPi Zero W for touchscreen device development with a HyperPixel screen

## Prerequisites:

- [Etcher](https://etcher.io/)
- [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
- [Python 3 for Windows](https://www.python.org/downloads/)

## Step by step:

### Set up a headless RPi Zero W

Throughout this process, Windows may occasionally pop up warning dialogs saying you have to format the disk before you can use it - *always* ignore these (click Cancel or close)

- Download [Raspbian Stretch (or later) *Lite* image](https://downloads.raspberrypi.org/raspbian_lite_latest) 
- Mount the RPi SD card in your PC
- Open Etcher, select the downloaded Raspbian image and click Flash
- Once the card is flashed and validated, Etcher will automatically eject it
- Remove and re-insert the card
- Open the `boot` partition of the SD card in Explorer
- Create an empty text file called `ssh` (no extension) at the root of the SD card partition
- Create another empty text file called `wpa_supplicant.conf` at the root of the SD card partition
- Open `wpa_supplicant.conf`, add the following (substituting your own Wifi SSID and password) and save the file (if possible, using UNIX line endings):

    country=GB
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1

    network={
        ssid="MyWiFiNetwork"
        psk="password123"
    }

- Eject the SD card, remove it and reinsert into the RPi
- Power up the RPi and wait for it to boot (LED will flicker until it is up and running)
- Find out which IP address your network has assigned to the RPi - easiest way is to look at your router's connection status page, but you can use AngryIP or Fing on a mobile device
- Open PuTTY and enter `pi@192.168.0.123` as the hostname, replacing the IP address with that or your RPi
- Make sure the connection type is set to SSH, then click **Open**
- You should see a password prompt: enter `raspberry` (the default RPi password)
- That's it: you're now logged in to your RPi

### Update the RPi firmware and system packages

- Run `sudo apt-get update`
- Run `sudo apt-get dist-upgrade`
- Run `sudo reboot`

#### Optionally (BEWARE)

- Run `sudo apt-get upgrade` to upgrade *all* packages to the latest versions
- Run `sudo reboot` again

*Be warned!* Doing this currently (on Raspbian Stretch) seems to 'hang' when updating some Perl modules, and I can't currently find a solution.

https://raspberrypi.stackexchange.com/questions/7342/raspberry-pi-apt-get-update-upgrade-on-raspbian-hangs  
https://raspberrypi.stackexchange.com/questions/27819/command-apt-get-upgrade-crashes-raspbian?rq=1
https://www.raspberrypi.org/documentation/raspbian/updating.md

### Install Python dependencies

#### Python 2.X

- Run `sudo apt-get install build-essential python-pip python-imaging python-smbus`
- Run `sudo pip install RPi.GPIO Adafruit-SSD1306 requests evdev`
- Run `sudo raspi-config`
- Choose `5 - Interfacing` and enable I2C kernel module, then exit
- Run `sudo reboot`

#### Python 3.X (TBD)

<!-- - Run `sudo apt-get install python3-pip` -->

## References:

https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage  
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c  
https://github.com/balena-io/etcher/blob/master/CHANGELOG.md  
https://sourceforge.net/projects/win32diskimager/  
https://learn.pimoroni.com/tutorial/sandyj/setting-up-a-headless-pi  
https://play.google.com/store/apps/details?id=com.overlook.android.fing&hl=en_GB&rdid=com.overlook.android.fing  
http://angryip.org/