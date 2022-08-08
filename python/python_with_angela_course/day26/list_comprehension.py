# List comprehensions are for loops created to generate a new list from an old one in one line
# list comprehension is very popular because it saves a lot of lines and is easier
# to understand

# The syntax for list comprehension is: 
# new_list_name = [(the thing you want to do inside for loop) for variable_name in old_list_name]

# Let's try a list comprehension:
# Let me try getting numbers from the old list squared inside the new list:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squared_numbers = [num ** 2 for num in numbers]

print(squared_numbers)


# Let's try another thing with list comprehension:

names = ['sar', 'shloka', 'sruth', 'adhya', 'mishka']
new_names = [name.upper() for name in names if len(name) >= 5]

print(new_names)


# I was able to save so many lines by doing a list comprehension instead of a for loop
# This method is so much easier and shorter than doing a for loop

# Challenge:
# use range in list comprehension to make a list with each number doubled from 1, 5:

range_numbers = [num*2 for num in range(1,5)]

print(range_numbers)


# Challenge:
# Filter out the even numbers:

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
 
result = [num for num in numbers if num % 2 == 0]
print(result)