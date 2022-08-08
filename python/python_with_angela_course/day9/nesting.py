# Nesting is storing data storage types in different data storage types
# For example putting lists in dictionaries or making a list of dictionaries
# Let's try putting a list as a value in a dictionary
list_dict = {"names": ["sarayu", "sruthi", "shloka", "adhya"]}

# We can also make a list of dictionaries

dictionary_a = {"name": "sarayu"}
dictionary_b = {"name": "sarayu"}
dictionary_c = {"name": "sarayu"}

list_of_dicts = [dictionary_a, dictionary_b, dictionary_c]

# You can also nest dictionaries into dictionaries as well as nesting lists into lists

# Dictionaries into dictionaries look like this:
dict_of_dicts = {"ages": {"age": 9, "age" : 10}}

# A list of lists would look like this:
list_of_lists = [[1, 2, 3], [4, 5, 6]]


# Practice Time!
# You are going to write a program that adds to a travel_log. 
# Write a function that will work to add the entry for Russia

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},]

def add_new_country(country, amount, cities):
    new_dictionary = {}
    new_dictionary["country"] = country
    new_dictionary["visits"] = amount
    new_dictionary["cities"] = cities
    travel_log.append(new_dictionary)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)