import info
import datetime as dt
import smtplib
from pandas import read_csv
from random import randint
from email.mime.text import MIMEText

FILE = "birthdays.csv"
SERVER = "smtp.gmail.com"
FROM = info.FROM
PW = info.PW2


def birthday_list(file):
    birthdays = read_csv(file)
    today = dt.datetime.now()
    day = today.day
    month = today.month
    birthdays_index = {row.get("name"): row.get("email") for i, row in birthdays.iterrows()
                       if (row.month == month) and (row.day == day)}

    return birthdays_index


def send_birthday_email(birthdays_index):
    if birthdays_index:
        for name, email in birthdays_index.items():
            with open(f"letter_templates/letter_{randint(1, 3)}.txt", "r") as letter:
                text = letter.read()
                bd_text = text.replace("[NAME]", name.capitalize())

            bd_msg = MIMEText(bd_text)
            bd_msg['Subject'] = "Happy Birthday!"
            bd_msg['From'] = f"Me <{FROM}>"
            bd_msg['To'] = f"{name}<{email}>"

            send_email(email, bd_msg.as_string())
            print(f"Birthday email sent to {name} at {email}")

    else:
        print("No emails were sent")


def send_email(recipient, message):
    with smtplib.SMTP(SERVER) as connection:
        connection.starttls()
        connection.login(user=FROM, password=info.PW)
        connection.sendmail(from_addr=FROM,
                            to_addrs=recipient,
                            msg=message)


if __name__ == '__main__':
    send_birthday_email(birthday_list(FILE))
