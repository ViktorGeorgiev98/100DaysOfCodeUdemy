##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

today = dt.datetime.now()
today_tuple = (today.month, today.day)

# read birthday csv
data = pandas.read_csv(
    "./day_32_email_smtp_and_datetime_module/birthday_wish/birthdays.csv"
)
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}


if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"./day_32_email_smtp_and_datetime_module/birthday_wish/letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        replaced_contents = contents.replace("[NAME]", birthday_person["name"])

    # send email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login("111@gmail.com", "111")
        connection.sendmail(
            from_addr="111@gmail.com",
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{replaced_contents}",
        )
