[A, B, C] = list(map(int, input().split()))

square = []
square.append(A)
count =1 
while (count*2<=B):
    count = count * 2
    square.append(square[-1]*square[-1])

print(count)
print(square)
def rec(A,B):
    global count

    if (B==1):
        return A
        
    elif (B==0):
        return 1

    if (len(square)!=0):
        count -= 1
        last = square.pop()
        return rec(A,B%count)*last

print(rec(A,B))

    

# def rec(A,B):
#     if (B == 1):
#         return A
#     elif (B%2==0):
#         return rec(A,B/2)*rec(A,B/2)
#     else:
#         return A*(rec(A,B//2)*rec(A,B//2))