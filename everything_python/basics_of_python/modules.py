# Modules

# A module is a piece of software that has a specific functionality. 
# A Python module is a file that contains Python code.

# Any file is a module because they can be imported and has the potential to be reusable

# Example:
# Module Code Here; will invoke in different file

def factorial(num):
    counter = 1
    product = 1
    while counter <= num:
        product *= counter
        counter += 1
    return product

    