import smtplib

my_email = "tanmay10agarwal@gmail.com"
password = "bhrp bpxa nnln kegg" #app password in data.txt

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls() #to make the connection secure
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email, 
    to_addrs="tanmay.agarwal2021@vitstudent.ac.in",
    msg="Subject:Hello\n\nThis is the body of my email."
    )
connection.close()
