##################### Hard Starting Project ######################

from datetime import datetime
from os import name

import pandas
import random
import smtplib

MY_EMAIL = 'ewrnmsaerjh@gmail.com'
MY_PASSWORD = 'W3Ir|)###'

today = datetime.now()
today_tuple = (today.month, today.day)

birthday_file = pandas.read_csv('birthdays.csv')
birthday_dict = {(birthday_file_row.month, birthday_file_row.day): birthday_file_row for index, birthday_file_row in birthday_file.iterrows()}

if today_tuple in birthday_dict:
    template_list = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
    file_path = f'letter_templates/{random.choice(template_list)}'

    with open(file_path) as letter_file:
        content = letter_file.read()
        new_content = content.replace('[NAME]', birthday_dict[today_tuple]['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs= birthday_dict[today_tuple]['email'], msg=new_content)

    


    
# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



