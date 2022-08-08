# In our code, we always have bugs or we make errors, right?
# Some types of errors we tend to get frequently are listed below:

# FileNotFound Error:
# with open('daata.txt') as file:
#   # the bug in this code is the daata.txt instead of data.txt

# Key Error:
# dict = {key: value}
# dict['extinct']
# The problem with this code is that the key 'extinct' does not exist in the dict dictionary

# Index Error
# Fruit_list = ['tomato', 'grapes', 'strawberries', 'watermelon', 'banana']
# Fruit_list[5]
# The bug with this code is that there is no element at the index of 5 because the index starts from 0

# Type Error
# string = 'This is a string'
# number = 3
# print(string + number)
# The problem with this code is that you cannot add strings and numbers together


# These are some very common types of errors tom make in programs
# Usually we've used the errors as indicators to tell us when something isn't quite right

# But instead of doing all of this work of testing, finding error, fix error, repeat...
# what if I told you that there is a way to plan for these errors, like a plan B...


# This concept is called catching exceptions in programming

# There are four steps to catching exceptions:

# Try:
# The try block is the part where you put the code that you think will have exceptions/errors

# Except:
# The except block is the place where you put the code that should run if an 
# exception occurs in the try block

# Else:
# The else block is the place where you put the code that should run if the 
# exception doesn't occur in the try block

# Finally:
# The finally block is the place where you put the code that should run 
# regardless of whether there is an exception in the try block or not


# Now let's try some examples:

try:
    # Remember that inside the try block, we keep the code that we think has exceptions in it
    file = open('a_file.txt')
    a_dict = {'key': 'value'}
    print(a_dict['reqi'])
except FileNotFoundError:
    # The cool thing about except is you can create except blocks of code for specific types of errors
    # The except block will carry the code that will run only if the try block has exceptions
        file = open('a_file.txt', 'w')
        file.write('Hello')
except KeyError:
    a_dict['reqi'] = 'weqhqho' 
    print(a_dict['reqi'])
else:
    # The else block will carry the code that will run only if the try block doesn't have exceptions
    file = open('a_file.txt')
    content = file.read()
    print(content)
finally:
    # The finally block will carry the code that will run regardless of what happens
    file.close()