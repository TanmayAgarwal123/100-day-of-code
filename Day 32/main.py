# import smtplib

# my_email = "tanmay10agarwal@gmail.com"
# password = "bhrp bpxa nnln kegg" #app password in data.txt

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls() #to make the connection secure
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email, 
#     to_addrs="tanmay.agarwal2021@vitstudent.ac.in",
#     msg="Subject:Happy Birthday\n\nThis is the body of my email."
#     )
# connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2002, month=10, day=10)
