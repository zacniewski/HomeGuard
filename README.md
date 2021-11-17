# HomeGuard

## Connect to RPi:
  * in console type `ping raspberrypi.local` to get IP of your RPi,
  * for example address of my RPi is 192.168.178.36, your address will be different,
  * more info about getting IP address of RPi [here](https://www.raspberrypi.org/documentation/remote-access/ip-address.md),
  * in console type `ssh pi@raspberrypi.local` to connect to your RPi.
  
## Install OpenCV 4
  * for RPi 3 [here](https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/),
  * for RPi 4 [here](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/),
  * or use install_opencv4_prerequisites_for_RPi_4.sh script.
  
## Install necessary software
 * [supervisor](http://supervisord.org/index.html) (process control system), [installation](https://cavelab.dev/wiki/Raspberry_Pi_IoT_setup#Supervisor)
 * [nginx](https://www.raspberrypi.org/documentation/remote-access/web-server/nginx.md) (web server), install globally via apt,  
 * [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) (application server),   
   install globally via apt and in virtual environment via pip, versions should be the same!
 * [Redis](https://redis.io/) (database, cache and message broker), install via apt.
 
## Create virtual environment and activate it
  * `python3 -m venv myenv`
  * `source my_env/bin/activate`

## Install packages with pip
  * `pip install -r requirements.txt`

## uWSGI
  * install both system-wide (sudo -H pip3 install uwsgi) and in virtual environment (pip install uwsgi),  
  * copy (with sudo) 'homeguard.ini' file to /etc/uwsgi/sites/  
  * check logs with ```sudo journalctl -u uwsgi```
  * I uninstalled uWSGI globally (only left this one in virtualenv) and changed path to uwsgi executable in uwsgi.service

## systemd
  * copy (with sudo) 'uwsgi.service' file to /etc/systemd/system/  

## Nginx
  * copy (with sudo) 'homeguard.conf' file to /etc/nginx/sites-available/
  * create symlink (with sudo) to aforementioned file in /etc/nginx/sites-enabled/
  * add default_server in listen section
  * remove default files in 'sites-available' and 'sites-enabled' folders  

If this all goes well, you can enable both of the services to start automatically at boot by typing:

    sudo systemctl enable nginx
    sudo systemctl enable uwsgi
You can find many useful hints [here](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-16-04).  

## Self-signed certificate
  * useful information from [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu-18-04),

## Applying changes without reboot
  ```sudo systemctl restart uwsgi```  and  
  ```sudo systemctl restart nginx```

## Install OpenCV 4
  * follow [these](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/) steps of PyImageSearch creator,
  * April 2021, OpenCV 4.5.2 is installed in HomeGuard system,
  * in [this](https://www.pyimagesearch.com/2018/08/15/how-to-install-opencv-4-on-ubuntu/) article, way to install OpenCV 4 on Ubuntu is presented,
  the only thing to correct is the path to cv2***.so file, which will be symlinked later. The correct path is presented under the first link.
  * compile OpenCV with flags listed in 'opencv-452-flags-cmake.txt'    

## Permissions to use camera in production mode
  * changing ```sudo chmod 666 /dev/video0/``` (temporary permission to check if code works)
  * add ```www-data``` user to 'video'
  * changing owner to pi:video in 'uwsgi.service'

## Frames in template
  * on RPi 4 Logitech, Inc. C922 Pro Stream Webcam displays image in 640 x 480 format
  * on my laptop webcam displays image in 2304 x 1536 format

## bc2835-v4l2 drivers
  * add line 'bcm2835-v4l2' to /etc/modules and restart

## udev rules
  * I created udev rule: SUBSYSTEM=="video0", GROUP="video", MODE="0660" in file /etc/udev/rules.d/10-webcam.rules to check access to USB camera.  

## rpi-update
  * I did 'sudo rpi-update' and kernel changed from 5.10.17 to 5.10.36 (22 May 2021),
  * kernel changed to 5.10.78 (10 Now 2021).

## New camera system in Raspberry Pi OS
  * [News](https://www.raspberrypi.com/news/bullseye-camera-system/) from 17th November 2021.
