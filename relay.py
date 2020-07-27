import time
import os
import dronekit_sitl
from dronekit import connect, VehicleMode


###Initialization process
##
##Print PID to tempfile
#
print("Writing relay.py PID to tempfile")
try:
    with open("/tmp/relay.py.pid", "w") as temp_file:
        temp_file.write(str(os.getpid()))
except:
    print("PID could not be written.\nThis feature will not work in Windows.")

##Set-up logging
#
print('Starting logfile')
am_logging = True
log_file = None
try:
    log_file = open("~/tmp/relay_log_" + time.time() + ".txt", "w")
    print("Opened log file")
except:
    #log file not working
    am_logging = False
    print("Log file couldn't be opened.\nThis feature will not work in Windows.")

#Write to a logfile
def log_line(text):
    print(str(text))
    if am_logging:
        log_file.write(str(text))

##Start simulator
#
log_line("Start simulator (SITL)")
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()


# Connect to the Vehicle.
log_line("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, wait_ready=True)

# Get some vehicle attributes (state)
log_line("Vehicle attribute values:")
log_line(" GPS: %s" % vehicle.gps_0)
log_line(" Battery: %s" % vehicle.battery)
log_line(" Last Heartbeat: %s" % vehicle.last_heartbeat)
log_line(" Is Armable?: %s" % vehicle.is_armable)
log_line(" System status: %s" % vehicle.system_status.state)
log_line(" Mode: %s" % vehicle.mode.name)    # settable

#Finished
log_line('Initialized!')

# Close vehicle object before exiting script
vehicle.close()

# Shut down simulator
sitl.stop()
print("Completed")

# ###Main loop
# ##
# while 1:
#     log_line(".")
#     time.sleep(1)






# Sendmail testing...

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

#    print("Running relay script. This message is displayed once every 30 seconds.")
#    time.sleep(30)


#    try:
#        #send an email from a gmail account
#        mail_content = "Hello World"
#        sender_address = "..."
#        sender_pass = "..."
#        receiver_address = "..."
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
