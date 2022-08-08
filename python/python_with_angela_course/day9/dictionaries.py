# Dictionaries are made up of key value pairs.
# the values are the data and the keys are the values defininf the datas
# Let's try creating a dictionary and learn its syntax:

python_dict = {"bug": "an error", "function": "a piece of code you can easily call again and again"}

# Now that we know the proper syntax of dictionaries
# Let's try retrieving an item from our dictionary
# Now to retrieve a key, value pair from our dictionary is kinda similar to retrieving items from lists
# The only difference is that values are identified by their key
# Let's try retrieving the "an error" value from our dictionary

print(python_dict["bug"])

# Now we get the value that is being defined by the key, "bug"

# Now let's try adding a key, value pair to our dictionary
# We are going to define a new key, loop, and add a value to it

python_dict["loop"] = "A piece of code that will keep on repeating"
print(python_dict)

# We have successfully added a new key, value pair to our dictionary
# We can also create empty dictionaries in our programs just like we create empty lists:
names = {}
# You can also wipe a current dictionary empty using the same syntax


# Also, you can edit a value using a key:
python_dict["bug"] = "An error."

# The final thing we are going to learn about dictionaries right now is how to loop through them
# Syntax:

# If you wanted to loop through key, value pairs:
for key,value in python_dict.items():
    print("key: " + str(key))
    print("value: " + str(value))

# If you wanted to loop through only keys:
for key in python_dict.keys():
    print("key: " + str(key))

# If you wanted to loop through only values:
for value in python_dict.values():
    print("value: " + str(value))


# Practice Time!

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62
}

for key,value in student_scores.items():
    if value >= 91:
        student_scores[key] = "Outstanding"
    elif value >= 81 and value <= 90:
        student_scores[key] = "Exceeds Expectations"
    elif value >= 71 and value <= 80:
        student_scores[key] = "Acceptable"
    elif value <= 70:
        student_scores[key] = "Fail"

print(student_scores)