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

## Certbot


## Applying changes without reboot
  ```sudo systemctl restart uwsgi```  and  
  ```sudo systemctl restart nginx```
