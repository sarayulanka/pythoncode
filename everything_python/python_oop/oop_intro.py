# Classes are user-defined data types that act as the blueprint for individual objects, attributes
# and methods. Objects are instances of a class created with specifically defined data. 

# Objects can correspond to real-world objects or an abstract entity.
# Everything in Python is an object. Classes are used to model and give data to different objects.

# Defining a class:
# To define a class, you do not use def. Instead, you use class...
# The name of your class always has to be in title case meaning first letter should be uppercase

class Dog:
    pass

# To create an object from the Person class, you use the class name followed by parentheses (),
#  like calling a function:
biscuit = Dog()

# biscuit is an object

# Creating Instant Attributes
# Sometimes you want unique data to give more behaviours and things liek that to yoru object.
# For example in my dog class, is there a way to give data that the dog oject is named biscuit?
# Yes there is:

# An instance attribute is a Python variable containing unique data that varies between objects
# This variable is only accessible in the scope of this object and it is defined inside
# the constructor function, __init__(self,..) of the class.

# To define and initialize an attribute for all instances of a class, you use the __init__ method.
# The following defines the Person class with two instance attributes name and age:

# When you create a Person object, Python automatically calls the __init__ method 
# to initialize the instance attributes. In the __init__ method, the self is the instance 
# of the Person class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# The following creates a Person object named sarayu:
sarayu = Person('Sarayu', 12)

# The person object now has the name and age attributes. 
# To access an instance attribute, you use the dot notation. 
# For example, the following returns the value of the name attribute of the person object:
# person.name

# You can also define instance methods:
# Instance methods are the default methods defined in Python classes. They are called
#  instance methods because they can access instances of a class (objects).
#  Two ways to use instance methods are to read or write instance attributes.
#  In other words instance methods are used to read or modify the state of an object

class Car:
    def __init__(self, model, age, speedometer):
        self.speedometer = speedometer
        self.model = model
        self.age = age
    
    def car_speed(self):
        print(f"The car is traveling at a speed of {self.speedometer} miles per hour.")
    
tesla = Car("Model Y", 1, 75)

# To call one of the methods, do this syntax
# print() or not print(object.instance_method())
tesla.car_speed()

# Define class attributes
# Unlike instance attributes, class attributes are shared by all instances of the class. 
# They are helpful if you want to define class constants or variables that keep track of 
# the number of instances of a class.

class House:
    house_type = "Regular Sized House"

# In this scenario, house_type is the class attributes

# Class Methods

# Like a class attribute, a class method is shared by all instances of the class. 
# The first argument of a class method is the class itself. By convention, its name is cls.
#  Python automatically passes this argument to the class method. 
#  Also, you use the @classmethod decorator to decorate a class method.

# The following example defines a class method that returns an anonymous Person object:

class Person_two:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f"Hi, it's {self.name}."

    @classmethod
    def create_anonymous(cls):
        return Person('Anonymous', 22)


anonymous = Person.create_anonymous()
print(anonymous.name)

# Define static method
# A static method is not bound to a class or any instances of the class. 
# In Python, you use static methods to group logically related functions in a class.
#  To define a static method, you use the @staticmethod decorator.

# For example, the following defines a class TemperatureConverter that has two static methods that 
# convert from celsius to Fahrenheit and vice versa:

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5 * (f - 32) / 9


# Single inheritance
# A class can reuse another class by inheriting it. When a child class inherits from a parent class,
#  the child class can access the attributes and methods of the parent class.

# For example, you can define an Employee class that inherits from the Person class:

class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

# Inside the __init__ method of the Employee class calls the __init__method of the Person class
# to initialize the name and age attributes. The super() allows a child class to access a method 
# of the parent class.

# The Employee class extends the Person class by adding one more attribute called job_title.

# The Person is the parent class while the Employee is a child class. To override the greet() method
#  in the Person class, you can define the greet() method in the Employee class as follows:

class Employee(Person_two):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def greet(self):
        return super().greet() + f" I'm a {self.job_title}."