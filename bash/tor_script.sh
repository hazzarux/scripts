#!/bin/bash

########################################################
# Copyright 2011 Yigit Ozkan.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
########################################################

echo "deb http://deb.torproject.org/torproject.org experimental-lucid main" | sudo tee -a /etc/apt/sources.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 886DDD89
sudo apt-get update 
sudo apt-get install tor privoxy
sudo echo "forward-socks5 / 127.0.0.1:9050 ." >>/etc/privoxy/config
sudo /etc/init.d/tor restart
sudo /etc/init.d/privoxy restart
