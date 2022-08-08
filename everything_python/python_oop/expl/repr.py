class Person:
    # every object creation involved invoking the __init__ method <- constructor
    # which means when you do Person(), __init__ is executed
    # you dont execute this method seperately
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # __repr__ just like __str__ returns a string
    # but __repr__ returns a string that can be executed by the machine
    def __repr__(self):
        return f'Person("{self.name}", {self.age})'
    
    def __str__(self):
        return f"{self.name} - {self.age}"

    # if __str__ is not implemented in a class
    # and only __repr__ is implemented, then when you are trying to print an object
    # python will invoke __repr__

raghu = Person('Raghu', 44)

print(raghu)
print(repr(raghu))

o1 = eval(repr(raghu))
print(o1)