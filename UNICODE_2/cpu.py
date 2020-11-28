import sys
import math

N = int(sys.stdin.readline().replace("\n", ""))
C = list(map(int, sys.stdin.readline().replace("\n", "").split()))
array = []
def dp(list):
    if len(list) == 1:
        array.append(list[0])
        result = int(list[0]+1)
        return(result)
    else: 
        last = list.pop()
        x = dp(list)
        array.append(last*x)
        return last*x+1

dp(C)
print(sum(array)%int(1e9+7))

