import smtplib
import datetime as dt
import random


# email sending class
class Motivation_Email_Sender:
    def __init__(self):
        self.my_email = "111@gmail.com"
        self.password = "111"
        self.to_address = "111@abv.bg"
        self.port = 587
        self.smtp_connection = "smtp.gmail.com"
        self.get_random_quote()
        self.msg = f"Subject:Motivation\n\n{self.quote}"

    def send_motivational_email(self):
        with smtplib.SMTP(self.smtp_connection, self.port) as connection:
            try:
                connection.starttls()
                connection.login(user=self.my_email, password=self.password)
                connection.sendmail(
                    from_addr=self.my_email, to_addrs=self.to_address, msg=self.msg
                )
            except:
                print("Email was not sent, please check")
            else:
                print("Email was sent")

    def get_random_quote(self):
        # read data
        with open("./day_32_email_smtp_and_datetime_module/quotes.txt", "r") as quotes:
            quotes_data = quotes.readlines()
            quote_for_today = random.choice(quotes_data)
            self.quote = quote_for_today


# set date time
date_today = dt.datetime.now().weekday()
email_sender = Motivation_Email_Sender()
if date_today == 2:
    # send email
    email_sender.send_motivational_email()
