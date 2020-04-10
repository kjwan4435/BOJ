star = int(input())

for i in range(star):
    print (" "*(i), end="")
    print ("*"*((2*star-1)-(2*i)))

for i in range(star-2,-1,-1):
    print (" "*(i), end="")
    print ("*"*((2*star-1)-(2*i)))