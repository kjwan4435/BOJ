import sys
import random

N = int(sys.stdin.readline().replace("\n", ""))
K = list(map(int, sys.stdin.readline().replace("\n", "").split()))
judge = "YES"

for i in range(N):
    if (K[i]-1)%2 != i%2:
        judge = "NO"

print(judge)