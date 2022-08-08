class Person:
    # every object creation involved invoking the __init__ method <- constructor
    # which means when you do Person(), __init__ is executed
    # you dont execute this method seperately
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"{self.name} -- {self.age}")

    # All the special methods even though you dont declare them
    # they are still there with the creation of a class
    # with default implementations
    # examples for special methods __init__, __str__, __eq__, __repr__ etc etc.

    # __eq__ is used for comparing objects of the Person type only
    def __eq__(self, o: object):
        return type(self) == type(o) and self.name == o.name and self.age == o.age


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating objects of Person type
raghu = Person('raghu', 44)
raghu1 = Person('raghu', 44)
raghu2 = Person('raghu', 42)
sarayu = Person('sarayu', 12)

# Creating objects of Person1 type
raghu3 = Animal('raghu', 44)

# When you are trying to compare one object to another
# python will execute the __eq__ method thats implemented inside the class
# if its not implemented, then the default is to compare the objects that
# the variables are pointing to
# default behavior
# if the variables are pointing to different objects, then == returns false
# if the variables are pointing to same objects, then == returns true
print(raghu == sarayu)
print(raghu == raghu1)
# print(raghu.__eq__(raghu1))
print(raghu == raghu2)

print(raghu == raghu3)