# Class methods vs. instance methods
# The following table illustrates the differences between class methods and instance methods:

# Features|	class methods | Instance methods
# Binding|	Class | An instance of the class
# Calling|	Class.method() | object.method()
# Accessing| Class attributes | Instance & class attributes
# When to use Python class methods
# You can use class methods for any methods that are not bound to a specific instance but the class.
#  In practice, you often use class methods for methods that create an instance of the class.

# When a method creates an instance of the class and returns it, the method is called a factory method.
#  For example, the create_anonymous() is a factory method because it returns a new instance of the Person class.

# A class method isn’t bound to any specific instance. It’s bound to the class only.

# To define a class method:

# First place the @classmethod decorator above the method definition. For now, you just need to understand 
# that the @classmethod decorator will change an instance method to a class method.
# Second, rename the self parameter to cls. The cls means class. However, class is a keyword so you cannot 
# use it as a parameter.
# The following shows the new version of the Person class:

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def introduce(self):
        return f"Hi. I'm {self.first_name} {self.last_name}. I'm {self.age} years old."

    @classmethod
    def create_anonymous(cls):
        return Person('John', 'Doe', 25)
