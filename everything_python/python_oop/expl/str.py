class Person:
    # every object creation involved invoking the __init__ method <- constructor
    # which means when you do Person(), __init__ is executed
    # you dont execute this method seperately
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return (f"{self.name} -- {self.age}")

    def str1(self):
        return (f"{self.name}{self.age}")

# This is the instantiation process
# which will execute __init__ method
# This assigns values to the instance variable name and age
raghu = Person('raghu', 44)
sarayu = Person('sarayu', 12)
raghu1 = Person('raghu', 44)

# Printing an object
print('printing an object')

# when you try to print an object
# python will invoke __str__ method if its defined in the class
# if not will execute the default implementation that comes with the class - even without implementing
print(sarayu)
print(sarayu.__str__())