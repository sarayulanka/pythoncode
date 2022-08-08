# Sometimes, when you are working with APIs, you need to use valuable data that you 
# constantly need to keep updating. Of course, because the data you are using from the API is so precious,
# the people who created the API are probably not going to make the data free

# Some of the data though, is free. This is free only for people who are still learning the ropes of 
# how to use APIs. But how do people know when you are getting the data for free and you are not a beginner
# in APIs? Usually, people creating APIs will set up some sort of way to make sure that you don't use more data
# frequently than you are allowed to. This is called API authentication.

# One type of API authentication is called the API key. An api key is when the API provider can track how
# much data you're using from the free API and deny you access if you've gone over the limit.

# Let's try creating a key and using an API:

import requests
import smtplib

link = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = '2c3ec1665e1e99720a1ea3c0fc7ef344'

weather_parameters = {'lat': 39.267471, 'lon': -76.798019, 'appid': api_key, 'exclude': 'current,minutely,daily'}

response = requests.get(link, params=weather_parameters)
data = response.json()
data_slice = data['hourly'][:12]

for hour_data in data_slice:
    hourly_weather = hour_data['weather'][0]['id']
    
    if int(hourly_weather) < 700:
       will_rain = True

if will_rain:
    my_email = 'ewrnmsaerjh@gmail.com'
    my_password = 'W3Ir|)###'

    with smtplib.SMTP("smtp.gmail.com") as connection:
       
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs='sarayulanka9@gmail.com', msg=f'It will rain today so remember to bring an umbrella!')

# We did it! We called an API using a key we created on a weather website.
