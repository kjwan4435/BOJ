import sys

S = sys.stdin.readline().replace("\n", "")
zero = int(S.count("0")/2)
one = (int(len(S)/2)-zero)
print(len(S))
print(zero)
print(one)
answer = "0"*zero+"1"*one
print(answer)