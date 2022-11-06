EMPTY_SPACE = ' '
CHAR_TO_REPEAT = '*'

lines_number = int(input("Enter a number: "))
line = 1
while line <= lines_number:
    print(EMPTY_SPACE * (lines_number - line) + CHAR_TO_REPEAT * line)
    line+=1