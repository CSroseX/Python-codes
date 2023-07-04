import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
dict  = {row.letter: row.code for (index,row) in data.iterrows()} #dictionary comprehension
 
word = input('Enter a word : ').upper()
output_list = [dict[letter] for letter in word] #list comprehension
print (output_list)
