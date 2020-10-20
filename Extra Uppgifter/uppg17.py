def main():
    string = input("Skriv en sträng: ")
    new_string = ""
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å ', 'ä', 'ö', ' ']
    for c in string:
        if c in vowels:
            new_string += c
        else:
            new_string += c + "o" + c
    print(new_string)


if __name__ == '__main__':
    main()
