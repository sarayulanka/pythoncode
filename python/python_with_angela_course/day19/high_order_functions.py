# Higher order functions are functions that work with other functions
# For example, if one function, takes in another function as an argument,
# that function is a higher order function

# Let's try understanding this concept better with an example:
# P.S. when you put in the name of the function as an argument for another function,
#  you do not put the parenthesis next to the function argument

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def calc(n1, n2, function):
    print(function(n1, n2))

calc(3, 2, add)

# That is what a high order function is.