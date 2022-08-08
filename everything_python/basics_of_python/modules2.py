# To use objects defined in a module from another file, you can use the import statement.
# The import statement has several forms that we will discuss in the next sections.

# 1) import <module_name>
import modules

# When you import a module, Python executes all the code from the corresponding file.
# In this example, Python executes the code from the modules.py file.
# Also, Python adds the module name to the current module.

# This module name allows you to access functions, variables, etc. from the imported module in the 
# current module.
# For example, you can call a function defined in the imported module using the following syntax:
# module_name.function()

print(modules.factorial(5))

# 2) import <module_name> as new_name
# If you don’t want to use the module_name as the identifier in the main program, 
# you can rename the module name to another as follows:

import s as sums1

print(sums1.sums(2, 3))


# 3) from <module_name> import <name>
# If you want to reference objects in a module without prefixing the module name,
# you can explicitly import them using the following syntax:

# from module_name import fn1, fn2
from h import recursive_fibo

def fibo_series(num):
    counter = 1
    while counter <= num:
        print(recursive_fibo(counter))
        counter += 1

fibo_series(5)

# 4) from <module_name> import <name> as <new_name>: rename the imported objects
# It’s possible to rename an imported name to another by using the following import statement:

# from <module_name> import <name> as <new_name>

from d import divide as d_func

print(d_func(6, 3))

# 5) from <module_name> import * : import all objects from a module
# To import every object from a module, you can use the following syntax:
# from module_name import *

from m import *
# Note: Everything in Python is an object so basically everything is imported

print(multiply(9, 3))

# Don't use this statement if you have huge and complex blocks of code

# The difference between import module and from module import foo is mainly subjective. 
# Pick the one you like best and be consistent in your use of it. Here are some points to help you decide.

# import module:

# Pros:
# Less maintenance of your import statements. 
# Don't need to add any additional imports to start using another item from the module

# Cons:
# Typing module.foo in your code can be tedious and redundant 
# (tedium can be minimized by using import module as mo then typing mo.foo)


# from module import foo:

# Pros:
# Less typing to use foo
# More control over which items of a module can be accessed

# Cons:
# To use a new item from the module you have to update your import statement
# You lose context about foo. For example, it's less clear what ceil() does compared to math.ceil()
# Either method is acceptable, but don't use from module import *.

# For any reasonable large set of code, if you import * you will likely be cementing it into the module, 
# unable to be removed. This is because it is difficult to determine what items used 
# in the code are coming from 'module', making it easy to get to the point where you think 
# you don't use the import any more but it's extremely difficult to be sure.

# Introduction to Python module search path
# When you import a python module, there are three places where python will look for module_name.py:

# - The current folder from which the program executes.
# - A list of folders specified in the PYTHONPATH environment variable, if you set it before.
# - An installation-dependent list of folders that you configured when you installed Python.    

# So to make sure that your module is always found in Python and won't be an issue and result in errors,
# make sure to:

# - Place module.py in the folder where the program will execute.
# - Include the folder that contains the module.py in the PYTHONPATH environment variable. 
# Or you can place the module.py in one of the folders included in the PYTHONPATH variable.

#  - Place the module.py in one of the installation-dependent folders.

# Modifying the Python module search path at runtime
# Python allows you to modify the module search path at runtime by modifying the sys.path variable. 
# This allows you to store module files in any folder of your choice.

# Since the sys.path is a list, you can append a search-path to it.

# The following example adds the d:\modules to the search path and use the recruitment module 
# stored in this folder


# Python Packages are basically just a set of modules combined into one package 
# Grouping modules together will result in a package

# The way Python organizes packages and modules like the Operating System structures the folders and files.
# To create a package, you create a new folder and place the relevant modules in that folder.
# To instruct Python to treat a folder containing files as a package, you need to create a __init__.py 
# file in the folder.

# But first, let's talk about how to import a package:

# To import a package, you use the import statement like this:
# import package.module

# And to access an object from a module that belongs to a package, you use the dot notation:
# package.module.function

# When you use the statement to import all objects from a package:

# from <package> import *

