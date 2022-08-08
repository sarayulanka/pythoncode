# Today, we are going to focus on a strategy called debugging
# Well, we do know what bugs mean: bugs are little accidental errors that we create in our code
# debugging is a strategy on how to fix the bugs and how to look over your code so that you can find the bugs easily
# We will dive straight in to this concept today and learn it thoroughly

# Today we are going to learn tips, tricks, and techniques to being able to debug quickly.

# First step to debugging quickly:
# Describing the problem

# To debug quickly, you first have to understand the problems in your code. What isn't working and why isn't it working?
# If you don't fully understand the problem and are not able to describe the problem, then you won't be able to debug  it quickly
# We are going to take some examples and try describing and understanding the problem

def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")
my_function()

# Above this line, I have written a function
# the functioon is supposed to print "you got it!" when i becomes 20 but it never printed you got it!
# The problem is that the range will only go up till 20 not including 20
# so i is going up till 19 and not 20
# Therefore, i is never going to become twenty and that is why it never printed "You got it!"
# Now because we were able to describe the problem, we are going to be able to fix it
# Let us fix this function:

def my_function2():
    for i in range(1, 21):
        if i == 20:
            print("You got it!")
my_function2()

# Now i will become 20 at the end and it will print "You got it!"
# because we described the problem and we were able to fully understand the problem, we were able to fix it!


# Second step to debugging quickly and thoroughly:
# Reproducing the bug


# By trying to recreate the same bug, you will be able to know what is causing the bug and where the bug is happening
# Let's try debugging a new piece of code using this step:

# Dice images are getting printed from the list but every once in a while, we are getting an index error
# Let's try analyzing where the problem is coming from using the strategy of reproducing the bug:

from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# The problem is that when using randint, both endpoints are included unlike the range function so 6 is included but 
# the list doesn't have an element that has an index of 6 which is why we are getting a name error
# Let's try fixing it below:

dice_imgs2 = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num2 = randint(0, 5)
print(dice_imgs2[dice_num2])

# Now we won't be getting an index error which means we solved the problem!


# Third step to debugging quickly and thoroughly:
# Play computer and evaluate each line:

# When we run our code, the computer goes through each line of our code carefully and does exactly what you tell it to do
# If there is a problem or bug in your code, the computer will inform you by telling you that there's an error
# But what if we act like the computer and evaluate through our code line by line?
# This can help us because if we think like a computer, we will be able to spot the bug easily

# Let's try another program and spot the bug using this new strategy:

year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

# The problem is that if we put 1980 or 1994 as our input, we never specified what to do with those numbers
# We only specified what to do with greater than or less than numbers
# Let's go through it like how a computer would
# Year will equal 1994
# now it will go through the if condition. It is greater than 1980 but not less than 1994
# It is also not greater than 1994, so none of the conditions are met
# Now let's fix the problem now that we know what it is:

if year >= 1980 and year <= 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")



# Fourth step to debugging quickly and thoroughly:
# Being aware of red squiggly lines

# Now this next tip is pretty straightforward all it means is that when there is an error or bug somewhere in your code,
# there will probably be a red or yellow squiggly line underneath the code
# If it's there, it means there is an error where the red or yellow squiggly line is.



# Fifth step to debugging quickly and thoroughly:
# Using print statements to find errors

# Print statements are helpful and can be used to see when things are going wrong and where the bug is
# We can print each step out and see where something goes wrong
# You can always trust the print statement to do this for you
# Let's try getting out the bugs below by using the print statement


pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)
word_per_page == int(input("Number of words per page: "))
print(word_per_page)
total_words = pages * word_per_page
print(total_words)

word_per_page2 = int(input("Number of words per page: "))
total_words2 = pages * word_per_page2
print(total_words2)


# By using the print, I found out where my program went wrong
# Instead of putting one equal sign, there was two equal signs when creatin a variable called word_per_page
# I fixed the problem easily all because of my trusty print statement strategy!



# These are many of the ways to start debugging quickly and accurately!