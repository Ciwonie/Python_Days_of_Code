# import smtplib
# import datetime as dt
# import random
#
# MY_EMAIL = "throwthroughthrew@gmail.com"
# PASSWORD = "Meowmeowcat123!"
#
#
# now = dt.datetime.now()
# weekday = now.weekday()
#
# if weekday == 2:
#     with open("quotes.txt") as quotes_file:
#         all_quotes = quotes_file.readlines()
#         quote = random.choice(all_quotes)
#
#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, PASSWORD)
#         connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
#                             msg=f"Subject:Wednesday Motivation\n\n{quote}")

