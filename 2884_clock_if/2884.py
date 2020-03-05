class Clock():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.counter = 60*x +y
    def set_clock(self, m=45):
        self.counter -= m
        if (self.counter>60*24): self.counter -= 60*24
        elif (self.counter<0): self.counter += 60*24
        self.x = self.counter // 60
        self.y = self.counter % 60

def main():
    x,y = map(int, input().split())
    sangeun = Clock(x,y)
    sangeun.set_clock()
    print(f'{sangeun.x} {sangeun.y}')

if __name__ == "__main__":
    main()