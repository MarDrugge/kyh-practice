from Uppgift36 import pwstrength


def main():
    pw = input("skriv ditt lösenord: ")
    pwstrength.compute_strength(pw)


if __name__ == '__main__':
    main()
