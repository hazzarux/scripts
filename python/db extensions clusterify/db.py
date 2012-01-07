#! /usr/bin/env python


#little script so we can add database extensions to .gitignore in clusterify project :)


f = open('db_extensions','r')
lines = f.readlines()


for line in lines:
  words = line.split()
  for word in words[:1]:
    print word
    with open('extensions.txt','a') as result_file:
      result_file.write('*.')
      result_file.write(word)
      result_file.write('\n')
  
