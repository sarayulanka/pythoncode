# The first type of advanced arguments we are going to learn is called default arguments

# When we were learning about classes, we learnt about how we can initialize default attributes so that 
# whenever the user created an object and didn't specify something for that argument, it would 
# already have a default value

# Default arguments are a similar concept except with arguments and not attributes
# Let's try creating a function with default arguments

def numbers(a, b=4, c=6): 
    print(a, b, c)
 
numbers(1)

# This code wouldn't work if b and c parameters werne't default arguments but since they have a 
# value when the function is first getting defined, they have default values so if the user doesn't give
#  them any values, they will be assigned the default values

# It is important to remember that this ONLY works if you have assigned a default value





# Now we are going to learn about the second type of advanced arguments:
# The *args(many positional arguments) type of advanced arguments:

# *args means when you put an asterik followed by a parameter when
# defining the function and instead of the user only giving as many arguments as there are parameters,
# the asterik allows the user to put unlimited arguments regardless of how many arguments there are

# Let's try creating a function with *args:

def add(*numbers):
    print(numbers)
    sum = 0
    for number in numbers:
        sum += number

    print(sum)

add(3, 5, 6)


# all the arguments you put when calling the function are stored into a tuple inside the *args name
# *args are called unlimited position arguments because the order in which you put them matters 
# because they are stored inside of a tuple


# **kwargs is basically the same as *args 
# There are only two differences:

# The first difference is that there are two asteriks before the name for **kwargs only 
# one asterik before the name for *args

# The second difference is that instead of the unlimited positional arguments being called 
# by position in *args, the unlimited arguments are being called by there keyword, therefore 
# being called unlimited keyword arguments

# Unlimited keyword arguments(**kwargs) are stored in a dictionary, the keyword will be the key,
# and the value assigned to the keyword when the function is called is the value


# Let's try creating a function with **kwargs:

def name(**kwargs):
    print(kwargs)
    # When kwargs is printed, you can see that it is in dictionary format

    for key, value in kwargs.items():
        print(f"{key}: {value}")


name(name1='Sarayu', name2='shloka', name3='sruthi', name4='adhya')

# So the main difference between *args and **kwargs is that *args arguments are called by position
# and **kwargs arguments are called by keyword and that the arguments are put in tuples in *args and
# for **kwargs, the arguments are put in dictionaries
