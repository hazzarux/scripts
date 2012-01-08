#! /usr/bin/python

from BeautifulSoup import BeautifulSoup
import urllib
from pprint import pprint

target = 'http://britneyspears.ac/lyrics.htm'
target = urllib.urlopen(target)
target = target.read()
soup = BeautifulSoup(target)
result_file = open("britney_spears_results.txt",'w')

for elem in soup.findAll('h5','lyrics'):
  links = elem.findAll('a')
  for link in links:
    contents = link.contents
    for content in contents:
      content = content.split()
      content.pop(0)
      content = ' '.join(content)
      if content[0].capitalize() =='I': #I has to be capital cause we capitalized content[0]
        result_file.write(content)
        result_file.write('\n')
