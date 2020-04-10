def split(list): return [num for num in list]

line = input()
line = split(line)
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha = split(alpha)

for i in range(len(alpha)):
    if alpha[i] in line: print(line.index(alpha[i]), end=" ")
    else: print(-1, end=" ")