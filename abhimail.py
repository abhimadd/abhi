import smtplib
import getpass

myemail=input("your email id : ")
password=getpass.getpass()
recemail=input("reciever's email id : ")

#create SMTP session
s=smtplib.SMTP('smtp.gmail.com',587)

#start TLS for security
s.starttls()

#authentication
s.login(myemail, password)

#message to be sent
message="hi bro.. good ni8"

#sending the mail
s.sendmail(myemail,recemail,message)

#terminating the session
s.quit()