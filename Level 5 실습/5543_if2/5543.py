Burger = 2000
Beverage = 2000
for _ in range(3):
    a = int(input())
    if (a<Burger): Burger = a
for _ in range(2):
    b = int(input())
    if (b<Beverage): Beverage = b
print(Burger + Beverage - 50)
