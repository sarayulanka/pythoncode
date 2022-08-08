# In Python, class variables are bound to a class while instance variables are bound
# to a specific instance of a class. The instance variables are also called instance attributes.

from pprint import pprint


class HtmlDocument:
    version = 5
    extension = 'html'


pprint(HtmlDocument.__dict__)

print(HtmlDocument.extension)
print(HtmlDocument.version)

# The HtmlDocument class has two class variables: extension and version. 
# Python stores these two variables in the __dict__ attribute.

# When you access the class variables via the class, Python looks them up in the __dict__ of the class.

# The following creates a new instance of the HtmlDocument class:
home = HtmlDocument()

# The home is an instance of the HtmlDocument class. It has its own __dict__ attribute:

pprint(home.__dict__)
# Code language: Python (python)
# The home.__dict__ is now empty:

# {}

# Initializing instance variables
# In practice, you initialize instance variables for all instances of a class in the __init__ method.

# For example, the following redefines the HtmlDocument class that has two instance variables name and 
# contents

class HtmlDocument:
    version = 5
    extension = 'html'

    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

# When creating a new instance of the HtmlDocument, you need to pass the corresponding arguments like this:
blank = HtmlDocument('Blank', '')

# Python stores instance variables in the __dict__ attribute of the instance.
# Each instance has its own __dict__ attribute and the keys in this __dict__ may be different.

# When you access a variable via the instance, Python finds the variable in the __dict__ attribute
# of the instance. If it cannot find the variable, it goes up and look it up in the __dict__ attribute
# of the class.

# If the value of a variable varies from object to object, then such variables are called instance variables.
#  For every object, a separate copy of the instance variable will be created.
# Instance variables are not shared by objects.
# Example

class Student:
    def __init__(self, name, age):
        self.name = name # Instance Var
        self.age = age # Instance Var
        # for every object the data in these variables change, that is why they are instant vars


