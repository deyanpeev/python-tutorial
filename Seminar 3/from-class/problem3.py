CHAR_TO_REPEAT = '*'

lines_number = int(input("Enter a number: "))
for i in range(0, lines_number):
    print(CHAR_TO_REPEAT * (i + 1))