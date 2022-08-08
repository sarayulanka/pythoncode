# JSON is a fancier file format
# JSON was originally made for javascript but it was so simple and popular that now you can use it in python

# To write using JSON, the format is json.dump()
# To read using JSON, the format is json.load()
# Lastly, to update using JSON, the format is json.update()

# Let's try using JSON below:

import json

with open('intro.json', 'w') as data_file:
    json.dump('Hello. I am writing and reading a file using json!', data_file)

with open('intro.json') as data_file:
    data = json.load(data_file)
    print(data)

data1 = json.load(data_file)
data1.update('More text!')
json.dump(data1, data_file)

data_file.close()


