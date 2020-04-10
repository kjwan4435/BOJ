TEST_NUM = int(input())

for test in range(TEST_NUM):
    num = int(input())
    parenting = [] 

    for _ in range(num):
        parenting.append(list(map(int, input().split())))
        
    # 끝나는 시간을 기준으로 정렬 후 그 안에서 시작시간을 기준으로 정렬.
    def sortingArray(array):
        array = sorted(array, key = lambda x:(x[0],x[1]))
        return array

    def greedy(array):
        num = len(array)
        answer = []
        if num>0:
            answer.append(array[0])
            for i in range(1,num):
                if array[i][0] >= answer[-1][1]: 
                    answer.append(array[i])
        return answer

    def findIndex(origin, answer):
        indexSave = []
        for i in range(len(answer)):
            indexSave.append(origin.index(answer[i]) )
        return indexSave

    def removeAnswer(origin, answer):
        for i in range(len(answer)):
            origin.remove(answer[i])
        return origin

    sortedParenting = sortingArray(parenting)
    answerOfC = greedy(sortedParenting)
    indexOfC = findIndex(parenting, answerOfC)
    removedParenting = removeAnswer(sortedParenting, answerOfC)
    answerOfJ = greedy(removedParenting)
    removedBothParenting = removeAnswer(removedParenting, answerOfJ)

    def writeAnswer(num, indexOfC):
        answer = []
        for i in range(num):
            if i in indexOfC:
                answer.append("C")
            else:
                answer.append("J")
        return answer

    answer = writeAnswer(num, indexOfC)

    if (len(removedParenting) != 0): 
        print("Case #{}:".format(test+1), end=" ")
        print("IMPOSSIBLE")
    else:
        print("Case #{}:".format(test+1), end=" ") 
        print(*answer, sep="")