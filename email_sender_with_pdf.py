import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text()) #same html file
email = EmailMessage()

email['from'] = 'John'
email['to'] = '<receiver email>'
email['subject'] = 'Title'


email.set_content(html.substitute({'name': 'TinTin'}), 'html') 
#in html we have $name so we replace with the TinTin

#with smtplib.SMTP(host='smpt.gmail.com',port='587') as smtp:
with smtplib.SMTP('smtp.gmail.com:587') as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('<my email>', '<password>') 
	smtp.send_message(email)
	print('Email sent')
