

import smtplib
server=smtplib.SMTP('smtp.gmail.com',)
server.starttls()
server.login("ikhlaasrasib@gmail.com", "*********")
msg = "......."
server.sendmail("ikhlaasrasib@gnmail.com", "vk9339135@gmail.com", msg)
server.quit()