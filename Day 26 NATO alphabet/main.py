import pandas

data = pandas.read_csv("Day 26 NATO alphabet/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    output_list = []
    for letter in word:
        if letter in phonetic_dict:
            output_list.append(phonetic_dict[letter])
        else:
            print(f"Sorry, '{letter}' is not a letter in the alphabet.")
            break
    else:
        print(output_list)
        return

    generate_phonetic()

generate_phonetic()
