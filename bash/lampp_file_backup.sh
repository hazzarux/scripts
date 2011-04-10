#!/bin/sh

# creates a backup of the htdocs directory
# ----------------------------------------


# variables
original = "/opt/lampp/htdocs/"
backup = "/media/sda2/"
# variables--

sudo apt-get install rsync
rsync -aHk  $original $backup
