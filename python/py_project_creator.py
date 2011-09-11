#!/usr/bin/python2.7


# -*- coding: utf-8 -*-
"""
-- py_project_creator --
Created on Sun Sep 11 18:33:48 2011

@licence: GNU GPL v3+
@author: Yigit Ozkan
"""

import os
from datetime import date
import datetime

def get_dir_path(name):
    home_dir=os.getenv("HOME")
    home_dir = os.getenv("HOME")
    name = home_dir+'/'+name+'/'
    print "directory path is: "+name
    return name
    
def check_create_dir(name):
    if os.path.isdir(name):
        print "directory already exists"
    if not os.path.isdir(name):
        os.mkdir(name)
    print name,'created'
    
def create_readme(folder, name, time):
    filename=folder+"README.md"
    FILE = open(filename,"w")
    FILE.writelines("-- "+name+".py --\nCreated on "+time+"\n@licence: GNU GPL v3+\n@author: Yigit Ozkan")
    FILE.close()
    print "readme created"

def create_src(folder):
    name=folder+"src/"
    if os.path.isdir(name):
        print "directory already exists"
    if not os.path.isdir(name):
        os.mkdir(name)
    print name,'created'
    return name

def create_init(path):
    filename=path+"__init__.py"
    FILE = open(filename,"w")
    FILE.close()
    print "init file created"
    
    
def main():
    project_name=raw_input('Enter project name: ')
    now = datetime.datetime.now()
    creation_time=now.strftime("%a %b %d %H:%M:%S %Y")
    folder = get_dir_path(project_name)
    check_create_dir(folder)
    create_readme(folder,project_name,creation_time)
    src_path=create_src(folder)
    create_init(src_path)
    

if __name__ == '__main__':
    main()
