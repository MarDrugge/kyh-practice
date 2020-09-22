def main():
    inp = input("Skriv en sträng: ")
    inp2 = inp.join('')
    palin = inp2[::-1]
    print(f'Längd: {len(inp)}')
    if palin.lower() == inp2.lower():
        print(f'Strängen är ett palindrom')
    else:
        print(f'Strängen är inte ett palindrom')


if __name__ == '__main__':
    main()
