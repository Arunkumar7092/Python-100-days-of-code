import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(data)
# new_dict = {}
# for (index, row) in df.iterrows():
#     new_dict[row.letter] = row.code
# print(new_dict)
dictionary = {row.letter: row.code for (index, row) in df.iterrows()}
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter your name:").upper()
name_list = [dictionary[letter] for letter in name]
print(name_list)