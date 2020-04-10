TEST_NUM = int(input())

for test in range(TEST_NUM):
    size = int(input())
    trace = 0
    rows = 0
    cols = 0
    matrix = []

    for i in range(size):
        matrix.append(list(map(int,input().split())))

    def diagSum(matrix, size, trace):
        for i in range(size):
            trace += matrix[i][i]
        return trace

    def rowIsSame(matrix, size, rows):
        for i in range(size):
            isSame = False
            for j in range(size):
                if (j == 0):
                    if (matrix[i][j] in matrix[i][1:]): isSame = True
                elif (j == size-1):
                    if (matrix[i][j] in matrix[i][0:j-1]): isSame = True
                else:
                    if (matrix[i][j] in matrix[i][0:j] or matrix[i][j] in matrix[i][j+1:]):
                        isSame = True
            if (isSame):
                rows += 1
                isSame = False
        return rows

    def matrixRotation(matrix,size):
        matrixT = [[] for _ in range(size)]
        for i in range(size):
            for j in range(size):
                matrixT[i].append(matrix[j][i])
        return matrixT

    trace = diagSum(matrix,size,trace)
    rows = rowIsSame(matrix,size,rows)
    matrixT = matrixRotation(matrix,size)
    cols = rowIsSame(matrixT,size,cols)
    
    print("Case #{}: {} {} {}".format(test+1, trace, rows, cols))