numbers = [-1, -4, -5, 6, 7, 8, 9]
new_numbers = []

if len(numbers) <= 4:
    new_numbers.append(0)
else:
    for x in range(1, 5):
        num = max(numbers)
        new_numbers.append(num)
        numbers.remove(num)


print(sum(new_numbers))
