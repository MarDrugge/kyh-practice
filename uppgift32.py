def main():
    inp = input("Skriv en sträng: ")
    palin = inp[::-1]
    print(f'Längd: {len(inp)}')
    if palin.lower() == inp.lower():
        print(f'Strängen är ett palindrom')


if __name__ == '__main__':
    main()
