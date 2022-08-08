friends = ["Shloka", "Sruthi", "Adhya", "Natalie", "Charlotte"]

# This is applying filter criteria using list comprehension
# Here there will only be if

filtered_friends = [x for x in friends if x[:2].lower() == "sh"]
print(filtered_friends)


numbers = list(range(1, 21))
fibonacci_series = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
not_in_fibonacci = []

for number in numbers:
    if number not in fibonacci_series:
        not_in_fibonacci.append(number)
    else:
        continue

print(not_in_fibonacci)

not_in_fibonacci2 = [number for number in numbers if number not in fibonacci_series]
print(not_in_fibonacci2)
