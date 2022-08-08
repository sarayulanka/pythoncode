# csv data(comma seperated values) are a very common way 
# of representing tabular data or data that is frequently stored in tables, spreadsheets, etc.

# An example of csv data is the file weather_data.csv:
# We are going to do some experiments with csv data so first we have to open our file and 
# put each line as a value in a list:

# import csv

# with open('weather_data.csv', mode='r') as csv_file:
#     data = csv.reader(csv_file)

#     # Next, we have to try and exlude every piece of data except the temperature:
#     temperatures = []
#     for row in data:
#             if row[1] != 'temp':
#                 temperatures.append(int(row[1]))

#     print(temperatures)

     # The method we did above works but what if we have to deal with more complex data files?
    # That is why there is something called the pandas library to help with this

    # The pandas library is super useful and powerful when trying to analyze tabular data
    # so let's try doing the exact same thing but with using the pandas library,
    # which is so much better:

import pandas

data = pandas.read_csv('weather_data.csv')
print(type(data))
temp = data['temp']
print(temp)

# The two main things in panda are the mainframe: the full spreadsheet, chart, or table, 
# and the series: the series is each and every column in the spreadsheet, chart, or table
        
# There are many things you can do with mainframes and series

# Some things that you can do with series is convert them into data structures
# For example, you can convert series into data structures like dictionaries and lists

# let's try converting the temp series to a list and then getting the average temp out of that list:

temp_list = temp.tolist()
print(f'The average temperature is {round(sum(temp_list) / len(temp_list), 0)} degrees celcius.')


# Now, here's a challenge, let's try getting the biggest number in the temp column using the documentation:

print(max(temp_list))

# Now here's a harder challenge, let's try getting the row of the biggest temperature printed:
print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
c2f = lambda c: (c * 1.8) + 32
print(c2f(monday.temp))

