# Now that we know about some data types including floats and integers,
# we are going to learn about how to do mathematical operations with them.
# There are many operators in python that we can use to make mathematical operations
# One of them is the plus sign which we have experimented with in the past
# there is addition, subtraction, multiplication, division, and more!

# Addition:
print(456 + 3456)

# Subtraction:
print(45 - 17)

# Multiplication
print(2 * 8)

# Division:
print(6 / 2)

# exponents or powers
print(2 ** 4)


# Practice Time!

weight = input("Please enter your weight: ")
height = input("Please enter your height: ")


BMI = int(weight) / float(height) ** 2
print(int(BMI))

# Yay!! We did it! Now we rae ready to move on to number manipulation and F strings!

# Number Manipulation:
# Let's learn a new function!
# Usually when we have a number in python like 2.66666 and we don't want the decimal,
# instead of rounding the number, the numbers after the decimal point are completely cut off
# What if you wanted to round the number instead of cutting off everything after the decimal?
# That is when the round function will come in handy!
# when you put any decimal number inside the round function, it will round the number!
# Let's try it:
print(round(345.777777777))

# Another cool thing you can do is called flaw division
# Flaw division will automatically cut off everything after the decimal point 
# if the quotient has decimals in it
# Let's try it:
# BTW, you use two slashes instead of one to do flaw division

print(10 // 3)

# Now, sometimes when you want to say 
# variable = variable + 1 (and trust me you will need to say that at some point)
# Instead of writing out that whole thing, you can say variable += 1
# you can also do variable -= 1
# Example:

score = 0
score += 1
print(score)

# You know how when you want to add strings to some things that are not strings,
# you have to use str function?
# Well, what if I were to say there was an easier way?
# The easier way is called F strings
# F strings is used to mkae it more comfortable and easy to add non-strings and strings together
# How to do it:

print(f"Your score is {score}")

# Notice how there is an F before the string?
# Well, that's what makes it an F string and it's important to remember that
# whatever non-string you want to add in the f string has to be in curly braces INSIDE the quotes
# This makes adding the non-strings to string much more convenient

# Practice Time:

age = input("What is your current age?  ")
num = 90

subtraction = 90 - int(age)

months = subtraction * 12
days = subtraction * 365
weeks = subtraction * 52

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
