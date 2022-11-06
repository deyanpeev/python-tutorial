from tokenize import Intnumber


intlist = [1, 2, 3, 4]
print(sum(intlist))
custom_sum = 0
for intnumber in intlist:
    custom_sum += intnumber
print(custom_sum)