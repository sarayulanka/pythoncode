# In Python, when you prefix a string with the letter r or R such as r'...' and R'...', that string becomes a raw string. Unlike a regular string, a raw string treats the backslashes (\) as literal characters.

# Raw strings are useful when you deal with strings that have many backslashes, for example, regular expressions or directory paths on Windows.

# To represent special characters such as tabs and newlines, Python uses the backslash (\) to signify the start of an escape sequence. For example:

# s = 'lang\tver\nPython\t3'
# print(s)
# Code language: Python (python)
# Output:

# lang    ver
# Python  3
# Code language: Python (python)
# However, raw strings treat the backslash (\) as a literal character, one character

