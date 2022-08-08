# Now let's talk about something that is basically one of the most important things
# to learn in python which will be used very frequently in python programs: lists
# Lists are like containers except instead of only containing one piece of data,
# they contain groups of data that connect in some sort of way
# Lists can contain any data type like strings, floats, and integers
# Let's try creating a list right now!

letters = ["a", "b", "c", "d", 'e', "f"]

# Now lists might look like they have no pattern or order but,
# the way you type in the values into a list is the order that the list maintains
# the order will not be lost so later you can access the list in the same order you put it in.

# Earlier, we learned how to pull out characters in a string and print them
# We can do the same thing to elements in a list
# Let's try it!

print(letters[2])

# When I printed this out, we got the third character in the list, c
# It's important to remember that python always starts counting from zero so,
# if you were to say give me the first value in the list, python would give you the second
# You know how to access the beginning of the list you do 0, 1, 2, 3, and so forth?
# Well there is an easy way to access the end of the list and that is using negative numbers
# To access the last value of the list, you can use -1.
# For the second-to-last value of the list you can use -2 etc.
# This gives you an easier way of accessing the last elements/values in lists
# Let's try it!

print(letters[-1])
print(letters[-4])

# Now, we've been learning how to pull out some elements in a list using a piece of code
# You can also replace elements with different elements using very similar blocks of code
# Let's try it!

letters[-1] = "G"

print(letters)

# using this piece of code, I changed f to g in my list
# This piece of code can come in handy and is very important to know
# This is called changing elements using the index
# The index are the numbers we are putting in the square brackets
# to show which elements we're talking about


# Now let's learn how to add elements to a list
# To add elements to a list, we have to use a function called append
# Let's try adding an element to our list using append:

instruments = ["piano", "cello", "viola"]
instruments.append("violin")

print(instruments)

# We successfully added violin, a new element to the list using the append function
# Now, append can only add one element at a time to a list,
# but what if I need to add a whole group of elements to a list quickly?
# The extend function can do that!
# Let's try it!

instruments.extend(["Trumpet", "saxaphone", "flute", "clarinet"])
print(instruments)

# Now there are much more functions but trying to memorize all of those functions would be unreasonable
# And that's why we have documentations and google


# Practice Time!

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

name_amount = len(names)

print(f"{names[random.randint(0, name_amount - 1)]} is going to buy the meal today!")

# Now let's talk about one of the most common errors to be aware about: index errors
# index errors simply means that the index you put inside the brackets does not exist in the list
# For example, in my instruments list, if I were to say print(instruments[8]),
# I would get an index error because my list doesn't contain an element that has an index of 8


# Now, we have worked with simple lists containing different data types
# But what if I wanted to work with a list containing lists
# Let's try that and see what happens!

fruits = ["strawberries", "nectarines", "apples", "cherries", "pears"]
vegetables = ["tomatoes", "potatoes", "spinach", "kale", "celery"]
dirty_dozen = [fruits, vegetables]

# Now dirty_dozen is a list of two lists and that's called a nested list

# Practice Time!

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = int(position[0])
row = int(position[1])

if row == 1:
  row1[column - 1] = "X"
elif row == 2:
  row2[column - 1] = "X"
else:
  row3[column - 1] = "X"

print(map)