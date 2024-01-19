import pandas
file = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in file.iterrows()}
print(nato_dict)


def nato():
    word = input("Enter a word: ").upper()

    try:

        word_code = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        nato()
    else:
        print(word_code)

nato()

