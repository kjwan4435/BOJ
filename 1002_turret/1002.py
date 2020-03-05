import math
num = int(input())
results = []

for i in range(num):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두 원의 중심 사이의 거리를 계산
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    # 두 원의 중심이 동일하고, 반지름이 같다면 류재명이 존재할 수 있는 좌표의 개수는 무한대
    if x1 == x2 and y1 == y2 and r1 == r2: results.append(-1)
    # 교점이 두 개인 경우
    elif abs(r1 - r2) < d and r1 + r2 > d: results.append(2)
    # 교점이 한 개인 경우, 즉 접하는 경우
    elif abs(r1 - r2) == d or r1 + r2 == d: results.append(1)
    # 그 외에는 교점이 없음
    else: results.append(0)

for result in results:
    print(result)