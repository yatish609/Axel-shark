# Axel-Shark

Axel-Shark is a packet sniffer tool created using PyQt5 and Scapy in Python.

Libraries used: 
> PyQt5

> Scapy

> Psutil

Based on Python 3.8.2 and compiled using python's own virtualenv.

To install dependencies:

~~~
sudo pip install PyQt5 scapy psutil
~~~

To run Axel-Shark:

~~~
sudo python3 axelshark.py
~~~

NOTE: You need to run the command as root(sudo) because the modules used such as netifaces and scapy
require root priveleges to run and sniff packets.
