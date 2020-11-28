import sys

S = sys.stdin.readline().replace("\n", "")
count_0 = 0
count_1 = 0
for i in range(len(S)):
    if S[i] == "0":
        count_0 += 1
    elif S[i] == "1":
        count_1 += 1
count_0 = int(count_0/2)
count_1 = int(count_1/2)

answer = []
answer_0 = 0
answer_1 = 1
for i in range(len(S)):
    if S[i] == "0" and answer_0 < count_0:
        answer_0 += 1
        answer.append(S[i])
    elif S[i] == "1" and answer_1 <= count_1:
        answer_1 += 1
    elif S[i] == "1" and answer_1 > count_1:
        answer_1 += 1
        answer.append(S[i])

print(''.join(answer))
