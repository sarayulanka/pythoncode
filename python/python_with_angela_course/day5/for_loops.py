# Today, we are going to talk about for loops
# but to understand for loops, we first need to understand loops
# loops are just blocks of code designed to repeat actions over and over

# Now, we know what loops are, so what are for loops?
# for loops are loops that take each individual value out of a list 
# so that you can do something with it each time
# Now, for loops are hard to understand with words so let's try making one!

friends = ["shloka", "sruthi", "adhya"]

# Now, the first word we put to start a for loop is for
# Then we create a temporary variable which you can name anything
# This variable is only for the loop and it will hold each value every time the loop starts again
# Let's start making the for loop

for friend in friends:
    print(f"{friend} is my friend!")

# Each time a loop starts again, it's called an iteration
# It's important to remember that each time the iteration starts again, 
# the variable or in this case, friend, will hold a new value in the list
# which is why it is printing a new friend's name each time


# Practice Time!
# You are going to write a program that calculates the average student height from a List of heights. 

student_heights = [180, 124, 165, 173, 189, 169, 146]
number = 0
sums = 0

for height in student_heights:
    sums += height
    number += 1

print(round(sums/number))


# Let's do another practice problem!
# You are going to write a program that calculates the highest score from a List of scores.

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print("The highest score in the class is: " + str(highest_score))