import smtplib
import datetime as dt
import pandas
import random

bday_list = pandas.read_csv("birthdays.csv")
new_dict = {(data_row['month'], data_row['day']) : data_row  for (index,data_row) in bday_list.iterrows()}
print(bday_list.iterrows())
now = dt.datetime.now()
today_tuple = (now.month, now.day)

if today_tuple in new_dict:
    birthday_person = new_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as bday_file:
        contents = bday_file.read()
        contents = contents.replace('[NAME]', birthday_person['name'])

    with open("letter_templates/letter.txt", mode='w') as file:
        file.write(contents)




