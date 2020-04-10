[A, B, C] = list(map(int, input().split()))

counter = 1
answer = []
pcheck = 1

answer.append(A%C)
while((A*answer[-1])%C not in answer):
    if counter == B: break
    answer.append((A*answer[-1])%C)
    counter +=1

if (B == 1):
    print(answer[0])
elif (B == len(answer)):
    print(answer[-1])
elif (B > len(answer)):
    pre = (answer.index((answer[-1]*A)%C))
    answer = answer[pre:]
    print(answer[(B-pre)%len(answer)-1])
