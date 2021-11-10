echo "Updating and upgrading ......" &&
sudo apt-get -y update &&
sudo apt-get upgrade &&
sudo apt-get dist-upgrade &&
echo "Cleaning Up ......" &&
sudo apt-get -f install &&
sudo apt-get -y autoremove &&
sudo apt-get -y autoclean &&
sudo apt-get -y clean && 
echo "Checking snaps ......" &&
date >> /home/pi/Scripts/test.txt &&
echo "Done!!!!"
