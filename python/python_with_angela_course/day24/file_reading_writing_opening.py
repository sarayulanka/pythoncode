# In python, we can do many things with a file
# The things we are going to learn to do with a file today are opening a file, reading a file, 
# writing to a file, and closing a file.

# To demonstrate the steps, let's first create a text file call my_file.txt
# One we have done that, we are ready to go through the steps!

# The first step is to open the file you wish to do something with:
# P.S. the syntax for opening a file is this: 
# open(filename in quotes, mode: the mode which you want to open the file in)
# Sometimes it might be hard to remember to close the fileand so to make it easier,
# there is a way to not have to remember to close the file and that is by using with
# The way to use it is below:

with open('my_file.txt', mode='w') as file:
    # The second step is to read or write to the file:
    # The syntax for writing to a file is variablename.write('whatever text you want to add')
    file.write('Because I know how to write to a file, I can add content to this file!')

with open('my_file.txt') as file:
    # The syntax for reading a file is variable_name.read(), this will print whatever text is in the file
    content = file.read()
    print(content)