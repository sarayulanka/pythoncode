# In this file, we are going to be doing a challenge
# The challenge is to take the squirrel data, take a few rows, 
# and lastly, create a new csv file with that data

# So... let's give it a try!
# The first thing we have to do is import pandas and then read the squirrel file using pandas:

import pandas 
data = pandas.read_csv('squirrel_data.csv')

# Next we have to get the column from the data called Primary Fur Color:

gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])


print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict = {
    'Fur color': ['gray_squirrels', 'black_squirrels', 'cinnamon_squirrels'],
    'Count': [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}
print(data_dict)


df = pandas.DataFrame(data_dict)
df.to_csv('new_data.csv')