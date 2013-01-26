from ftplib import FTP
import os
import urllib2
import time


'''A lil script that'll copy PROJECTS into shellmix account. :)'''

PROJECTS=['song_tracker']

if os.path.isfile(os.getcwd()+'/ftpsync.py')==False:
  download_time=time.time()
  print "ftpsync doesn't exist"
  ftpsync = urllib2.urlopen('http://ftpsync2d.googlecode.com/files/ftpsync.py')
  output = open('ftpsync.py','wb')
  output.write(ftpsync.read())
  output.close()
  print "ftpsync downloaded in %s seconds" % (time.time()-download_time)

print 'ftpsync is there'


