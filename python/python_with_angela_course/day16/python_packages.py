# As you already know, modules are file data that you can access at any point in time
# Python packages are modules full of code bunched up together into a package
# These python packages are very useful
# However, it's time-consuming to find these packages by just searching them up
# That is why the py-pi website was created
# The py-pi website is a database full of python packages written by other people

# The beauty of the py-pi website is that anybody can access the different python packages
# Let's try accessing a package, install it, and then use it in this file

# I am going to pip install an emoji python package

import emoji

print(emoji.emojize('Python is :thumbs_up:'))


# Now let's do a project using a python package called pretty table.
# Inside the pretty table package, there is a class
# This class creates objects that takes data and puts it in appealing tables
# Using command prompt, I pip installed the package and now we're ready to start working with it.

# The first thing we are going to do is say from python_package_name import classname:
from prettytable import PrettyTable

# Now that we have imported the PrettyTable class successfully, let's try creating a table
table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]

table.add_row(["Pikachu", "Electric"])
table.add_row(["--------------", "-----------"])
table.add_row(["Fennekin", "Fire"])

print(table)


# What we did above was tapping into prettytable's methods
# Now let's try tapping into the class's attributes

# There is one attribute called align
# We can change the alignment by saying l for left, c for center, or r for right
# Let's change the attribute below:

table.align = "l"