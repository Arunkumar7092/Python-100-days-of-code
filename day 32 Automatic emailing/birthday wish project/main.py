from datetime import datetime
import pandas
import random
import smtplib

my_email = "pythonhackerr@gmail.com"
password = "aidni007"

today_month = datetime.today().month
today_day = datetime.today().day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")

birthdays_list = []
for (index, row) in data.iterrows():
    birthdays_dict = {}
    birthdays_dict[(row.month, row.day)] = row
    birthdays_list.append(birthdays_dict)
for each in range(len(birthdays_list)):
    for key, value in birthdays_list[each]:
        current_birthday = (key, value)
        if today == current_birthday:
            birthday_person = birthdays_list[each][today]
            print(birthday_person["email"])
            file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
            with open(file_path) as file:
                content = file.read()
                content = content.replace("[NAME]", birthday_person["name"])
                print(content)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                                    msg=f"Subject:Happy Birthday !\n\n{content}")







