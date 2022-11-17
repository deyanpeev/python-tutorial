# print multiple fibonacci sequences

def print_fibonacci(n):
    f,s = 1,1
    counter = 0
    result = []
    while(counter < n):
        result.append(f)
        f, s = s, f+s
        counter+=1
    print(result)

first = int(input('Enter the first number: '))
second = int(input('Enter the second number: '))
for i in range(first, second):
    print_fibonacci(i)