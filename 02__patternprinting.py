def main():
    for i in range(1, 5):
        for j in range(i):
            print('*', end=' ')
        print()

def inverted():
    for i in range(5, 0, -1):
        for j in range(i):
            print('*', end=' ')
        print()

def Num():
    for i in range(1, 5):
        for j in range(i):
            print(i, end=' ')
        print()

def invertedNum():
    for i in range(5, 0, -1):
        for j in range(i):
            print(i, end=' ')
        print()

def Num():
    for i in range(1, 6):
        for j in range(i):
            print(j+1, end=' ')
        print()

def numInverted():
    x = 1
    for i in range(5, 0, -1):
        for j in range(i):
            print(x, end=' ')
        x += 1
        print()

def numInverted():
    for i in range(5, 0, -1):
        for j in range(i):
            print("5", end=' ')
        print()

def oddTriangle():
    x = 1
    for i in range(0, 6):
        for j in range(i+1):
            print((2*i)+1, end=' ')
        x += 2
        print()

if __name__ == '__main__':
    oddTriangle()