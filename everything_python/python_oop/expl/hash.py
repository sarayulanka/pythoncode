class Person:
    # every object creation involved invoking the __init__ method <- constructor
    # which means when you do Person(), __init__ is executed
    # you dont execute this method seperately
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash(self.name)

raghu = Person('Raghu', 44)
sarayu = Person('Sarayu', 12)
raghu1 = Person('Raghu', 44)

print(raghu)
print(sarayu)
print(raghu1)

# if you execute hash(object), 
# python will invoke the __hash__ method thats implemented on the class
print(hash(raghu))
print(hash(sarayu))
print(hash(raghu1))
