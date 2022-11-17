#print fiibonacci numbers

n = int(input("Enter a number: "))
f,s = 1,1
counter = 0
result = []
while(counter < n):
    result.append(f)
    f, s = s, f+s
    counter+=1

print(result)