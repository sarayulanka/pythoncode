# Class variables are bound to the class. They’re shared by all instances of that class.
# The following example adds the extension and version class variables to the HtmlDocument class:

class HtmlDocument:
    extension = 'html'
    version = '5'


# Both extension and version are the class variables of the HtmlDocument class.
# They’re bound to the HtmlDocument class.

# Get the values of class variables
# To get the values of class variables, you use the dot notation (.). For example:

print(HtmlDocument.extension) # html
print(HtmlDocument.version) # 5

# Attribute errors occur when one tries to access a class variable that actually isn't existent


# Another way to get the value of a class variable is to use the getattr() function.
# The getattr() function accepts an object and a variable name. It returns the value of the class variable.
# For example:

extension = getattr(HtmlDocument, 'extension')
version = getattr(HtmlDocument, 'version')

print(extension)  # html
print(version)  # 5



# Setting a class variable inside a class or outside(both work)

# To set a value for a class variable, you use the dot notation:

# HtmlDocument.version = 10

# or you can use the setattr() built-in function:

# setattr(HtmlDocument, 'version', 10)

# Since Python is a dynamic language, you can add a class variable to a class at runtime
#  after you have created it. For example, the following adds the media_type class variable 
# to the HtmlDocument class:

# HtmlDocument.media_type = 'text/html'
# print(HtmlDocument.media_type)

# Similarly, you can use the setattr() function:
# setattr() function syntax: setattr(class_name, class_variable, new_value)

# setattr(HtmlDocument, media_type, 'text/html')
# print(HtmlDocument.media_type)


# To delete a class variable at runtime, you use the delattr() function:
delattr(HtmlDocument, 'version')

# Or you can use the del keyword:
del HtmlDocument.extension


# Class variable storage
# Python stores class variables in the __dict__ attribute. The __dict__ is a mapping proxy,
#  which is a dictionary. For example:

from pprint import pprint

class HtmlDocumentTwo:
    extension = 'html'
    version = '5'

HtmlDocument.media_type = 'text/html'
pprint(HtmlDocument.__dict__)

# you can use the setattr() function or dot notation to indirectly change the __dict__ attribute.
# Also, the key of the __dict__ are strings that will help Python speeds up the variable lookup.

# Although Python allows you to access class variables through the __dict__ dictionary,
# it’s not a good practice. Also, it won’t work in some situations. For example:

# print(HtmlDocument.__dict__['type']) -> BAD CODE