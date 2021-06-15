from smtplib import SMTP
import datetime as dt

from constants import EMAIL, PASS


def send_mail(receiver, message):
    try:
        with SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(user=EMAIL, password=PASS)
            smtp.sendmail(from_addr=EMAIL, to_addrs=receiver, msg=message)
    except Exception as e:
        print(f"SMTP message sending failed: {e}")


def check_bdays():
    try:
        with open('birthdays.csv', 'r') as f:
            bdays = [tuple(record.strip().split(',')) for record in f.readlines()[1:]]
    except Exception as e:
        print(f"Error reading file: {e}")
    for day in bdays:
        if dt.date.today().strftime("%Y-%m-%d")[5:] == day[2][5:]:
            'here'
            receiver = day[1]
            msg = f"Happy Birthday, {day[0]}!"
            send_mail(receiver=receiver, message=msg)


check_bdays()
