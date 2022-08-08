# A method is bound to the instances of a class but how exactly does it work under the hood?
# So when you define a function inside a class, it’s purely a function. However,
# when you access that function via an object, the function becomes a method.

# Therefore, a method is a function that is bound to an instance of a class.
# Example:

# Create a class
class Request:
    def send():
        print('Sent')

# And you can call the send() function via the Request class like this:

Request.send() # Sent
# The send() is a function object, which is an instance of the function 
# class as shown in the following output:
print(Request.send)

# Output:
# <function Request.send at 0x00000276F9E00310>

# The type of the send is function:
print(type(Request.send))

# Output:
# <class 'function'>

# The following creates a new instance of the Request class:
http_request = Request()

# If you display the http_request.send, it’ll return a bound method object:
print(http_request.send)

# This proves that when you define a function inside a class, it’s purely a function. However,
# when you access that function with an object, the function becomes a method.

# A method is an instance of the method class.
# A method has the first argument (self) as the object to which it is bound.

# Python automatically passes the bound object to the method as the first argument. 
# By convention, its name is self.