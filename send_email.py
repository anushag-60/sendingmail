#import smtplib and all necessary components of email package
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Specify the sender’s credentials and receiver’s email addresses:
sender = 'anudemouser1@gmail.com'
sender_password = 'demouser1'
receiver = 'anudemouser2@gmail.com'

#This is the subject line
subject = 'Sending Mail through Python'

#Setup MIMEMultipart for each email address (if we don't do this, the emails will concatenate on each email sent)
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = subject

#attach both Plain text and Html versions
messageHTML = '<p>Visit <a href="https://www.whitehatjr.com/">Whitehat Jr</a> for some great <span style="color: #496dd0">Coding Classes!</span><p>'
messagePlain = 'Inspire Kids today to Become Creators of Tomorrow'
msg.attach(MIMEText(messagePlain,'plain'))
msg.attach(MIMEText(messageHTML,'html'))

# Setup the attachment
filename='whj.jpg'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)
msg.attach(part)

# You now need to convert the MIMEMultipart object to a string to send
text = msg.as_string()

#connect to the server
server = smtplib.SMTP('smtp.gmail.com',587)

#secure email transmission
server.starttls()
#login with email and password
server.login(sender,sender_password)

#send mail
server.sendmail(sender,receiver,text)

#logout from email server
server.quit()
