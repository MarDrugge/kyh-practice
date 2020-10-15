def main():
    vowels = ['a','e', 'i', 'o', 'u', 'y']
    char = input('Skriv en char: ')
    if char in vowels:
        print(f'{char} är en vokal')
    else:
        print(f'{char} är inte en vokal')


if __name__ == '__main__':
    main()
