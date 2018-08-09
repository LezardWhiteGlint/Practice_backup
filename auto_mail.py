import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
msg = "\r\n".join([
  "From: sheldon@r2games.com",
  "To: sheldon@r2games.com",
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])
server.sendmail('sheldon@r2games.com','sheldon@r2games.com',msg)
