# create a list of positive and negative numbers
# create new list which is a multiple of 3 and is a positive number
# then create a new list of squares of those numbers

user_input = input("Please enter a number(enter quit to stop):  ")
numbers = []

while user_input.lower() != "quit":
    number = int(user_input)
    numbers.append(number)
    user_input = input("Please enter a number(enter quit to stop):  ")


number_sort = [x ** 2 for x in numbers if x > 0 and x % 3 == 0]
print(number_sort)
