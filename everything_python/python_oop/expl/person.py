class Person:
    # every object creation involved invoking the __init__ method <- constructor
    # which means when you do Person(), __init__ is executed
    # you dont execute this method seperately
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
# This is the instantiation process
# which will execute __init__ method
# This assigns values to the instance variable name and age
raghu = Person('raghu', 44)
sarayu = Person('sarayu', 12)
raghu1 = Person('raghu', 44)
raghu2 = raghu

print(raghu.name)
print(raghu.age)
print(raghu)
print(raghu1)
print(raghu2)
print(sarayu)

# Returns false because they are pointing to different objects
print(raghu1 == raghu)

# Returns true because they are pointing to the same object
print(raghu2 == raghu)

# Printing an object
print('printing an object')
print(sarayu)


# class Vehicle:
#     def __init__(self) -> None:
#         pass



# # toyota = Vehicle()
# # print(Vehicle())
# # print(toyota)

# v1 = 'apple'
# print(v1)
# print('apple')

