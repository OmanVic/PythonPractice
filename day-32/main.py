import smtplib
email_id = "workingdummydev@yahoomail.com"
password = "developertest1997"
connection = smtplib.SMTP("smtp.mail.yahoo.com")
connection.starttls()
connection.login(user=email_id, password=password)
connection.sendmail(from_addr=email_id, to_addrs="workingdummydev@gmail.com", msg="Hello")
connection.quit()