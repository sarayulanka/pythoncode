# Functions are blocks of code that are supposed to do an action when we call them
# For example, when we call the print() function, it prints something
# Let's try using some built in functions and analyze what happens:

print("Hello!")
print(len("hello"))

# As examples, we used the print function and the len function
# Now, we know that there are many built-in functions but what if we wanted to create our own?
# That is actually possible in python
# we can create our own functions and use them in our programs
# Let's try creating a function and calling it when we need it in our program:

def my_function():
    # def stands for define because we are defining our function
    # my_function is now the name of the function so we are saying define my_function as function
    print("Hi!")
    print("Bye")


# Did you notice how hi and bye weren't printed when we executed the program?
# the reason is because we didn't call the function yet
# if we were to call the function, we would get hi and bye
# so let's try it!
# the syntax is: name_of_function(parameters if there are any)

my_function()

# It worked! We just created our first function!
# We will be using this technique a lot more in the near future
