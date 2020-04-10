count = []
num = [0 for _ in range(10)]
for i in range(10):
    num[i] = int(input())
    if (num[i]%42 not in count):
        count.append(num[i]%42)
print(len(count))