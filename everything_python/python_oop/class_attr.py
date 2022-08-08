# To help explain what class attributes are, let's create a circle class:

class Circle:
    pi = 3.14159
    def __init__(self, radius):
        self.radius = radius
    
    def circle_area(self):
        print(f"The area of the circle is {(self.radius**2)*self.pi} sq. units.")
    
    def circumference(self):
        print(f"The circumference of a circle is {(self.radius*2)*self.pi}")
    

# In this class, radius is an instance attribute meaning that for each object, its value will vary
# However, if radius is an instance attribute, what is pi?

# Well, pi is what you would call a class attribute, which means that the value that belongs to the var pi
# doens't vary for each object or instance and stays the same. the value is shared by all the instances

# When are python class attributes useful?

# The 1st way that python class attributes are useful is that they make for perfect ways to store
# class constants. Since a constant doesn’t change from instance to instance of a class, 
# it’s handy to store it as a class attribute.

# The 2nd way that python class attributes come in handy are tracking data across all instances

# 3) Defining default values
# Sometimes, you want to set a default value for all instances of a class. 
# In this case, you can use a class attribute.

