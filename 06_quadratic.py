import math
def main():
    a, b, c = int(input("Enter values of a,b, c: ").split())
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        print(x1, x2)
    elif D < 0:
        x1 = (-b + math.sqrt(D))/(2*a)


if __name__ == '__main__':
    main()