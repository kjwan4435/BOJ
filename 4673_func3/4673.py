def rem(li):
    for i in range(1, 10001):
        x = (i//10000)%10+(i//1000)%10+(i//100)%10+(i//10)%10+i%10+i
        if (x < 10001 and x in li):
            li.remove(x)

li = [i for i in range(1,10001)]
rem(li)
for i in range(len(li)):
    print(li[i])