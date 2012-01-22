#! /usr/bin/env bash


########################################################
# Copyright 2011 Yigit Ozkan.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
########################################################

sudo apt-get install git-core git-gui git-doc

cd ~/.ssh
mkdir key_backup
cp id_rsa* key_backup
rm id_rsa*

ssh-keygen -t rsa -C "yigitozkan2804@gmail.com"

git config --global user.name "Yigit Ozkan"
git config --global user.email "yigitozkan2804@gmail.com"

git config --global color.diff auto
git config --global color.status auto
git config --global color.branch auto

cat id_rsa.pub

echo "Done"
