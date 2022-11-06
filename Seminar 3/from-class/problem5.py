EMPTY_SPACE = ' '
CHAR_TO_REPEAT = '*'

lines_number = int(input("Enter a number: "))
line = 0
while line < lines_number:
    print(EMPTY_SPACE * (lines_number - line - 1) + CHAR_TO_REPEAT * (line * 2 + 1))
    line+=1