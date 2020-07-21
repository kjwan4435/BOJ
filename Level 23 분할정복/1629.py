[A, B, C] = list(map(int, input().split()))
b = []
current = -1
answer = 1

# B를 이진수로 b 리스트에 담기
x = 1
while(B>=x):x *= 2 
while(x!=1): 
    x /= 2
    if (B>=x):
        b.append(1)
        B -= x
    else: b.append(0)

# b 리스트 끝부터 시작하며 A를 B번 곱한 수를 C로 나눈 나머지를 answer에 저장
while(b != []):
    K = b.pop()
    if (current == -1): current = A%C
    else: current = (current*current)%C

    if (K==1):
        answer *= current
        answer %= C

print(answer)