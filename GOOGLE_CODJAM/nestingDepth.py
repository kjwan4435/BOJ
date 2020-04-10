TEST_NUM = int(input())

for test in range(TEST_NUM):
    LINE = input()
    def split(list): return [num for num in list]
    NUMSET = list(map(int,split(LINE)))
    stacker = []
    currLevel = 0

    for i in range(len(NUMSET)):
        num = NUMSET[i]
        if num > currLevel:
            for _ in range(num-currLevel):
                stacker.append("(")
            stacker.append(num)
            currLevel += (num-currLevel)
        elif num == currLevel:
            stacker.append(num)
        else:
            for _ in range(currLevel-num):
                stacker.append(")")
            stacker.append(num)
            currLevel -= (currLevel-num)
        if (i == len(NUMSET)-1 and num != 0):
            for _ in range(currLevel):
                stacker.append(")")
    
    print("Case #{}:".format(test+1), end=" ")
    print(*stacker, sep="")