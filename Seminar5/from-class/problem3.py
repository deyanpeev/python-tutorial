# print an array of multiple fibonacci sequences

def get_fibonacci(n):
    f,s = 1,1
    counter = 0
    result = []
    while(counter < n):
        result.append(f)
        f, s = s, f+s
        counter+=1
    return result

fibonacci_list = []
first = int(input('Enter the first number: '))
second = int(input('Enter the second number: '))
for i in range(first, second):
    fibonacci_list.append(get_fibonacci(i))
print(fibonacci_list)