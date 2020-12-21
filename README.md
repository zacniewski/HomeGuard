# HomeGuard

## Connect to RPi:
  * in console type `ping raspberrypi.local` to get IP of your RPi,
  * for example address of my RPi is 192.168.178.36, your address will be different,
  * more info about getting IP address of RPi [here](https://www.raspberrypi.org/documentation/remote-access/ip-address.md),
  * in console type `ssh pi@192.168.178.36` (write yours IP address, not mine) to connect to your RPi.
  
## Install OpenCV 4
  * for RPi 3 [here](https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/),
  * for RPi 4 [here](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/),
  * or use install_opencv4_prerequisites_for_RPi_4.sh script.
  
## Install necessary software
 * [supervisor](http://supervisord.org/index.html) (process control system), [installation](https://cavelab.dev/wiki/Raspberry_Pi_IoT_setup#Supervisor)
 * [nginx](https://www.raspberrypi.org/documentation/remote-access/web-server/nginx.md) (web server),
 * [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) (application server),   
   install globally via apt and in virtual environment via pip, versions should be the same!
 * [Redis](https://redis.io/) (database, cache and message broker), install via apt.
 
## Create virtual environment and activate it
  * `python3 -m venv myenv`
  * `source my_env/bin/activate`

## Install packages with pip
  * `pip install -r requirements.txt`

## uWSGI
  * install both system-wide and in virtual environment

## Nginx
