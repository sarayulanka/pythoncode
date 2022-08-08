# Using the open() function to create a new text file
# To create a new text file, you use the open() function. The open() function has many parameters. However, we’ll focus on the first two parameters:

# f = open(path_to_file, mode)
# In this syntax, the path_to_file parameter specifies the path to the text file that you want to create.

# For creating a new text file, you use one of the following modes:

# 'w' – open a file for writing. If the file doesn’t exist, the open() function creates a new file. Otherwise, it’ll overwrite the contents of the existing file.
# 'x' – open a file for exclusive creation. If the file exists, the open() function raises an error (FileExistsError). Otherwise, it’ll create the text file.
# For example, the following creates a new file called readme.txt and write some text into it:

# with open('readme.txt', 'w') as f:
#     f.write('Create a new text file!')
# Code language: JavaScript (javascript)
# This script creates a file with the name readme.txt in the same directory where the script file locates. If you want to create a file in a specified directory e.g., docs/readme.text, you need to ensure that the docs directory exists before creating the file. Otherwise, you’ll get an exception. For example:

# with open('docs/readme.txt', 'w') as f:
#     f.write('Create a new text file!')
# Code language: Python (python)
# Error:

# FileNotFoundError: [Errno 2] No such file or directory: 'docs/readme.txt'
# Code language: JavaScript (javascript)
# In this example, Python raises an exception because the docs directory doesn’t exist. Therefore, it could not create the readme.txt file in that directory. To fix the issue, you need to create the docs directory first and then create the readme.txt file in that folder.

# Also, you can handle the exception using the try-except statement as follows:

# try:
#     with open('docs/readme.txt', 'w') as f:
#         f.write('Create a new text file!')
# except FileNotFoundError:
#     print("The 'docs' directory does not exist")
# Code language: Python (python)
# Output:

# The 'docs' directory does not exist
# Code language: plaintext (plaintext)
# If you don’t want to create a new text file in case it already exists, you can use the 'x' mode when calling the open() function:

# with open('readme.txt', 'x') as f:
#     f.write('Create a new text file!')
# Code language: Python (python)
# Summary
# Use the open() function with the 'w' or 'x' mode to create a new text file.