# We already know one function and the syntax for it: the print function
# Now, let's learn about one function that allows you to get data from the user
# This function is call the input function
# The input function is useful when it comes to getting data from user to use in your programs
# Let's try and use the input function right now!
input("What is your name? ")


# After the user enters data for the input function,
# the text inside the brackets gets replaced with the data the user gave
# An easy way to see this is to add the input with another text:
print("Hello " + input("What is your name? "))


# Write a program that prints the number of characters in a user's name. 
# You might need to Google for a function that calculates the length of a string.
# the function that calculates how many characters there are in something is called len
# the syntax for len is: len(content)

print(len(input("What is your name? ")))
