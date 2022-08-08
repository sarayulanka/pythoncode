# A function with output means a function that allows you to have an output when the function completes
# Let's try creating a function that returns an output
# BTW, a function with input and a function with output are not related or connected in any way
# Now let's get on with creating a function that returns an output:

def my_function():
    result = 3 * 2
    return result

print(my_function())

# Return is a keyword that is written before whatever value you want to be outputted after the function is completed
# In this particular scenario, result is equal to 3 * 2 aka 6. By saying return result, we are making result the output of the function
# so line 10 is replacing my_function() with the result variable value which is 6
# So in the end, this will print 6

# Now let's try writing a function that takes first name and last name and converts them into a title case
# Hint: there is a title function

def title_name(first_name, last_name):
    return first_name.title() + " " + last_name.title()

print(title_name("sArAYU", "LANKA"))

# We returned the first name and last name in a certain way so when we printed the function that format was the output we got

# Practice Time!
# You are going to create a function called `days_in_month()` which will take a **year** and a **month** as inputs, e.g.
# And it will use this information to work out the **number of days in the month**, then **return** that as the **output**

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "True"
            else:
                return "False"
        else:
             return "True"
    else:
        return "False"

def days_in_month(year1, month1):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year1) == "True":
    if month1 == 2:
      return month_days[month1 - 1] + 1
  else:
    return month_days[month1 - 1] 
  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)