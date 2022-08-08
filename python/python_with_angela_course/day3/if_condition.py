# If condition is a conditional statement that gives a certain affect based on what you choose
# If conditions's syntax will look like this:

# if condition is true:
#      do something
# else:
#      do something

# Basically, how if conditions work is that you first write if and then your condition
# If the condition is true it will go into the next line
# However, if the condition is false, it will skip to the else part and do the other thing
# Let's try an example:

water_level = 50

if water_level < 60:
    print("The water level is less than 60!")
else:
    print("The water level isn't less than 60!")

# Let's try some more practice together
# Let's try making a ticket booth program
# We have to make sure that each person is taller than 120 cm before allowing them on the ride
# But if they're not taller than 120, they can't go on the ride
# Let's try it!

# In my condition I wrote >= which means greater than or equal to,
# and there are many more symbols that you can use in your if condition
# in python, these symbols are called comparison operators

print("Welcome to the carnival!")
user_input = input("Please enter your height in centimeters:  ")
user_input_int = int(user_input)
age_input = int(input("Please enter your age: "))

if user_input_int >= 120:
    if age_input <= 18:
        print("Please pay $7.00")
    else:
        print("Please pay $12.00")
    print("You may go on the ride! Have a great time!")
else:
    print("I am sorry but you aren't allowed to go on the ride.")



# Usually, after passing the first condition,
# you want to be even more specific and put another if condition
# that is called nesting an if condition
# You can put an if condition inside of an if condition
# and that what is I did in the if condition above 
# I nested an if condition inside an if condition

# Now, usually there won't just be two choices
# Sometimes, we will be needing multiple conditions and the way to do that is called an elif statement
# An elif is what you can add after an if statement but before an else statement
# Elif can be used when multiple choices are needed
# Example:

age = int(input("Please enter your age:  "))

if age < 18:
    print("The price for your ticket will be 12 dollars.")
elif age >= 18 and age < 60:
    print("The price for your ticket will be 30 dollars.")
else:
    print("The price for your ticket will be 15 dollars")

# Practice Time:

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = int(weight) / float(height) ** 2
new_BMI = round(BMI)

if new_BMI < 18.5:
  print(f"Your BMI is {new_BMI}, You are underweight.")
elif new_BMI > 18.5 and new_BMI < 25:
  print(f"Your BMI is {new_BMI}, you have a normal weight.")
elif new_BMI > 25 and new_BMI < 30:
  print(f"Your BMI is {new_BMI}, you are slightly overweight.")
elif new_BMI > 30 and new_BMI < 35:
  print(f"Your BMI is {new_BMI}, you are obese.")
else:
  print(f"Your BMI is {new_BMI}, you are clinically obese")


# Let's Do Another!
# Practice Time 2!

year = int(input("Please enter a year:  "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size.lower() == "s":
  bill += 15
elif size.lower() == "m":
  bill += 20
else:
  bill += 25

if add_pepperoni.lower() == "y":
  if size.lower() == "s":
    bill += 2
  else:
    bill += 3

if extra_cheese.lower() == "y":
  bill += 1


print(f"Your final bill is: ${bill}.")