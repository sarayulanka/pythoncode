# Unlike instance methods, static methods aren’t bound to an object. In other words, static methods 
# cannot access and modify an object state.

# In addition, Python doesn’t implicitly pass the cls parameter (or the self parameter) to static methods.
# Therefore, static methods cannot access and modify the class’s state.

# In practice, you use static methods to define utility methods or group functions
# that have some logical relationships in a class.

# To define a static method, you use the @staticmethod decorator:

# class className:
#     @staticmethod
#     def static_method_name(param_list):
#         pass

# Python static method examples
# The following defines a class called TemperatureConverter that has static methods for converting temperatures between Celsius, Fahrenheit, and Kelvin:

class TemperatureConverter:
    KEVIN = 'K',
    FAHRENHEIT = 'F'
    CELSIUS = 'C'

    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9*c/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5*(f-32)/9

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(f):
        return 5*(f+459.67)/9

    @staticmethod
    def kelvin_to_fahrenheit(k):
        return 9*k/5 - 459.67

    @staticmethod
    def format(value, unit):
        symbol = ''
        if unit == TemperatureConverter.FAHRENHEIT:
            symbol = '°F'
        elif unit == TemperatureConverter.CELSIUS:
            symbol = '°C'
        elif unit == TemperatureConverter.KEVIN:
            symbol = '°K'

        return f'{value}{symbol}'

# Static functions can't change anything and have the same output each time

