def main():
    s = 'Pythonist 2'
    for i in s:
        if i.isupper():
            print(i.lower(), end='')
        else :
            print(i.upper(), end='')

if __name__ == '__main__':
    main()