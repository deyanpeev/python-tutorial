letters = ['a', 'b', 'c']
custom_string = "some random string"
for letter in letters:
    if letter not in custom_string:
        print(False)
        exit()
print(True)