TEST_NUM = int(input())

for testnum in range(TEST_NUM):
    num = int(input())
    test = []
    answer = []

    for _ in range(num):
        test.append(input().split("*"))

    for i in range(num):
        if i == 0:
            for j in range(len(test[i])):
                answer.append(test[i][j])

        else:
            for j in range(len(test[i])):
                if j == 0:
                    if test[i][j] == ' ' or test[i][j] in answer[0] or answer == "*": pass
                    elif answer[0] == ' ' or answer[0] in test[i][j]: answer[0] = test[i][j]
                    else: answer = "*"
                elif j == len(test[i]) - 1:
                    if test[i][j] == ' ' or test[i][j] in answer[-1] or answer == "*": pass
                    elif answer[-1] == ' ' or answer[-1] in test[i][j]: answer[-1] = test[i][j]
                    else: answer = "*"
                
    print("Case #{}:".format(testnum+1), end=" ")
    print(*answer, sep="")