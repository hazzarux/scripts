#!/bin/bash

########################################################
# Copyright 2011 Yigit Ozkan.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
########################################################

# put this script file in home folder & configure to start it at startup
# system -> preferences -> startup applications

# deluge
# run after in the background after 15 seconds
sleep 15 && deluge &
