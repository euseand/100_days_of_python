from constants import NATO_ALPHABET


word = input('Enter a word: ')
new_word = [NATO_ALPHABET[letter.upper()] for letter in word]
print(new_word)
