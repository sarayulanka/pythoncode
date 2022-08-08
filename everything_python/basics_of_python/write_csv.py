# Steps for writing a CSV file
# To write data into a CSV file, you follow these steps:

# First, open the CSV file for writing (w mode) by using the open() function.
# Second, create a CSV writer object by calling the writer() function of the csv module.
# Third, write data to CSV file by calling the writerow() or writerows() method of the CSV writer object.
# Finally, close the file once you complete writing data to it.
# The following code illustrates the above steps:

# import csv

# # open the file in the write mode
# f = open('path/to/csv_file', 'w')

# # create the csv writer
# writer = csv.writer(f)

# # write a row to the csv file
# writer.writerow(row)

# # close the file
# f.close()
# Code language: Python (python)
# It’ll be shorter if you use the with statement so that you don’t need to call the close() method to explicitly close the file:

# import csv

# # open the file in the write mode
# with open('path/to/csv_file', 'w') as f:
#     # create the csv writer
#     writer = csv.writer(f)

#     # write a row to the csv file
#     writer.writerow(row)
# Code language: PHP (php)
# If you’re dealing with non-ASCII characters, you need to specify the character encoding in the open() function.

# The following illustrates how to write UTF-8 characters to a CSV file:

# import csv

# # open the file in the write mode
# with open('path/to/csv_file', 'w', encoding='UTF8') as f:
#     # create the csv writer
#     writer = csv.writer(f)

#     # write a row to the csv file
#     writer.writerow(row)
# Code language: PHP (php)
# Writing to CSV files example
# The following example shows how to write data to the CSV file:

# import csv  

# header = ['name', 'area', 'country_code2', 'country_code3']
# data = ['Afghanistan', 652090, 'AF', 'AFG']

# with open('countries.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write the data
#     writer.writerow(data)
# Code language: PHP (php)
# If you open the countries.csv, you’ll see one issue that the file contents have an additional blank line between two subsequent rows:


# To remove the blank line, you pass the keyword argument newline='' to the open() function as follows:

# import csv

# header = ['name', 'area', 'country_code2', 'country_code3']
# data = ['Afghanistan', 652090, 'AF', 'AFG']


# with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write the data
#     writer.writerow(data)
# Code language: PHP (php)
# Output:


# Writing multiple rows to CSV files
# To write multiple rows to a CSV file at once, you use the writerows() method of the CSV writer object.

# The following uses the writerows() method to write multiple rows into the countries.csv file:

# import csv

# header = ['name', 'area', 'country_code2', 'country_code3']
# data = [
#     ['Albania', 28748, 'AL', 'ALB'],
#     ['Algeria', 2381741, 'DZ', 'DZA'],
#     ['American Samoa', 199, 'AS', 'ASM'],
#     ['Andorra', 468, 'AD', 'AND'],
#     ['Angola', 1246700, 'AO', 'AGO']
# ]

# with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write multiple rows
#     writer.writerows(data)
# Code language: PHP (php)
# Writing to CSV files using the DictWriter class
# If each row of the CSV file is a dictionary, you can use the DictWriter class of the csv module to write the dictionary to the CSV file.

# The example illustrates how to use the DictWriter class to write data to a CSV file:

# import csv

# # csv header
# fieldnames = ['name', 'area', 'country_code2', 'country_code3']

# # csv data
# rows = [
#     {'name': 'Albania',
#     'area': 28748,
#     'country_code2': 'AL',
#     'country_code3': 'ALB'},
#     {'name': 'Algeria',
#     'area': 2381741,
#     'country_code2': 'DZ',
#     'country_code3': 'DZA'},
#     {'name': 'American Samoa',
#     'area': 199,
#     'country_code2': 'AS',
#     'country_code3': 'ASM'}
# ]

# with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(rows)
# Code language: PHP (php)
# How it works.

# First, define variables that hold the field names and data rows of the CSV file.
# Next, open the CSV file for writing by calling the open() function.
# Then, create a new instance of the DictWriter class by passing the file object (f) and fieldnames argument to it.
# After that, write the header for the CSV file by calling the writeheader() method.
# Finally, write data rows to the CSV file using the writerows() method.
# Summary
# Use the CSV Writer or the DictWriter class to write data to a CSV file.