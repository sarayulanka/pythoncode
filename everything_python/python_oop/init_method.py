# Python calls the __init__ method when it is needed to initialize the created object's attributes
# Usually, methods do not have two underscores on both sides of them. However, the __init method does

# Python will immediately call the __init__method when an object is created of a class

# The __init__ method with default parameters

# The __init__ method can have default parameters, which work the same way 
# they would for a regular function

class Person:
    def __init__(self, name, age=12):
        self.name = name
        self.age = age


if __name__ == '__main__':
    person = Person('Sarayu')
    print(f"I'm {person.name}. I'm {person.age} years old.")
