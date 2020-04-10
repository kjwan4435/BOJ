num = int(input())
for _ in range(num):
    string = input()
    cnt = 0
    score = 0
    for i in range(len(string)):
        if string[i] == 'O':
            cnt +=1
            score += cnt
        else: 
            cnt = 0
    print(score)