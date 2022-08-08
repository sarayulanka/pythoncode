
def one_tree(num):
    string_num = ""

    for x in range(1, num+1):
        string_num += "\n"
        for y in range(1, x+1):
            string_num += "1"
    return string_num


print(one_tree(int(input())))
