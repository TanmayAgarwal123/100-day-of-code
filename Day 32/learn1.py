import smtplib
my_email = "tanmay10agarwal@gmail.com"
password = "bhrp bpxa nnln kegg" #app password in data.txt

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls() #to make the connection secure
connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email, 
#     to_addrs="tanmay.agarwal2021@vitstudent.ac.in",
#     msg="Subject:Happy Birthday\n\nThis is the body of my email."
#     )
#connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

#date_of_birth = dt.datetime(year=2002, month=10, day=10)
import random
if day_of_week == 0:
    with open("Day 32/quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="tanmay.agarwal2021@vitstudent.ac.in",
            msg="Subject:Happy Birthday\n\nThis is the body of my email."
            )
        connection.close()
else:
    print("no")