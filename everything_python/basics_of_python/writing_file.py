# The following illustrates how to write a string to a text file:

# with open('readme.txt', 'w') as f:
#     f.write('readme')
# Code language: JavaScript (javascript)
# Steps for writing to text files
# To write to a text file in Python, you follow these steps:

# First, open the text file for writing (or appending) using the open() function.
# Second, write to the text file using the write() or writelines() method.
# Third, close the file using the close() method.
# The following shows the basic syntax of the open() function:

# f = open(path_to_file, mode)
# The open() function accepts many parameters. But you’ll focus on the first two:

# The path_to_file parameter specifies the path to the text file that you want to open for writing.
# The mode parameter specifies the mode for which you want to open the text file.
# For writing to a text file, you use one of the following modes:

# Mode	Description
# 'w'	Open a text file for writing text
# 'a'	Open a text file for appending text
# The open() function returns a file object. And the file object has two useful methods for writing text to the file: write() and writelines().

# The write() method writes a string to a text file and the writelines() method write a list of strings to a file at once.

# In fact, the writelines() method accepts an iterable object, not just a list, so you can pass a tuple of strings, a set of strings, etc., to the writelines() method.

# To write a line to a text file, you need to manually add a new line character:

# f.write('\n')
# f.writelines('\n')
# Code language: JavaScript (javascript)
# And it’s up to you to add the new line characters.

# Writing text file examples
# The following example shows how to use the write() function to write a list of texts to a text file:

# lines = ['Readme', 'How to write text files in Python']
# with open('readme.txt', 'w') as f:
#     for line in lines:
#         f.write(line)
#         f.write('\n')
# Code language: JavaScript (javascript)
# If the readme.txt file doesn’t exist, the open() function will create a new file.


# The following shows how to write a list of text strings to a text file:

# lines = ['Readme', 'How to write text files in Python']
# with open('readme.txt', 'w') as f:
#     f.writelines(lines)
# Code language: JavaScript (javascript)
# If you treat each element of the list as a line, you need to concatenate it with the newline character like this:

# lines = ['Readme', 'How to write text files in Python']
# with open('readme.txt', 'w') as f:
#     f.write('\n'.join(lines))
# Code language: JavaScript (javascript)

# Appending text files
# To append to a text file, you need to open the text file for appending mode. The following example appends new lines to the readme.txt file:

# more_lines = ['', 'Append text files', 'The End']
# with open('readme.txt', 'a') as f:
#     f.writelines('\n'.join(more_lines))
# Code language: JavaScript (javascript)
# Output:


# Writing to a UTF-8 text file
# If you write UTF-8 characters to a text file using the code from the previous examples, you’ll get an error like this:

# UnicodeEncodeError: 'charmap' codec can't encode characters in position 0-44: character maps to <undefined>
# Code language: HTML, XML (xml)
# To open a file and write UTF-8 characters to a file, you need to pass the encoding='utf-8' parameter to the open() function.

# The following example shows how to write UTF-8 characters to a text file:


# quote = '成功を収める人とは人が投げてきたレンガでしっかりした基盤を築くことができる人のことである。'

# with open('quotes.txt', 'w', encoding='utf-8') as f:
#     f.write(quote)
# Code language: JavaScript (javascript)
# Summary
# Use the open() function with the w or a mode to open a text file for appending.
# Always close the file after completing writing using the close() method or use the with statement when opening the file.
# Use write() and writelines() methods to write to a text file.
# Pass the encoding='utf-8' to the open() function to write UTF-8 characters into a file.