#/bin/bash!

#Install dependancies
sudo apt install -y python3 python3-scapy libiperf0 python3-pip
sudo python3 -m pip install requests paho-mqtt iperf3 pymongo
pip3 install paho-mqtt python-etcd
