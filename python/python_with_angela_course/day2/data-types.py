# Data types are about classifying the data that is used in python
# One data type that we learned about are strings
# The data types that we are going to learn today are called string, integer, float, and boolean

# String Data Types:
print("Hello World!")

# Subscript is pulling out a character from a string
# The way to do this is write the string and next to it put square brackets
# Python will always start counting from zero 
# so if you want the first character, you put zero in brackets
# and the second character will be 1 in the brackets and so on
# Examples of subscript:
print("hello world!"[0])
print("hello world!"[1])
print("hello world!"[2])
print("hello world!"[3])
print("hello world!"[4])

# Practice Time:
# make python print out o in "hello"
print("Hello"[4])

# Now it's important to remember that whatever you put in quotes is now a string
# Even if you put numbers in quotes, it is still a string
#  When you add strings it just combines the two strings
# Let's see what happens when we combine two strings that have numbers in them

print("123" + "456")

# As you can see, python just combined the numbers, and did not actually add them
# That is because the numbers are in quotes so python treats them as strings

# Integer Data Types:
# Integers are whole numbers without any decimals or fractions etc.
# To make an integer, all you have to do is type a number and not use quotes
# If you actually want to add the numbers and get a sum,
# you put the two numbers in a print statement with a plus sign
# Example:

print(123 + 456)

# The output will give you an actual sum because python is treating these numbers like numbers
# That is because they aren't in quotes so they aren't treated like strings


# Float Data Types:
# Floats are numbers that can have decimals in them in python
# 3.14159 is a float because it has a decimal point in it
print(3.14159)


# Boolean Data Types:
# Booleans are only two values
True
False
# True and False are the only two values that will count as booleans
# Booleans will not have quotes
# Booleans are used to determine if the program is True or False
# We will be using them a lot in the near future
