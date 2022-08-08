# A while loop is a block of code that will kepp on doing an action as long as a condition is true
#  when the condition becomes false, the while loop will stop running
# The syntax is:
# while something is true:
#    do this action

# let's try making a while loop:

number = 0

while number <= 100:
    print(number)
    number += 5

# See? Until number became greater than 100, the while loop kept on printing number
# The while loop kept on repeating the action I told it to until finally, number was greater than 100

# Now you might be asking when should you use for loops and when should you use while loops?
# For loops are ideal when you want you want to iterate over something and do something
# to each value that you iterate over.
# Now, while loops are great to use when you want to do a repeated action only while a 
# specific condition is true.


# Now let's say that we have a while loop
# The while loop has a condition that will never be false
# What will happen?
# Those types of while loops are called infinite loops
# It is because the action you told the loop to do will 
# keep on happening because the condition never becomes false
