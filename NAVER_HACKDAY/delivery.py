def solution(n, delivery):
    ansArray = ["?" for _ in range(n)]
    for i in range(len(delivery)): # 정답일 경우 우선 O 처리
        if delivery[i][2] == 1:
            ansArray[delivery[i][0]-1] = "O"
            ansArray[delivery[i][1]-1] = "O"
    for i in range(len(delivery)): # 정답이 아니고 O와 짝인 친구들 모두 X 처리
        if delivery[i][2] == 0:
            if ansArray[delivery[i][0]-1] == "O":
                ansArray[delivery[i][1]-1] = "X"
            elif ansArray[delivery[i][1]-1] == "O":
                ansArray[delivery[i][0]-1] = "X" 
            else: # 정답이 아니고 O와 짝이 아닌 친구들은 모르는 거니까 모두 ?처리
                if ansArray[delivery[i][0]-1] != "X":
                    ansArray[delivery[i][0]-1] = "?"
                if ansArray[delivery[i][1]-1] != "X":
                    ansArray[delivery[i][1]-1] = "?"
    answer = ''.join(ansArray)
    return answer