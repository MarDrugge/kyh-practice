def main():
    age = int(input('Hur gammal är du? '))
    if 13 <= age <= 19:
        print('Du är en tonåring')
    else:
        print('Du är inte en tonåring')


if __name__ == '__main__':
    main()
