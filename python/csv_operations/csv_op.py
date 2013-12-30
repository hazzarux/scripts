__author__ = 'yigit'

"""
gmail's contacts csv file has way too much information.
i just need name & e-mail
copy&paste this into mailing solution
"""


import csv
import codecs

csvReader = csv.reader(codecs.open("google.csv",'rU',"utf-16"))
csvWriter = csv.writer(codecs.open("result13.csv",'wb',"utf-16"),delimiter=',')

for row in csvReader:
    name=row[0]
    email=row[28]
    name=name.replace(",","")
    print("name",name)
    print("email",email)
    csvWriter.writerow([name,email])
    print("[+] csv written")