numbers = [3, 7, 4, 5, 1, 2, 3, 6]
sequences = []
counter = 1

for number in numbers:
    if number != numbers[-1]:
        if numbers[numbers.index(number) + 1] >= number:
            counter += 1
        else:
            sequences.append(counter)
            counter = 1

print(max(sequences))
