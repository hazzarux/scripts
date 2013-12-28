__author__ = 'yigit'

import os

f=open("brussels.txt","w")

emails = 'DATA'

array = emails.split(",")
array2 = []

for email in array:
    if email[0]==" ":
        email = email[1:]
    email = email.replace('<','')
    email=email.replace('>','')
    first = email.find('"')
    second = email.find('"',first+1)
    email=email[second+2:]
    print(email)
    f.write(email)
    f.write('\n')
    array2.append(email)

print(array2)