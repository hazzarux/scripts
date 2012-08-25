#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

DBNAME = 'cdcol'
USERNAME = 'root'
DEST_FOLDER = r'C:\Users\xoxo\Desktop\db_backup/'

SQLNAME = DEST_FOLDER+DBNAME+".sql"

command = 'mysqldump.exe -u {USERNAME} {DBNAME} > {SQLNAME}'.format(**locals())
    
print "Running command.."

Popen(command, shell=True, stdout=PIPE, stderr=PIPE)

print "SQL file saved to",SQLNAME