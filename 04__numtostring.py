def main():
    dct = {
        "1" : "one",
        "2" : "two",
        "3" : "three",
        "4" : "four",
        "5" : "five",
        "6" : "six",
        "7" : "seven",
        "8" : "eight",
        "9" : "nine",
        "10" : "ten",
        "-" : "minus"
    }
    n = input("Enter a number: ")
    for i in n:
        print(dct.get(i, i), end=' ')

if __name__ == '__main__':
    main()