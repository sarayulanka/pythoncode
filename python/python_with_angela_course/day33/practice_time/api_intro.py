# Application Programming Interfaces(API) are a set of commands, functions, protocols and objects
# that programmers can use to create software or interact with an external system.

# The API is kinda like a barrier between your program and external systems
# What you are trying to do is send a request to the external system following all of the rules of the API

# The API endpoints are basically the location of the the data that you want to get from a particular
# external system. For example, if you want to get money from a bank, you need to know where the bank is and
# how to get to it. That is called an API endpoint.

# To get data from an external system, you can't just go and get the data, 
# you have to make a request online for the data. That is called an API request.

# Let's try sending an API request to an external system.
# To do this, I have to import a package called requests:
import requests
from datetime import datetime

# # Next, I will have to call get(). This will help us get the data that we want
#  from the external system we choose:
response = requests.get(url='http://api.open-notify.org/iss-now.json')
data = response.json()
print(data)

# That's all there is to it, we have officially created our first API request. 
# However, when we run this, we don't get a JSON format of the data that we saw we should get
# so is it an error?
# What does the output we got mean?

# If the output is 1XX(100), it means Here You Go
# If the output is 2XX(200), it means Hold on
# If the output is 3XX(300), it means Go Away
# If the output is 4XX(400), it means You Screwed Up
# Lastly, if the output is 5XX(500), it means The server screwed up

# Working with APIS that have parameters:

MY_LAT = 39.045753
MY_LONG = -76.641273


parameters = {'lat': MY_LAT, 'lng': MY_LONG, 'formatted': 0}

response2 = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response2.raise_for_status()


data2 = response2.json()
sunrise = data2['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data2['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)