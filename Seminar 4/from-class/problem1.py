names = ['ivan', 'petkan', 'stamat', 'ivan', 'pencho', 'pencho', 'ivan']

names_counter = dict()
for name in names:
    if name in names_counter.keys():
        names_counter[name] += 1
    else:
        names_counter[name] = 1

for name in names_counter:
    print(name, ' ', names_counter[name])