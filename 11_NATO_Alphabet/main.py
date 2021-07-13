import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output = [phonetic_dictionary[letter] for letter in word]
for key, val in enumerate(output):
    print(f"{word[key]} : {val}")

