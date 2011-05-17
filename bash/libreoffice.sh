#!/bin/sh

########################################################
# Copyright 2011 Yigit Ozkan.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
########################################################

sudo apt-get purge "openoffice*"

sudo add-apt-repository ppa:libreoffice/ppa
sudo apt-get update

sudo apt-get install libreoffice
sudo apt-get install libreoffice-gnome

sudo apt-get install aspell aspell-en dictionaries-common hunspell-en-us myspell-en-us
