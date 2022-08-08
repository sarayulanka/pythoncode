# First special method: __str__

# __str__() is a method defined in a class that returns a string representation of the object.
 
# In other words, The __str__ method in Python represents the class objects as a string – it 
# can be used for classes. The __str__ method should be defined in a way that is easy to read and outputs
# all the members of the class. This method is also used as a debugging tool when the members of a class
# need to be checked.

# Sometimes, it’s useful to have a string representation of an instance of a class.
# To customize the string representation of a class instance, the class needs to implement the __str__ 
# magic method.

# Internally, Python will call the __str__ method automatically when an instance calls the str() method.

# Note that the print() function converts all non-keyword arguments to strings by passing them to the str()
# before displaying the string values.

# The following illustrates how to implement the __str__ method in the Person class:

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'Person({self.first_name},{self.last_name},{self.age})'

# And when you use the print() function to print out an instance of the Person class,
# Python calls the __str__ method defined in the Person class. For example:

person = Person('Sarayu', 'Lanka', 12)
print(person.__str__())

# Output:
# Person(John,Doe,25)


# Second special method: __repr__ method

# repr(object): Return a string containing a printable representation of an object. 
# This is the same value yielded by conversions

# In Python, __repr__ is a special method used to represent a class's objects as a string.
#  __repr__ is called by the repr() built-in function.

# Now one might think that the repr method is the exact same to the __str__ method, but there is a difference

# The difference between str() and repr() is:

# The str() function returns a user-friendly description of an object.
# The repr() method returns a developer-friendly string representation of an object.

# Another way to say it would be:

# The __str__ method returns a string representation of an object that is human-readable
#  while the __repr__ method returns a string representation of an object that is machine-readable.

# Example of the __repr__ method in a class:

class Person2:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'



person = Person2('Sarayu', 'Lanka', 12)
print(person.__repr__())


# Third special method: __eq__ method

# One is supposed to use the Python __eq__ method to compare two objects by their values.