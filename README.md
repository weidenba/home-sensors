# home-sensors
Providing sensor data on the web using a raspberry pi.

## install

```sh
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv git nginx
git clone https://github.com/weidenba/home-sensors.git
cd home-sensors/src
sudo cp systemd/homesensors.service /etc/systemd/system/
sudo ln -s /home/pi/home-sensors/src/nginx/homesensors.site /etc/nginx/sites-enabled/
python3 -m venv homesensorsenv
source homesensorsenv/bin/activate
pip3 install wheel
pip3 install uwsgi flask 
```
