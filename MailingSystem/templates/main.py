import smtplib 
from email.mime.text import MIMEText
from email.message import EmailMessage
import imghdr
from email.mime.multipart import MIMEMultipart

username="harsh-cse19@satyug.edu.in"
password="nbvcfd765"

msg=EmailMessage()
msg['Subject']="hello world"
msg['From']=username
msg['To']="harsharora0703@gmail.com"
msg.set_content('How about dinner')


with open(r"D:\Web Automation\MailingSystem\templates\applicant-tracking-system-138k.png","rb") as f:
    file_data=f.read()
    file_type=imghdr.what(f.name)
    file_name=f.name
msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(username,password)
    smtp.send_message(msg)
