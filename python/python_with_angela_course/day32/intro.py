# We can send emails straight from our python code
# using something called SMTP(simple mail transfer protocol)

# import smtplib

# my_email = 'sarayulanka9@gmail.com'
# my_password = 'Sarayu2010'

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs='kidpythontestcourse@gmail.com', msg='Subject:Hello\n\n Hi!')

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
print(f'The year is {year}. It is the {month}th month. It is the {day}th day.')

day_of_week = now.weekday()
print(day_of_week)


# Practice time:

import random
import smtplib

my_email = 'ewrnmsaerjh@gmail.com'
my_password = 'W3Ir|)###'

with smtplib.SMTP("smtp.gmail.com") as connection:
    weekday = now.weekday()
    if weekday == 0:
        with open('quotes.txt') as quotes:
            quote_list = quotes.readlines()   
            random_quote = random.choice(quote_list)     
            
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs='kidpythontestcourse@gmail.com', msg=f'{random_quote}')
