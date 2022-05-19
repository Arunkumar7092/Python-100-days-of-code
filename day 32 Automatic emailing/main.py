import smtplib



with smtplib .SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="durgageetha96.dg@gmail.com", msg="Subject:Hello Durga\n\nContact me if you Don't wish to Lose Everything.")
