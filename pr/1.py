import smtplib
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'davidvetal09@gmail.com'
smtp_password =  '****************'
from_address = 'davidvetal09@gmail.com'
to_address = '<email_receiver>'
subject = 'Practical work 1'
body = 'Creating a web service for sending emails'
smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
smtp_conn.starttls()
smtp_conn.login(smtp_username, smtp_password)
message = f"From: {from_address}\nTo: {to_address}\nSubject: {subject}\n\n{body}"
smtp_conn.sendmail(from_address, to_address, message)
smtp_conn.quit()
