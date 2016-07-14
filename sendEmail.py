import smtplib


server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

username = #enter email address here
password = #enter password here
msg = #enter message here
recipient = #enter recipient here

server.login(username, password)
server.sendmail(username, recipient, msg)
