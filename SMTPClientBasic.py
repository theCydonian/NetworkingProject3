#SMTPClientBasic.py
from smtplib import *
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = str(input('Please input the mail server:'))

#set account infos
address = str(input('Please input your email address:'))
password = str(input('Please input your email password:'))
sendTo = str(input('Please input the address that you are sending to:'))

#set message
msg = MIMEMultipart()
msg['From'] = address
msg['To'] = sendTo
msg['Subject'] = str(input('Please input the subject of your email:'))

body = str(input('Please input the content of your email:'))
msg.attach(MIMEText(body, 'plain'))

#server setup
server = SMTP(mailserver)
server.starttls()
server.login(address, password)

#convert to string
text = msg.as_string()

#send message
server.sendmail(address, sendTo, text)
server.quit()