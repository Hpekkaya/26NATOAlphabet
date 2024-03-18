import pandas as pd

phonetic_df = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dic = {row.letter: row.code for (index, row) in phonetic_df.iterrows()}

# print(phonetic_dic)  # to check

is_on = True

while is_on:
    word_to_code = input("Enter the word to be coded :").upper()
    letters_to_code = [letter for letter in word_to_code]
    print(letters_to_code)

    if word_to_code == "OFF":
        is_on = False
        break

    word_coded = [phonetic_dic[letter] for letter in word_to_code]
    print((word_coded))



# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
