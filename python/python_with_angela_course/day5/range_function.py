# Recently, we have been learning how to use the for loop to iterate over lists
# But we can also iterate over a range of numbers using the range function
# A range function is really helpful if you want to do something with a range of numbers
# Now let's try looping over a range of numbers using for loop
# Example:

for number in range(1,10):
    # the number describing the end of the range will not be included in the range
    # For example, the 10 I put for the end number will not be part of the range
    print(number)

# Practice time!
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100
# 2595
sums = 0

for number in range(1, 101):
    if number % 2 == 0:
        sums += number

print(sums)


# Let's do some more practice!

for number in range(1, 101):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)