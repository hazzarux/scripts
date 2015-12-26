import csv, codecs

csvReader = csv.reader(codecs.open("google.csv",'rU'))

for row in csvReader:
    name=u' '.join(row[0]).encode("utf8").strip()
    email=u' '.join(row[1]).encode("utf8").strip()
    name=name.replace(",","")
    print("name",name)
    print("email",email)
    #csvWriter.writerow([name,email])
    #print("[+] csv written")