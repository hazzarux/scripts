#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

HOST = "localhost"
USERNAME = 'root'
DBNAME = 'cdcol'
DEST_FOLDER = r'C:\Users\xoxo\Desktop\db_backup/'


SQLNAME = DEST_FOLDER+DBNAME+".sql"

command = 'mysqldump.exe --host={HOST} -u {USERNAME} {DBNAME} > {SQLNAME}'.format(**locals())
    
print "Running command.."

Popen(command, shell=True, stdout=PIPE, stderr=PIPE)

print "SQL file saved to",SQLNAME