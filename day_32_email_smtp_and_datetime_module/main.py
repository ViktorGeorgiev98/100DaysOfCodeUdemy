import smtplib


# my_email = "1111"
# # # create new smtp object => we need to specify provider (smtp information)
# # connection = smtplib.SMTP("smtp.mail.yahoo.com")
# # # transport layer security, this will encrypt the message so no one else can read it
# # connection.starttls()
# # # login
# # connection.login(user=my_email, password="neshtositam1234!!??")
# # # send email
# # connection.sendmail(
# #     from_addr=my_email,
# #     to_addrs="viktor_georgiev98@abv.bg",
# #     msg="Subject: Hello\n\nThis is coding test",
# # )
# # # close connection
# # connection.close()
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     try:
#         connection.starttls()
#         connection.login(user=my_email, password="")
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="1111",
#             msg="Subject: Hello\n\nThis is coding test",
#         )
#     except:
#         print("Failure")
#     else:
#         print("Email send")


# ----------------------------------- working with dates ------------------------
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
date_of_birth = dt.datetime(year=1998, month=12, day=11, hour=1)
print(date_of_birth)
