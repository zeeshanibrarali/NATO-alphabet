# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#   Access key and value
#   pass

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
# Access index and row
# Access row.student or row.score
# pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

# TODO 1. Create a dictionary in this format:
list_of_words = pandas.read_csv('nato_phonetic_alphabet.csv')
paper = {row.letter: row.code for (index, row) in list_of_words.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
all_alphabets = False
while not all_alphabets:
    try:
        user_input = input('Please enter name to find code : ').upper()
        result = [paper[letter1] for letter1 in user_input]
        all_alphabets = True
    except KeyError:
        print('\tSorry, We accept only alphabets')
        all_alphabets = False
    else:
        print(result)
