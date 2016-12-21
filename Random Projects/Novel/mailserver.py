import smtplib

fromaddress = "kenshin421@yahoo.com"
toaddress = "brandonklo94@gmail.com"
msg = """testing"""


server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
server.ehlo()
server.starttls()
server.login("kenshin421","********")
server.sendmail(fromaddress, toaddress, msg)
print "Your mail has been sent"

                      



