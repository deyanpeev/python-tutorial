LETTERS_TO_EXCLUDE = ['a', 'e', 'i', 'o', 'u']

words = ["vowel", "consonant"]
new_words = []

for word in words:
    new_word = [] # the word will be array of characters wich will later be joined in a string
    for letter in word:
        if letter.casefold() not in LETTERS_TO_EXCLUDE:
            new_word.append(letter)
    new_words.append("".join(new_word))

print(new_words)
