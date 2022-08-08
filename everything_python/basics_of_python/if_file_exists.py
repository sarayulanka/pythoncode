# When processing files, you’ll often want to check if a file exists before doing something else with it such as reading from the file or writing to it.

# To do it, you can use the exists() function from the os.path module or is_file() method from the Path class in the pathlib module.

# os.path.exists() function
# from os.path import exists

# file_exists = exists(path_to_file)
# Code language: JavaScript (javascript)
# Path.is_file() method
# from pathlib import Path

# path = Path(path_to_file)

# path.is_file()
# Code language: JavaScript (javascript)
# 1) Using os.path.exists() function to check if a file exists
# To check if a file exists, you pass the file path to the exists() function from the os.path standard library.

# First, import the os.path standard library:

# import os.path
# Code language: JavaScript (javascript)
# Second, call the exists() function:

# os.path.exists(path_to_file)
# Code language: CSS (css)
# If the file exists, the exists() function returns True. Otherwise, it returns False.

# If the file is in the same folder as the program, the path_to_file is just simply the file name.

# However, it’s not the case, you need to pass the full file path of the file. For example:

# /path/to/filename
# Even if you run the program on Windows, you should use the forward-slash (/) to separate the path. It’ll work across Windows, macOS, and Linux.

# The following example uses the exists() function to check if the readme.txt file exists in the same folder as the program:

# import os.path

# file_exists = os.path.exists('readme.txt')

# print(file_exists)
# Code language: JavaScript (javascript)
# If the readme.txt file exists, you’ll see the following output:

# True
# Code language: PHP (php)
# Otherwise, you’ll see False on the screen:

# False
# Code language: PHP (php)
# To make the call to the exists() function shorter and more obvious, you can import that function and rename it to file_exists() function like this:

# from os.path import exists as file_exists

# file_exists('readme.txt')
# Code language: JavaScript (javascript)
# 2) Using the pathlib module to check if a file exists
# Python introduced the pathlib module since the version 3.4.

# The pathlib module allows you to manipulate files and folders using the object-oriented approach. If you’re not familiar with object-oriented programming, check out the Python OOP section.

# First, import the Path class from the pathlib module:

# from pathlib import Path
# Code language: JavaScript (javascript)
# Then, instantiate a new instance of the Path class and initialize it with the file path that you want to check for existence:

# path = Path(path_to_file)
# Finally, check if the file exists using the is_file() method:

# path.is_file()
# Code language: CSS (css)
# If the file doesn’t exist, the is_file() method returns False. Otherwise, it returns True.

# The following example shows how to use the Path class from the pathlib module to check if the readme.txt file exists in the same folder of the program:

# from pathlib import Path

# path_to_file = 'readme.txt'
# path = Path(path_to_file)

# if path.is_file():
#     print(f'The file {path_to_file} exists')
# else:
#     print(f'The file {path_to_file} does not exist')
# Code language: PHP (php)
# If the readme.txt file exists, you’ll see the following output:

# The file readme.txt exists
# Code language: CSS (css)
# Summary
# Use os.path.exists() function or Path.is_file() method to check if a file exists
