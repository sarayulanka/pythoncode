# We've learned about the print function and how to use it
# And we've briefly covered len
# We are going to talk about len more to fully understand the concept
# and then we might learn more about other functions

# Len is a function specifically for finding how many characters/elements are in something
# But len will give a type error when you try putting floats or integers
# Let's go back to an old program we were asked to do

name_length = len(input("What is your name?  "))
# print("Your name is " + name_length + " characters.")

# You cannot concatenate/add integers with strings because that will give an error
# So how do we fix it?
# To ensure that we don't make the same mistake again, we can use type function
# Type function will tell you the data type something is
# Let's try it on name_length

print(type(name_length))

# Type tells us that name_length is int or and integer
# This way we will know when we make a mistake and try to combine two different data types
# Now that we know that name_length is int, and that's why we can't add it to string,
# Let's convert it to string
# If we put str(name_length), we can convert name_length into a string 
# and we can add it to other strings
# Now let's try the program again

name_length = len(input("What is your name?  "))
new_name_length = str(name_length)
print("Your name is " + new_name_length + " characters.")

# The program worked!
# Now we have an integer copy of the input function 
# and an str copy to put when combining strings together!
# str can come in really handy when we need to ocnvert floats or integers to strings

# Let's try using str in other instances and see how it changes data types!

a = 123
print(type(a))

# The type of a is right now an integer
# Let's use str and make a contain a string

a = str(123)
print(type(a))

# a became a string!
# let's try converting something into a float and see if it worked

a = 456
a = float(456)
print(type(a))

# Now a became a float
# let's see what happens when we add an integer to a string converted to float!

print(70 + float("100.5"))

# We end up getting a float because the float will convert "100.5" to 100.5
# and when you add 100.5 to 70, you will get 170.5 which is a float!
# Now let's try adding this:

print(str(123) + str(456))

# it combines both numbers like how you would add two strings
# That shows how integers became strings after putting them in a print statement using str
# str makes elements turn into strings! So cool!

# Practice Time!
# Write a program that adds the digits in a 2 digit number
# e.g. if the input was 35, then the output should be 3 + 5 = 8

number = input("Enter a two digit number: ")


first_digit = number[0]
second_digit = number[1]

sum = int(first_digit) +  int(second_digit)

print(first_digit + " + " + second_digit + " = " + str(sum))