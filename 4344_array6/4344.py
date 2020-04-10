num = int(input())
for _ in range(num):
    uni = list(map(int, input().split()))
    avg = sum(uni[1:])/uni[0]
    count = 0
    for i in range(1,uni[0]+1):
        if uni[i] > avg: count+=1
    print("{0:0.3f}".format(count/uni[0]*100) + "%")
