[A, B, C] = list(map(int, input().split()))
x = 1
b = []
current = -1
answer = 1

while(B>=x):
    x *= 2

while(x!=1):
    x /= 2
    if (B>=x):
        b.append(1)
        B -= x
    else:
        b.append(0)

while(b != []):
    K = b.pop()
    # print(f"K is {K}")

    if (current == -1):
        current = A%C
    else:
        current = (current*current)%C
    # print(f"current is {current}")

    if (K==1):
        answer *= current
        answer %= C
    # print(f"current answer is {answer}")

print(answer)