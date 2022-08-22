from unicodedata import name


class Person:
    def __init__(self, name, age, birthPlace):
        self.name = name
        self.age = age
        self.birthPlace = birthPlace

    def __hash__(self) -> int:
        return hash(self.name + self.birthPlace)

    def __del__(self):
        # This is like a precautionary warning by the GC that its going to delete the object
        print('deleting object: ' + self.name)


p1 = Person('John', 36, 'Baltimore')
p2 = Person('Jane', 32, 'Miami')
p3 = Person('John', 40, 'Baltimore')

print(hash(p1))
print(hash(p2))
print(hash(p3))
# p3.name = 'Chris'
# print(hash(p3))

print(p1 == p3)

# __del__

# Garbage collector : This will be used to delete the objects that are no longer referenced or used
# You dont have to do anything to delete the objects created
# Garbage collector will take care of deleting the object so that the memory can be reallocated for something else
# __del__: This method is called by the garbage collector before deleting the object
# so once the execution of __del__ method is complete then GC will go ahead and delete the object
# why do we need __del__ method
# one of the use cases for __del__ is if you want to preserve the state of the object before deleting
# State of the object: It is very simple. It means the current values for all the attributes of an object
