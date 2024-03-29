echo "Prerequisities for OpenCV 4 on Raspberry Pi 4" &&
sudo apt-get -y purge wolfram-engine &&
sudo apt-get -y purge libreoffice* &&
sudo apt-get -y clean &&
sudo apt-get -y autoremove &&
sudo apt-get -y update &&
sudo apt-get -y upgrade &&
sudo apt-get -y install build-essential cmake pkg-config &&
sudo apt-get -y install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev &&
sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev &&
sudo apt-get -y install libxvidcore-dev libx264-dev &&
sudo apt-get -y install libfontconfig1-dev libcairo2-dev &&
sudo apt-get -y install libgdk-pixbuf2.0-dev libpango1.0-dev &&
sudo apt-get -y install libgtk2.0-dev libgtk-3-dev &&
sudo apt-get -y install libatlas-base-dev gfortran &&
sudo apt-get -y install libhdf5-dev libhdf5-serial-dev libhdf5-103
sudo apt-get -y install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5 &&
sudo apt-get -y install python3-dev &&
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py &&
sudo rm -rf ~/.cache/pip &&
rm get-pip.py
