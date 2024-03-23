import pandas as pd

phonetic_df = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dic = {row.letter: row.code for (index, row) in phonetic_df.iterrows()}

# print(phonetic_dic)  # to check

is_on = True

while is_on:
    def generate_phonetic():
        word_to_code = input("Enter the word to be coded :").upper()
        if word_to_code == "OFF":
            is_on = False

        try:
            word_to_code = [phonetic_dic[letter] for letter in word_to_code]

        except KeyError:
            print("Sorry, only letters in the alphabet please")
            generate_phonetic()
        else:
            print(word_to_code)

    generate_phonetic()



        # letters_to_code = [letter for letter in word_to_code]
        # word_coded = [phonetic_dic[letter] for letter in word_to_code]
        # print((word_coded))



# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
