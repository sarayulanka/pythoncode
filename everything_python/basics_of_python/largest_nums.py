# 5.  Write a function that takes a list of numbers as first parameter and a number (n) as second parameter and returns a list of n largest numbers in the list

def n_large_nums(numbers, n):
    largest_nums = []
    for i in range(1, n+1):
        largest_nums.append(max(numbers))
        numbers.remove(max(numbers))
    return largest_nums

# def n_large_nums(numbers, n):
#     largest_nums = []
#     while(len(largest_nums) < n ):
#         largest_nums.append(max(numbers))
#         numbers.remove(max(numbers))

nums = [1, 2, 3, 4, 5, 7, 7]
print(n_large_nums(nums, 2))