import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'John'
email['to'] = '<receiver email>'
email['subject'] = 'Title'

email.set_content('text')

#with smtplib.SMTP(host='smpt.gmail.com', port=587) as smtp:
with smtplib.SMTP('smtp.gmail.com:587') as smtp: #if they are same errors check the code above
	smtp.ehlo()
	smtp.starttls()
	smtp.login('<my email>', '<password>')
	smtp.send_message(email)
	print('Email sent')
