# Lambda is the short form for function definition
# list comprehension is short form for for loop

nums = list(range(1, 11))
product = []
for num in nums:
    product.append(num * 5)

print(product)
print(nums)

# using list comprehension
# syntax for list comprehension
# [expression for variable in list]
prodnum5 = [num * 5 for num in nums]
print(prodnum5)

# multiply even number with any number = even number
# multiple odd number with any number = even if even, odd if odd

# filter using list comprehension
# syntax [variable for variable in list if condition]
nums = list(range(1, 11))
evennums = [x for x in nums if x % 2 == 0]
print(evennums)
# syntax [expression for variable in list if condition]
prodeven5nums = [x * 5 for x in nums if x % 2 == 0]
print(prodeven5nums)

prod5 = lambda x: x * 5
prodeven5nums = [prod5(x) for x in nums if x % 2 == 0]
print(prodeven5nums)
