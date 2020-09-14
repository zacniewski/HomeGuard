# HomeGuard

## Connect to RPi:
  * in console type `ping raspberrypi.local` to get IP of your RPi,
  * for example address of my RPi is 192.168.178.36, your address will be different,
  * more info about getting IP address of RPi [here](https://www.raspberrypi.org/documentation/remote-access/ip-address.md),
  * in console type `ssh pi@192.168.178.36` (write yours IP address, not mine) to connect to your RPi.
  
## Install OpenCV 4
  * for RPi 3 [here](https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/),
  * for RPi 4 [here](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/).
  
## Install necessary software
 * supervisor (process control system),
 * nginx (web server),
 * uWSGI (application server),
 * Redis (database, cache and message broker)
 
## Create virtual environment and activate it
  * `python3 -m venv my_env`
  * `source my_env/bin/activate`

## Install packages with pip
  * `pip install -r requirements.txt`

## uWSGI
  * install both system-wide and in virtual environment

## Nginx
