a = int(input())
b = int(input())

def judgeQuadrant(a,b):
    if (a>0 and b>0):
        Q=1
    elif (a<0 and b>0):
        Q=2
    elif (a<0 and b<0):
        Q=3
    elif (a>0 and b<0):
        Q=4
    else:
        Q="NOT POSSIBLE"
    return Q

print(judgeQuadrant(a,b))