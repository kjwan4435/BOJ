size = int(input())
address = []
visited = [[0 for _ in range(size)] for _ in range(size)]
answer =[]
counter = -1

for i in range(size):
    address.append(list(map(int, input())))

def DFS(row,col):
    if (visited[row][col] == 0):
        visited[row][col] += 1
        if (address[row][col] == 1):
            answer[counter] +=1
            if (row>0):
                if (visited[row-1][col]==0):
                    DFS(row-1,col)     
            if (col>0):
                if (visited[row][col-1]==0):
                    DFS(row,col-1)
            if (row<size-1):
                if (visited[row+1][col]==0):
                    DFS(row+1,col)     
            if (col<size-1):
                if (visited[row][col+1]==0):
                    DFS(row,col+1)

for i in range(size):
    for j in range(size):
        if (visited[i][j] == 0 and address[i][j] == 1):
            answer.append(0)
            counter += 1
        DFS(i,j)

print(counter+1)
answer.sort()
for i in range(len(answer)):
    print(answer[i])