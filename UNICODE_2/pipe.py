import sys
import math

[N, K] = list(map(int, sys.stdin.readline().replace("\n", "").split()))
C = list(map(int, sys.stdin.readline().replace("\n", "").split()))
C_ = []
for i in range(len(C)):
    C_.append((i+1, C[i]))
C_ = sorted(C_, key = lambda value: value[1], reverse=True)

max_C = int(math.ceil(N/2))
index_0 = list(range(max_C))
index_1 = list(range(N-max_C))
for i in range(len(index_0)):
    index_0[i] *= 2
for i in range(len(index_1)):
    index_1[i] *= 2 
    index_1[i] += 1
index = index_1 + index_0

if (max(C)>max_C):
    print(-1)
else:
    answer = [0]*N
    for i in range(len(C_)):
        for j in range(C_[i][1]):
            answer[index[-1]] = C_[i][0]
            index.pop()
    print(' '.join(map(str, answer)))
    
