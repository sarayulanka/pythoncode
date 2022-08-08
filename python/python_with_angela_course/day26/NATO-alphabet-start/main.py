import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

alphabet_file = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet_file.to_dict()

phonetic_alphabet = {row.letter: row.code for (index, row) in alphabet_file.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input('Please write a word:  ')
letter_list = [letter for letter in user_input]

result = [phonetic_alphabet[letter.upper()] for letter in letter_list]
print(result)