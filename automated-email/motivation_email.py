from info import *
import smtplib
import datetime
from random import choice

yahoo_server = "smtp.mail.yahoo.com"
gmail_server = "smtp.gmail.com"
# credentials imported from info
from_mail = FROM
to_mail = TO
password = PW
# from_mail = TO
# to_mail = FROM
# password = PW2


def send_email(today="Monday"):
    message = motivation_message(today)
    if message is not None:
        motivation_email = f"Subject: {today} Motivation\n\n{message}"
        with smtplib.SMTP(gmail_server) as connection:
            connection.starttls()
            connection.login(user=from_mail, password=password)
            connection.sendmail(from_addr=from_mail, to_addrs=to_mail,
                                msg=motivation_email)


def motivation_message(today="Monday"):
    date = datetime.datetime.now()
    day = date.weekday()  # integer passed to a day-of-the-week dictionary to check if today parameter is the actual day
    print(day)
    if DAY_DICT[day] == today:  # dictionary imported from info
        with open("quotes.txt", "r") as file:
            quotes = file.readlines()

        motivation = choice(quotes)
    else:
        motivation = None
        print("Sorry, today is not the day for a motivation message.")

    return motivation


if __name__ == '__main__':
    send_email(today="Tuesday")
