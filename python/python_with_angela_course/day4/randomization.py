# We are going to talk about randomization
# Randomization is the process of making something random
# Now you might ask what that has to do with python
# Well, computers are what you called deterministic which means
# that computers do repeated and predictable actions 
# But there is a way to make computers do random things and that involves the random module
# First, to access the random module, we have to import it like this:

import random


# There are many things we can randomize using the random module
# For example the randint function in the random module will pick a 
# random integer within the range you give it
# Let's try it!

print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))

# Now notice how every time I print the variable, it will give a different number between 1 and 10?
# all of these numbers have no pattern or predictability and they are just random numbers
# also notice how all the numbers are within the range of 1 and 10?
# that is the range I put inside of the circle brackets



# Now let's try getting a random float number instead of an integer.
# Let's try it!

print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())

# Practice Time!
# Create a program that randomly says Heads or Tails!

coin_toss = random.randint(0, 1)

if coin_toss == 0:
    print("Heads")
else:
    print("Tails")