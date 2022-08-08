def count_sub_str(str, sub_str):
    test_str = str
    count = 0
    while test_str.find(sub_str) != -1:
        count += 1
        test_str = test_str[test_str.find(sub_str) + 1:]
    return count

print(count_sub_str('i love india, right now', 'in'))