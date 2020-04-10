import sys

[NUM, LENGTH] = list(map(int, sys.stdin.readline().replace("\n", "").split()))
BRANCH = list(map(int, sys.stdin.readline().replace("\n", "").split()))

sumBranch = sum(BRANCH)
maxBranch = max(BRANCH)

def findTake(minVal,maxVal):
    meanVal = int((minVal+maxVal)/2) # 자동으로 내림된다.
    cuttedBranchSum = 0
    for i in range(NUM):
        if BRANCH[i] < meanVal: cuttedBranchSum+=BRANCH[i]
        else: cuttedBranchSum+=meanVal
    if ((sumBranch - cuttedBranchSum == LENGTH)):
        return meanVal
    if ((minVal == meanVal) or (meanVal == maxVal)):
        if (sumBranch - cuttedBranchSum > LENGTH):
            return meanVal
        else:
            return findTake(minVal-1, maxVal)
    if (sumBranch - cuttedBranchSum > LENGTH):
        return findTake(meanVal, maxVal)
    else:
        return findTake(minVal, meanVal)
    
answer = findTake(0,maxBranch)
print(answer)