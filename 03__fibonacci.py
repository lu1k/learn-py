def main():
    a, b = 0, 1
    n = int(input("Enter a number: "))

    for i in range(2, n):
        a, b = b, a+b
        print(a, b, end='')

if __name__ == '__main__':
    main()