# In the past file, we learnt about list comprehension
# In this file, we are going to learn about a similar concept but with dictionaries

# Dictionary comprehension is basically the same concept as list comprehension execpt 
# instead of using a for loop for lists, you are using a for loop for dictionaries
#  and there are curly brackets in the syntax

# Let's try some exercises:

# First exercise:
# You are going to use Dictionary Comprehension to create a dictionary called weather_f 
# that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, 
    "Saturday": 22, "Sunday": 24
}

weather_f = {key: (value * 9/5) + 32 for key, value in weather_c.items()}
print(weather_f)


# Some general questions people have is that can you still do if conditions in dictionary comprehensions?
# The answer is yes
# The only difference between dictionary comprehension and list comprehension is that you 
# use curly for dicts and square for lists and that the for loop syntx is slightly different

# The concept and the execution of both comprehensions are mostly the same


# Now let's try another exercise!
# exercise 2:
# Find out from a dictionary of students who passed (50/100 or more)

import random


names = ['claire', 'sophie', 'alexia', 'charlie', 'brandon', 'kyle']
student_names = {name: random.randint(1, 100) for name in names}
print(student_names)

passed_students = {key:value for key, value in student_names.items() if value >= 50}
print(passed_students)


student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    print(f'{key}: {value}')

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
   print(f'{index}: {row}')
   # access indexes and rows