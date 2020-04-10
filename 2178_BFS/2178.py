[N, M] = list(map(int, input().split()))
maze = []
visited = [[0 for _ in range(M)] for _ in range(N)]
counter = [[0 for _ in range(M)] for _ in range(N)]
Q = []

for i in range(N):
    maze.append(list(map(int, input())))

def BFS():
    while(len(Q)>0):
        [row, col] = Q.pop(0)

        if (row>0):
            if (visited[row-1][col]==0 and maze[row-1][col] == 1):
                Q.append([row-1,col]) 
                visited[row-1][col]=1
                counter[row-1][col] += counter[row][col]+1

        if (col>0):
            if (visited[row][col-1]==0 and maze[row][col-1] == 1):
                Q.append([row,col-1])
                visited[row][col-1]=1
                counter[row][col-1] += counter[row][col]+1

        if (row<N-1):
            if (visited[row+1][col]==0 and maze[row+1][col] == 1):
                Q.append([row+1,col]) 
                visited[row+1][col]=1
                counter[row+1][col] += counter[row][col]+1

        if (col<M-1):
            if (visited[row][col+1]==0 and maze[row][col+1] == 1):
                Q.append([row,col+1])
                visited[row][col+1]=1
                counter[row][col+1] += counter[row][col]+1

        
Q.append([0,0])
visited[0][0] = 1
counter[0][0] = 1
BFS()
print(counter[N-1][M-1])