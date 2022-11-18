from math import ceil, floor

EMPTY_SPACE = ' '
CHAR_TO_REPEAT = '*'

lines_number = int(input("Enter a number: "))
lines_number /= 2
line = 0
while line < lines_number:
    print(EMPTY_SPACE * (ceil(lines_number) - line - 1) + CHAR_TO_REPEAT * (line * 2 + 1))
    line+=1

lines_number -= 1
while lines_number >= 0:
    print(EMPTY_SPACE * (line - floor(lines_number) - 1) + CHAR_TO_REPEAT * (floor(lines_number) * 2 + 1))
    lines_number-=1