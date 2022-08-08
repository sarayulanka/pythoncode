# Strings

# If a string contains a single quote, always contain it in a double quote
# One can use the backslash to escape quote like so:

message = 'It\'s also a valid string'

# if you don't want python to treat the blackslash in a special way, just add an r before the quotes:

message2 = r'It\'s also a valid string'

# You can also use triple quotes to make a string span across several lines:

help_message = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''
# This would output:

# Usage: mysql command
#     -h hostname
#     -d database name
#     -u username
#     -p password

# Python strings are immutable. It means that you cannot change the string. 
# For example, you’ll get an error if you attempt to update one or more characters in a string

# Numbers

# To calculate exponents, you use two multiplication symbols (**)
# To change order of math operations, use parenthesis

# Python supports common numeric types including integers, floats, and complex numbers.
# Use the underscores to group numbers for the large numbers.

# Booleans

# To find out if a value is True or False, you use the bool() function

# Falsy Values:
# The number zero (0)
# An empty string ''
# False
# None
# An empty list []
# An empty tuple ()
# An empty dictionary {}

# Constants

# To do it in other programming languages, you can use constants. 
# The constants like variables but their values don’t change during the program executes.

# The bad news is that Python doesn’t support constants.

# To work around this, you use all capital letters to name a variable to indicate
#  that the variable should be treated as a constant. For example:

HELLO_WORLD = "Hello World!"

# Possible type conversions in Python:

# Besides the int(str) functions, Python support other type conversion functions. 
# The following shows the most important ones for now:

# float(str) – convert a string to a floating-point number.
# bool(val) – convert a value to a boolean value, either True or False.
# str(val) – return the string representation of a value.

# To find the type of a value:
# you can use type(value)

# Comparison Operators

# Python has six comparison operators, which are as follows:

# Less than ( < )
# Less than or equal to (<=)
# Greater than (>)
# Greater than or equal to (>=)
# Equal to ( == )
# Not equal to ( != )

# These comparison operators compare two values and return a boolean value, either True or False.

# Logical Operators

# Sometimes, you may want to check multiple conditions at the same time. To do so, you use logical operators.

# Python has three logical operators:

# and
# or
# not

# The precedence of the logical operator from the highest to lowest: not, and, and or

# Perfect way to define if condition: You use the if statement to execute a block of code 
# based on a specified condition

x = 3

if x > 5:
    print("Something")
else:
    print("Something else")

# The if...elif...else statement checks each condition (if-condition, elif-condition1, elif-condition2, …) 
# in the order that they appear in the statement until it finds the one that evaluates to True.

if x > 5:
    print("Something")
elif x == 5:
    print("S")
else:
    print("Something Else")

# The following syntax is called a ternary operator in Python:

# value_if_true if condition else value_if_false
# Example:

y = 45
number = print("something") if y > 5 else print("Something else")

# You can print in the ternary operator as well as put a value in and print the variable later
# The ternary operator does not include valid logic for elif; only if and else

# Use the ternary operator to make your code more concise.

# Use the for loop statement to run a code block a fixed number of times.
# Use the range(start, stop, step) to customize the loop.

# The while statement checks the condition at the beginning of each iteration. 
# It’ll execute the body as long as the condition is True.

command = ''

while command.lower() != 'quit':
    command = input('>')
    print(f"Echo: {command}")

#  Break

# Sometimes, you want to terminate a for loop or a while loop 
# prematurely regardless of the results of the conditional tests. 
# In these cases, you can use the break statement:

# Typically, you use the break statement with the if statement
#  to terminate a loop when a condition is True.

# Continue

# The continue statement is used inside a for loop or a while loop. 
# The continue statement skips the current iteration and starts the next one.

# Typically, you use the continue statement with an if statement 
# to skip the current iteration once a condition is True.

# Pass

# The pass statement is a statement that does nothing.
# It’s just a placeholder for the code that you’ll write in the future.

# When you run the code that contains a pass statement, the Python interpreter
# will treat the pass statement as a single statement. As a result, it doesn’t issue a syntax error.

# A Python function is a reusable named block of code that performs a task or returns a value.
# Use the def keyword to define a new function. A function consists of function definition and body.
# A function can have zero or more parameters. You need to pass the same number of arguments into it.
# A function can perform a job or return a value. Use the return statement to return a value from a function.

# def function_name(param1, param2=value2, param3=value3, ...):
# if someone doesn't specify an argument for each parameter there can be a default value

# # Place default parameters after the non-default parameters.

# Use the Python keyword arguments to make your function call more readable and obvious, 
# especially for functions that accept many arguments.
# All the arguments after the first keyword argument must also be keyword arguments too.

# Recursive functions

# A recursive function is a function that calls itself until it doesn’t.
# It is typically used to make bits and pieces of a hard problem easier

# Example:

def count_down(start):
    """ Count down from a number  """
    print(start)

    # call the count_down if the next
    # number is greater than 0
    next = start - 1
    if next > 0:
        count_down(next)


count_down(3)

# A recursive function is a function that calls itself until it doesn’t.
# And a recursive function always has a condition that stops calling itself.

# Python lambda expressions allow you to define anonymous functions.

# Anonymous functions are functions without names. The anonymous functions are useful
#  when you need to use them once.

# A lambda expression typically contains one or more arguments, but it can have only one expression.

# The following shows the lambda expression syntax:

# lambda parameters: expression

names = lambda first_name,last_name: f"{first_name} {last_name}"

# names looks like a variable but because it has a lambda expression, it is a function
print(names("sarayu", "lanka"))


# Use the help() function to get the documentation of a function.
# Place a string, either single-line or multi-line strings, as the first line 
# in the function to add documentation to it.

# A list is an entry ordered collection of items.
# Use square bracket notation [] to access a list element by its index. The first element has an index 0.
# Use a negative index to access a list element from the end of a list. The last element has an index -1.
# Use list[index] = new_value to modify an element from a list.
# Use append() to add a new element to the end of a list.
# Use insert() to add a new element at a position in a list.
# Use pop() to remove an element from a list and return that element.
# Use remove() to remove an element from a list.

# A tuple is a list that cannot change. Python refers to a value that cannot change as immutable.
# So by definition, a tuple is an immutable list.
# Tuple syntax:

colors = ('red', 'green', 'blue')
print(colors)

# Use the Python List sort() method to sort a list in place.

# The sort() method sorts the string elements in alphabetical order 
# and sorts the numeric elements from smallest to largest.

# Use the sort(reverse=True) to reverse the default sort order.

# Use the sorted() function to return a new sorted list from a list.
# Use the sorted() function with the reverse argument sets to True
# to sort a list in the reverse sort order.

# Use list slice to extract a sublist from a list and modify the list.

# sub_list = list[begin: end: step]

# Reversing a list with slice is [::-1]

# Unpacking assigns elements of the list to multiple variables.

colors = ['red', 'blue', 'green']
red, blue, green = colors

red, blue, *other = colors

print(red)
print(blue)
print(green)

# Use the asterisk (*) in front of a variable like this *variable_name
# to pack the leftover elements of a list into another list.

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for index, city in enumerate(cities,1):
    print(f"{index}: {city}")

# Use a for loop with the enumerate() function to access indexes and to iterate over lists

# Use the in operator with the index() function to find if an element is in a list and find its index

# In Python, an iterable is an object that includes zero, one, or many elements. 
# An iterable has the ability to return its elements one at a time.
# Example: lists, dictionaries, tuples, strings, range function, etc

# An iterator is an agent that performs iteration. 
# It’s stateful. And an iterator is also an iterable object.
# Use the iter() function to get an iterator from an iterable object 
# and the next() function to get the next element from the iterable object.


# The map() function iterates over all elements in a list (or a tuple), 
# applies a function to each and returns a new iterator of the new elements.
# Example:

def exponents(num):
    return num**2

numbers = [1, 2, 3]
exponents_1 = map(exponents, numbers)
print(list(exponents_1))

# Use the Python map() to call a function on every item of a list and returns an iterator.
# Transform it into an iterable using functions like list()

# The filter() function iterates over the elements of the list and applies the fn() function to each element. 
# It returns an iterator for the elements where the fn() returns True.
# It filters each element of the list based on whether the function returns true

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = filter(lambda num: num % 2 == 0, numbers)

print(list(filtered))

# The reduce() function applies the fn function of two arguments cumulatively to the items of the list, 
# from left to right, to reduce the list into a single value.
# The reduce function

# The function that the reduce() function will take has requirements: 
# 

# Unlike the map() and filter() functions, the reduce() isn’t a built-in function in Python.
#  In fact, the reduce() function belongs to the functools module.

from functools import reduce

def sum(a, b):
    print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b


scores = [75, 65, 80, 95, 50]
total = reduce(sum, scores)
print(total)

# Python List comprehensions that allow you to create a new list from an existing one.
# for loops would be the straightforward way. However, list comprehensions allow you to have shorter and
# better code:
# Syntax is: [output_expression for element in list if condition], if condition is optional

numbers = [1, 2, 3]
new_numbers = [num * 2 for num in numbers]
print(new_numbers)


# The dictionary is a collection of key,value pairs and isn't an iterable. To loop over it, functions make it a list
# To access a value associated with a key you can use the square bracket notation:
# dict[key]

dict = {"name": "sarayu", "age": 12}
print(dict["age"])

# you can also use the get() method:
# dict.get(key)

print(dict.get("name"))

# If the key doesn’t exist, the get() method returns None instead of throwing a KeyError. 
# Note that None means no value exists.

dict['gender'] = 'Famale'

# This is how to add a new key value pair in the dictionary: dict_name[new_key] = new_value
# To modify a current value in the dictionary, you do dict[key] = new_value

dict['gender'] = 'female'
print(dict)

# To remove you just del dict_name[key]
del dict['gender']

# Looping through a dictionary:

for key, value in dict.items():
    print(f"{key}: {value}")

# Looping through all the keys in a dictionary:
# In fact, looping through all keys is the default behavior when looping through a dictionary.
# Therefore, you don’t need to use the keys() method, this is optional
for key in dict.keys():
    print(f"{key}")

for value in dict.values():
    print(f"{value}")

# A dictionary comprehension allows you to run a for loop on a dictionary 
# and do something on each item like transforming or filtering, and returns a new dictionary.

# Unlike a for loop, a dictionary comprehension offers a more expressive and concise syntax 
# when you use it correctly.
# Syntax: {key:value for (key,value) in dict.items() if condition}, if condition is optional

stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

new_stocks = {symbol: price * 1.02 for (symbol, price) in stocks.items()}
print(new_stocks)

# Sets: 

# A Python set is an unordered list of immutable elements. It means:

# Elements in a set are unordered.
# Elements in a set are unique. A set doesn’t allow duplicate elements.
# Elements in a set cannot be changed. For example, they can be numbers, strings, 
# and tuples, but cannot be lists or dictionaries.

first_set = set(["hello", "world", "i"])
print(first_set)

# To check if a set contains an element, you use the in operator
# To add an element to a set, you use the add() method:

first_set.add("quite")

print(first_set)

skills = {'Problem solving', 'Software design', 'Python programming'}
# skill = skills.pop()

# To remove and return an element you use pop()
# To remove an element you use remove()
# To make it more convenient, the set has the discard() method that allows you to remove an element.
# And it doesn’t raise an error if the element is not in the list unlike remove()
skills.discard('Software design')

print(skills)

# To remove all of the elements in a set you use clear()
# skills.clear()
# print(skills)

# To make a set immutable, you use the built-in function called frozenset()
frozenset(skills)

# Looping through set elements:
# To access the index of the current element inside the loop, you can use the built-in enumerate() function:

for index, skill in enumerate(skills, 1):
    print(f"{index}. {skill}")

# The 1 passed in the enumerate() function is the starting value being passed

# Set Comprehension:

python_instruments = {"Django", "Numpy", "Pandas"}
tags_lower = set(map(lambda value: value.lower(), python_instruments))
print(tags_lower)

# This is one way to do the program of turning the values into all lowercase with lambda and map() and set()
# However, the other way involves set comprehension:
# Set comprehension syntax: {expression for element in set if condition}

tags_lower_comp = {value.lower() for value in python_instruments}
print(tags_lower_comp)

# Let's do a program with an if condition in the set comprehension:

tags_lower_co_if = {value.lower() for value in python_instruments if "a" in value}
print(tags_lower_co_if)

# Set Union
# Allows u to create a new set from distinct elements of both sets
# Two ways to do this - the union() method and the union operator

# Union method:
# the union() method accepts one or more iterables, converts the iterables to sets, and performs the union.

rates = {1, 2, 3}
ranks = [2, 3, 4]

ratings = rates.union(ranks)
print(ratings)

s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

s = s1.union(s2)
print(s)

# Union Operator:
# However, the union operator (|) only allows sets, not iterables like the union() method.

s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

s4 = s1|s2
print(s4)

# Intersection of sets 
# When intersecting two or more sets, you’ll get a new set consisting of elements that exist in all sets.

# There is two ways to do this task:

# First way:
# Set Intersection method
# syntax: new_set = set1.intersection(set2, set3, ...)

s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

s = s1.intersection(s2)
print(s)

# Set Intersection operator
# new_set = s1 & s2 & s3 & ...

s12 = {'Python', 'Java', 'C++'}
s23 = {'C#', 'Java', 'C++'}

s5 = s12 & s23
print(s5)

# Set intersection() method vs set intersection operator (&)
# The set intersection operator only allows sets, while the set intersection()
# method can accept any iterables, like strings, lists, and dictionaries.

# If you pass iterables to the intersection() method, 
# it’ll convert the iterables to set before intersecting them.

# Difference of sets

s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

# Use these sets to understand the difference of sets
# s1 - s2 -> s1 - (the common elements between both sets)
# output for the diference of sets in this example is {'Python'}

# for this also there is a difference() method and an operator(-):
# Method:

s = s1.difference(s2)
print(s)

# Operator:

s3 = s1 - s2
print(s3)

# Like the other operations,
# The set difference() method can accept one or more iterables (e.g., strings, lists, dictionaries) 
# while the set difference operator (-) only allows sets.

# When you pass iterables to the set difference() method, 
# it’ll convert the iterables to sets before performing the difference operation.


# The symmetric difference of two sets is a set of elements 
# that are in either set, but not in their intersection.

s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

# for this also there is symmetric() method and an operator(^):
# Method:
s = s1.symmetric_difference(s2)
print(s)

# Operator:

s = s1 ^ s2
print(s)

# Like the other operations,
# The symmetric_difference() method can accept one or more iterables (e.g., strings, lists, dictionaries) 
# If the iterables aren’t sets, the method will convert them to sets before returning the symmetric difference of them.
# while the symmetric difference operator (^) only allows sets.

# Suppose that you have two sets A and B.
# Set A is a subset of set B if all elements of A are also elements of B. Then, set B is a superset of set A.

# In Python, you can use the Set issubset() method to check if a set is a subset of another
# Syntax: set_a.issubset(set_b)
# It will return a boolean value: True or False

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

print(scores.issubset(numbers))
print(numbers.issubset(scores))

# Subset Operators:

# you can use the subset operator (<=) to check if a set is a subset of another set:
# set_a <= set_b

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = scores <= numbers
print(result)  # True

result = numbers <= numbers
print(result)  # True

# If two sets aren't equal but one is a subset of another, then it is considered a proper subset
# You can use the proper subset operator (<) to check if a set is a proper subset of another set
# set_a < set_b

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = scores < numbers
print(result)  # True

result = numbers < numbers
print(result)  # False

# a set A is a superset of a set B if all elements of the set B are elements of the set A.
# If set A and set B are not equal, set A is a proper superset of set B.
# Use Python issuperset() method to check if a set is a superset of another.
# Use the superset operator (>=) or proper superset operator (>) to check if a set is a superset or proper superset of another set.

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

result = numbers >= scores
print(result)  # True

result = numbers > numbers
print(result)  # False

print(numbers.issuperset(scores))

# Disjoint sets:

# Two sets are disjoint when they have no elements in common.
# In other words, two disjoint sets are sets whose intersection is an empty set.

# For example, the {1,3,5} and {2,4,6} sets are disjoint because they have no common elements.

# Syntax: set_a.isdisjoint(set_b)
# Example:


odd_numbers = {1, 3, 5}
even_numbers = {2, 4, 6}

result = odd_numbers.isdisjoint(even_numbers)
print(result)

# Exception Handling
# When one writes invalide python code, it will raise an error, there are all sorts of errors
# In python, errors that occur during execution of programs are called exceptions
# When an exception occurs, the program doesn’t handle it automatically. This results in an error message.
# To make the program more robust, you need to handle the exception once it occurs. In other words,
# you need to catch the exception and inform users so that they can fix it.

# A good way to handle this is not to show what the Python interpreter returns.
# Instead, you replace that error message with a more user-friendly one.

# To do that, you can use the Python try...except statement:

try:
    # This is where you put the code you want to run that could have errors
    user_input = int(input("Please enter your age: "))
except:
    # This is where you put the block of code you want to execute 
    # if there is an error in the code from the try block
    print("The text you entered is invalid, please enter a number.")
    user_input = int(input("Please enter your age: "))

# However, what if you want to catch a specific exception?
# The Try-Except statement allows you to do that like below:

try:
    user_input = int(input('Please enter a number:  '))
except ValueError:
    # code to handle the exception
    print("Please enter a valid number!")
    user_input = int(input("Please enter a number: "))

# This statement also allows you to have multiple exceptions to look for several errors:

try:
    user_input = input('Please enter a number:  ')
    print(user_input + 34)
except TypeError:
    print("The code you wrote is invalid. Please look at your code again.")
except ValueError:
    # code to handle the exception
    print("Please enter a valid number!")
    user_input = int(input("Please enter a number: "))

# There is also a finally clause in this statement which is optional 
# but you use it to clean up the program
# The code in this block will execute whether there is an exception or not

try:
    # code that may cause exceptions
    pass
except:
    # code that handle exceptions
    pass
finally:
    # code that clean up
    pass

# The finally clause always executes whether an exception occurs or not.
# And it executes after the try clause and any except clause.

# Example:

a = 10
b = 0

try:
    c = a / b
    print(c)
except ZeroDivisionError as error:
    print(error)
finally:
    print('Finishing up.')

# Python Try Finally Statement
# The catch clause in the try...catch...finally statement is optional. So you can write it like this

# try:
#     # the code that may cause an exception
# finally:
#     # the code that always executes
# Use the finally clause to clean up the resources such as closing files.


# The try statement also has an optional else clause with the following syntax:

try:
    # code that may cause errors
    pass
except:
    # code that handle exceptions
    pass
else:
    # code that executes when no exception occurs
    pass

# Do While Statement in Python

# The Python Language doesn't support the Do While Statement
# However this can be imitated using the break keyword and while loop

# First, remove the code before the while loop.
# Second, add the condition to stop the loop 
# if the entered number equals the random number by using the break statement.


# MORE ON FUNCTIONS

# Unpacking Tuples

# Unpacking a tuple means splitting the tuple’s elements into individual variables.
# Syntax for unpacking tuples: x, y = (1, 2)

# Example:
num1, num2, num3 = (1, 2, 3)
print(num1)
print(num2)
print(num3)

# Using unpacking tuple to swap values of two variables
# To do this without a specific syntax, you would have to use a temporary variable
# This would take too many lines of code
# That is why there is an easier way to do this:
# x, y = y, x is the syntax

x, y = ("hello", "world")

print(f"{x} {y}!")

x, y = y, x

print(f"{x} {y}")

# The _ variable is a regular variable in Python. By convention, it’s called a dummy variable.
# Typically, you use the dummy variable to unpack when you don’t care and use its value afterward.

x, y, _ = 10, 20, 30

# Use the * operator to assign remaining elements of an unpacking assignment 
# into a list and assign it to a variable.

r, g, *other = (192, 210, 100, 0.5)

print(r)
print(g)
print(other)

# Using the * operator on the right hand 

# Python allows you to use the * operator on the right-hand side. Suppose that you have two tuples:

odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)

# The following example uses the * operator to unpack those tuples and merge them into a single tuple:

numbers = (*odd_numbers, *even_numbers)
print(numbers)

# Output:
# (1, 3, 5, 2, 4, 6)

# When a function has a parameter preceded by an asterisk (*), it can accept a variable number of arguments. 
# And you can pass zero, one, or more arguments to the *args parameter.

# In Python, the parameters like *args are called variadic parameters. 
# Functions that have variadic parameters are called variadic functions.

# Note that you don’t need to name args for a variadic parameter.
#  For example, you can use any meaningful names like *numbers, *strings, *lists, etc.

# The *args argument exhausts positional arguments so you can only use keyword arguments after it.
# Examples:

def add(*args):
    print(type(args))
    print(args)

add()

def add(x, y, *args, z):
    sums = x+y+z
    for arg in args:
        sums +=arg
    return sums

print(add(10, 20, 30, 40, z=50))

# Unpacking arguments
# The following point function accepts two arguments and 
# returns a string representation of a point with x-coordinate and y-coordinate:

def point(x, y):
    return f"({x}, {y})"

# If you pass a tuple to the point function, you’ll get an error:

a = (0, 0)
# origin = point(a)  -> This line will cause an error as it seems you are only passing on argument
# To fix this you need to prefix the tuple a with the operator * like this:

origin = point(*a)
print(origin)

# When you precede the argument a with the operator *,
# Python unpacks the tuple and assigns its elements to x and y parameters.

# The **kwargs is called a keyword parameter.

# When a function has the **kwargs parameter, 
# it can accept a variable number of keyword arguments as a dictionary.

# The two stars (**) are important. However, the name kwargs is by convention.
#  Therefore, you can use any other meaningful names such as **configs and **files.

# Example:

def persons(*args, **kwargs):
    print(args)
    print(kwargs)

persons(1, 2, 3, 4, name="Sarayu Lanka", age=12)

# In conclusion:

# Use the Python **kwargs parameter to allow the function to accept a variable number of keyword arguments.
# Inside the function, the kwargs argument is a dictionary that contains all keyword arguments as its name-value pairs.
# Precede double stars (**) to a dictionary argument to pass it to **kwargs parameter.
# Always place the **kwargs parameter at the end of the parameter list, or you’ll get an error.

# Partial Functions are functions that will be used for repurposing a generic function with less arguments
# Example:

def multiply(a, b):
    return a*b


def double(a):
    return multiply(a, 2)

def same_product():
    return multiply(double(10), 10)

result = double(10)
print(result)  # 20
res1 = same_product()
print(res1)

# In this example, double() is the partial function; it has reduced number of arguments 
# and is repurposing generic function which is multiply() just for doubling

def addnumbers(a, b):
    return a + b

def increment(a):
    return addnumbers(a, 1)


# Python partial function from functools module

# functools.partial(fn, /, *args, **kwargs)

# The partial function returns new partial object, which is a callable.

# When you call the partial object, Python calls the fn function 
# with the positional arguments args and keyword arguments kwargs.

# The following example shows how to use the partial function to define the double function 
# from the multiply function:

from functools import partial

def multiply(a, b):
    return a*b


double = partial(multiply, b=2)

result = double(10)
print(result)

# Use type hints and static type checker tools to make your code more robust; strong and accurate

# Python uses dynamic typing, in which variables, parameters, and return values of a function
# can be any type. Also, the types of variables can change while the program runs.

# Generally, dynamic typing makes it easy to program and causes unexpected errors
#  that you can only discover until the program runs.

# Python’s type hints provide you with optional static typing to leverage
#  the best of both static and dynamic typing.

# The following example defines a simple function that accepts a string and returns another string:

def say_hi(name):
    return f"Hello {name}"

greeting = say_hi("Sarayu")
print(greeting)

# Now let's do the same program but with type hints:
# Syntax for adding type hints to a parameter and return value of a function
# parameter: type
# -> type


def say_hi2(name: str) -> str:
    return f"Hello {name}"

greeting2 = say_hi2("hello")
print(greeting2)

# Besides the str type, you can use other built-in types such as int, float, bool,
# and bytes for type hintings.

# Python doesn’t have an official static type checker tool. 
# At the moment, the most popular third-party tool is Mypy.Since Mypy is a third-party package, 
# you need to install it using pip install command

# Once installed mypy, you can use it to check the type before running the program 
# by using the following command:

# mypy app.py

# Adding type hints for multiple types

# The numbers can be integers or floats. To set type hints for multiple types, you can use Union from the typing module.

# First, import Union from typing module:
from typing import Union

# Next use Union

def sums(x: Union[float, int], y: Union[float, int]) -> Union[float, int]:
    return x + y

print(sums(1, 2))

# Starting from Python 3.10, you can use the X | Y syntax to create a union type, for example:


# def sums(x: float|int, y: float | int) -> float|int:
#     return x + y

# Type Aliases
# Python allows you to assign an alias to a type and use the alias for type hintings. For example:

from typing import Union

number = Union[int, float]


def add2(x: number, y: number) -> number:
    return x + y

print(add2(2, 3))