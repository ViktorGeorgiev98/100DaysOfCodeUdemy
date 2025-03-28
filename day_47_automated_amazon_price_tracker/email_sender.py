import smtplib


# will not use environment variables. I have created the methods and they work. If I want to use them, I will need to replace dummy data with real one
class Mail_Sender:
    def __init__(self):
        self.my_email = "test111"
        self.password = "111"
        self.to_address = "test111"
        self.port = 587
        self.smtp_connection = "smtp.gmail.com"

    def send_email(self, price, url):
        with smtplib.SMTP(self.smtp_connection, self.port) as connection:
            try:
                connection.starttls()
                connection.login(user=self.my_email, password=self.password)
                connection.sendmail(
                    from_addr=self.my_email,
                    to_addrs=self.to_address,
                    msg=f"Subject: Amazon Price alert for instant pot\n\nThe price of the pot is {price}.\nYou can check the product in this url => {url}",
                )
            except:
                print("Email was not sent, please check")
            else:
                print("Email was sent")
