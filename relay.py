import time
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#print PID to tempfile
print("Writing relay.py PID to tempfile")
with open("/tmp/relay.py.pid", "w") as temp_file:
    temp_file.write(str(os.getpid()))


while 1:
    print "."


# Sendmail testing...    
#    print("Running relay script. This message is displayed once every 30 seconds.")
#    time.sleep(30)

    
#    try:
#        #send an email from a gmail account
#        mail_content = "Hello World"
#        sender_address = "MSfrigatebird@gmail.com"
#        sender_pass = "frigatebird1010!"
#        receiver_address = "decaplow@microsoft.com"
#
#        #smtp session
#        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
#        session.starttls() #start security
#        session.login(sender_address, sender_pass)
#
#        #setup MIME
#        message = MIMEMultipart()
#        message['From'] = sender_address
#        message['To'] = receiver_address
#        message['Subject'] = "Hello World"
#
#        #body and attachments
#        message.attach(MIMEText(mail_content, 'plain'))
#
#        #prepare
#        text = message.as_string()
#
#        session.sendmail(sender_address, receiver_address, text)
#        session.quit()
#        print('Mail Sent')
#    except:
#        print('Something went wrong sending mail')



