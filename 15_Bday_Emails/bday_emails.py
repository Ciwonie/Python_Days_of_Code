from datetime import datetime
import smtplib
import pandas
import random

TOTAL_LETTERS = 3
NAME_PLACEHOLDER = "[NAME]"
MY_EMAIL = "throwthroughthrew@gmail.com"
PASSWORD = "Meowmeowcat123!"

# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,TOTAL_LETTERS)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace(NAME_PLACEHOLDER, birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )




