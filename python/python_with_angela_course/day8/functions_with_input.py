# Recently, we talked about making simple function that required no data from the user
# Well, today we are going to talk about more complex functions that require data from the user
# but first, let's review simple functions:

def greet():
    print("Hello!")
    print("Konnichiwa!")
    print("Hola!")
    print("Bonjour!")

greet()

# As you know, def stands for define and will define the function
# The word next to it is the name you assign to the function
# And lastly, you put a set of parenthesis followed by a colon

# And to call for the function, you put the function name followed by a set of parenthesis

# Now sometimes in functions, we want to get input from the user and use that data in our function
# There is a way to do that
# While you are defining your function, put as many variables as you want inside the parenthesis,
# and when you are calling your function, substitute the variables with actual data inside the parenthesis
# The temporary variables you put inside the parenthesis when defining your function is called parameters
# and when you are calling you function, the actual data replacing the variables are called arguments


# Now, let's try creating a function with parameters and arguments:

def greet_2(name):
    print(f"Hello {name}!")
    print(f"Konnichiwa {name}!")
    print(f"Hola! {name}")
    print(f"Bonjour {name}!")

greet_2("Sarayu")

# Name contained the string that was put in the parenthesis when calling the function
# And that is why when I ran the code, each time name was in the code, 
# it was substituted by the string a.k.a the argument


# Now let's try the same greet function but this time, having two parameters


def greet_3(name, location):
    print(f"Hello {name}!")
    print(f"Isn't the weather nice today in {location}?")

greet_3("Sarayu", "Maryland")

# Now, here's a question
# What if I switched the order of "sarayu" and "Maryland"?
# That would give Hello Maryland! and Isn't the weather nice in Sarayu?
# That is called a positional argument
# Since we didn't specify exactly which argument is to which parameter, python assumes by the order
# So positional arguments are when python assumes which argument belongs to which parameter by order

# However, when you want a guarantee that this problem won't happen,
# you can use something called keyword arguments
# Keyword arguments are when you specify which argument belongs to which parameter so that if you
# ever mess up the order, python will still do what you want it to do with the data
# Let's see how keyword arguments look like:

greet_3(location= "Maryland", name= "Sarayu")


# Practice Time!
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# Calculation you need to do: (height * width) / cover

import math
print(int(math.ceil(4.2)))

def paint_calc(height, width, cover):
    amount_of_cans = (height * width) / cover
    print(f"You'll need {int(math.ceil(amount_of_cans))} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# More Practice Time!
# You need to write a function that checks whether if the number passed into it is a prime number or not.

def prime_checker(number):
    is_prime = True
    for counter in range(2, number):
        if number % counter == 0:
            is_prime = False
    
    if is_prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

num = int(input("Check this number: "))
prime_checker(num)