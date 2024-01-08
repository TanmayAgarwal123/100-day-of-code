from datetime import datetime
import pandas
import random
import smtplib

my_email = "tanmay10agarwal@gmail.com"
password = "bhrp bpxa nnln kegg"

today = datetime.now()
today_tuple = (today.month, today.day)
print(today_tuple)

data=pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        #print(contents)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        print("working")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
        connection.close()