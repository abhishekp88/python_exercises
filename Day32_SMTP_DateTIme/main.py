import smtplib

my_email = 'usa@gmail.com'
password = 'abc1234'
# connection creation
with smtplib.SMTP("smtp.gmail.com") as connection:
# tls transport layer security this is way to secure our connection to our email server
    connection.starttls()
    connection.login(user=my_email, password=password)
# Subject is used to add subject in mail
    connection.sendmail(from_addr=my_email, to_addrs='india@gmail.com',
                    msg='Subject:Welcome to Python\n\n this is email body')
# connection.close()