[V,E,start] = list(map(int, input().split()))
tree = [[] for _ in range(1001)]
counter = [0 for _  in range(1001)]

DFSvisited = [0 for _ in range(1001)]
DFSanswer = []

BFSvisited = [0 for _ in range(1001)]
BFSanswer = []
Q = []

for _ in range(E):
    i = list(map(int, input().split()))
    tree[i[0]].append(i[1])
    tree[i[1]].append(i[0])
    counter[i[0]] +=1 
    counter[i[1]] += 1

def DFS(TREE, n):
    if (DFSvisited[n] == 0):
        DFSanswer.append(n)
        DFSvisited[n] += 1
        tree[n].sort()
        for i in range(counter[n]):
            DFS(TREE,TREE[n][i])

def BFS(TREE):
    while(len(Q)>0):
        n = Q.pop(0)
        BFSanswer.append(n)
        tree[n].sort()
        for i in range(counter[n]):
            if (BFSvisited[tree[n][i]]==0):
                Q.append(tree[n][i])
                BFSvisited[tree[n][i]]+=1
        

Q.append(start)
BFSvisited[start]=1
BFS(tree)
DFS(tree,start)

print(*DFSanswer)
print(*BFSanswer)