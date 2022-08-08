# In day 16, we learnt about how to access classes including their attributes and methods
# But sometimes, there won't be a class that will fit our requirements for our program
# And that's why we have the advantage of being able to make classes

# So the goal for today(day 17) is to be able to make classes that fit our requirements for our programs
# Earlier, in day 16, we talked about how classes are basically blueprints for objects to be made later on
# Now we can create our own blueprints for our own objects.

# To first start creating a class, we have to define the classname, like in a function
# Also the first letter of each word in the name should be capitalized, this style is called pascal case
# Let's define our class below:

class Car:
    # Now we successfully defined our class
    # Now let's talk about the different parts of a class
    # We know what attributes and methods are

    # Now there is one more part that we need to learn
    # A constructor is a part of a class that allows us to specify 
    # what should happen when our object is being constructed.


    # The first type of constuctor we are going to learn is called __init__
    #  the __init__ constuctor initializes attributes and is used when creating the attributes
    # self is the parameter that is needed every time you use __init__
    # After self, you can put as many attributes in the parenthesis as you need

    # Also you can create default attributes by 
    # not putting the attribute name as a parameter and define it like I did below

    # Default attributes are useful when you feel it doesn't make sense
    # to have to enter a value for that parameter every time you call for a certain attribute

    def __init__(self, seats, barometer):
        self.seats = seats
        self.barometer = barometer
        self.speedometer = 27

    # It's important to remember that when defining __init__ or any methods,
    # self should always be the first parameter

    # Anyway, now let's create some methods
    # Creating methods are basically the same as creating functions
    # except for self which is always the first parameter

    def barometer_checker(self, barometer):
        for number in range(1, 11):
            print(f"The barometer is increasing! It's now: {barometer}")
            print("                                                   ")
            barometer += 1

    def speedometer_checker(self):
        for number in range(1, 11):
            print(f"The speedometer is increasing! It's now: {self.speedometer}")
            print("                                                            ")
            self.speedometer += 1


# Now let's create objects from the car class below:

my_car1 = Car(4, 67)
my_car1.barometer_checker(23)
my_car1.speedometer_checker()


# Now, we know how to make classes
# In the next file, we are going to be creating a class for the first part of a project