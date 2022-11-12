names = ["ivan", "petkan", "gosho", "petkan", "ivan", "stamat", "ivan", "petkan", "ivan"]

names_counter = dict()
for name in names:
    if name in names_counter.keys():
        names_counter[name] += 1
    else:
        names_counter[name] = 1

for name in names_counter:
    print(name, '-', names_counter[name])