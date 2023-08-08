import smtplib
import datetime as dt
import random

my_email = 'usa@gmail.com'
password = 'abc1234'

# print current date time
now = dt.datetime.now()
weekday = now.weekday()
# for monday
if weekday == 0:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    # connection creation
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # tls transport layer security this is way to secure our connection to our email server
        connection.starttls()
        connection.login(user=my_email, password=password)
        # Subject is used to add subject in mail \n\n  after that will be email content
        connection.sendmail(from_addr=my_email, to_addrs='india@gmail.com',
                            msg=f'Subject:Welcome to Python\n\n {quote}')

# print(dt.datetime.now())
#
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.weekday())
#
# date_of_birth = dt.datetime(year=1989, month=2, day=2, hour=20, minute=0, second=0)
# print(date_of_birth)
