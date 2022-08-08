# Intro to encapsulation in Python

# Encapsulation is one of the four fundamental concepts in object-oriented programming
# including abstraction, encapsulation, inheritance, and polymorphism.

# The process of wrapping up variables and methods into a single entity is known as Encapsulation.
# In other words, Encapsulation is the packing of data and functions that work on that data within a single 
# object. By doing so, you can hide the internal state of the object from the outside. 
# This is known as information hiding.

# However, to do the concept of encapsulation, you need to use something called private attributes

# Python encapsulation example
# The following defines the Counter class(regular class):

# class Counter:
#     def __init__(self):
#         self.current = 0

#     def increment(self):
#         self.current += 1

#     def value(self):
#         return self.current

#     def reset(self):
#         self.current = 0

# Now let's try to build this class using private attributes and then do the concept of encapsulation:

# Private attributes can be only accessible from the methods of the class. In other words, they cannot 
# be accessible from outside of the class.
# Python doesn’t have a concept of private attributes. In other words, all attributes are accessible 
# from the outside of a class.

# By convention, you can define a private attribute by prefixing a single underscore (_):
# _attribute

# This means that the _attribute should not be manipulated and may have a breaking change in the future.

class Counter:
    def __init__(self):
        self._current = 0

    def increment(self):
        self._current += 1

    def value(self):
        return self._current

    def reset(self):
        self._current = 0


counter = Counter() # Part of the encapsulation method


counter.increment() # Part of the encapsulation method
counter.increment() # Part of the encapsulation method
counter.increment() # Part of the encapsulation method

print(counter.value()) # Part of the encapsulation method


# Name mangling with Double Underscores

# A double underscore prefix causes the Python interpreter to rewrite the attribute name
# in order to avoid naming conflicts in subclasses. This is also called name mangling—the interpreter
# changes the name of the variable in a way that makes it harder to create collisions 
# when the class is extended later with inheritance.

# Syntax for name mangling:
# __attribute_name

# What will happen to the attribute's name after doing double_underscore:
# _class_name__attribute_name

