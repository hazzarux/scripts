#personal Python library
import requests
import smtplib

def get_html(url):
	html = requests.get(url, headers={'User-Agent': ''}).text
	return html.encode('utf-8')

def send_mail(gmail_user, gmail_pwd, fromaddr, toaddr, msg):
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(gmail_user,gmail_pwd)
	server.sendmail(fromaddr, toaddr, msg)
	server.close()
	print "email sent"
	return