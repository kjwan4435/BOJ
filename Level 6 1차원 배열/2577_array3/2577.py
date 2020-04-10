a = int(input())
b = int(input())
c = int(input())
multiply = a*b*c
multi = str(multiply)
num = [0 for _ in range(10)]
for i in range(len(multi)):
    number = int(multi[i])
    num[number] += 1 
for i in range(10):
    print(num[i])