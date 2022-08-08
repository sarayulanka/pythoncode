# 4. Write a function that takes a list of numbers and returns a boolean value if the list is monotonic which means either all the elements are increasing or decreasing
# for example: 7 9 11 14 is monotonic
# 7 9 11 5 is not monotonic

def is_monotonic(nums):
    # relations = []
    ascCount = 0
    dscCount = 0    

    for idx in range(1, len(nums)):
        if nums[idx] >= nums[idx-1]:
            # relations.append('asc')
            ascCount += 1
        else:
            # relations.append('dsc')
            dscCount += 1

    # ascCount = 0
    # dscCount = 0
    # for rel in relations:
    #     if rel == 'asc':
    #         ascCount += 1
    #     else:
    #         dscCount += 1
    
    return ascCount == len(nums) - 1 or dscCount == len(nums) - 1
     

print(is_monotonic([7, 9, 11, 14]))
print(is_monotonic([17, 15, 21, 9]))
