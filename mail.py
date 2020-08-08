import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user=""
email_send=""
password=''
subject='hello'

msg=MIMEMultipart()
msg['from']=email_user
msg['To']=email_send
msg['subject']=subject

body='hi sending email for testing'
msg.attach(MIMEText(body,'plain'))

filename='temp.txt'
attachement=open(filename,'rb')

part=MIMEBase('application','octate-stream')

part.set_payload((attachement).read())
encoders.encode_base64(part)

#add payload header with filename

part.add_header('Content-Decompostion','attachement',filename=filename)
msg.attach(part)
text=msg.as_string()
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()#to enable security
server.login(email_user,password)
server.sendmail(email_user,email_send,text)
print('Email Sent SuccessFully')
server.quit()

