num = int(input())

for i in range(num):
    for j in range(num):
        if ((j%2) == 0): print("*", end="")
        else: print(" ", end="")
    print("")
    if num != 1:
        for k in range(num):
            if ((k%2) == 1): print("*", end="")
            else: print(" ", end="")
        print("")