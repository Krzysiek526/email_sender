import smtplib

sender = '<my email>' 
password = '<password>'
receivers = ['<email>']

message = """
From: John <my email>
To: <email when i recevie text>
MIME-Version: 1.0
Content-Type: text/html
Subject: Test E-Mail
<some text>
"""

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(sender, password) #  Exception here
try:
    server.sendmail(sender, receivers, message)
    print("Message sent successfully")
except:
    print("Failed to send message")
server.quit()