def reg_plat():
    reg_nr = input("Skriv Reg. Nr: ")
    print(f'Bokstäver: {reg_nr[0:3]}\nSiffror: {reg_nr[3:6]}')


def numbers():
    numbers = input("Ange tal med komma imellan: ")
    string_nr = numbers.split(',')
    num = []
    for elem in string_nr:
        num.append(int(elem))
    print(f'Första talet: {numbers[0]}\nSista Talet: {numbers[-1]}\nSumma av Talen: {sum(num)}')
    print(f'Talen baklänges: {numbers[::-1]}')


def main():
    inp = input("Vill du köra 1. Reg_Plåt eller 2. Numbers: ")
    if inp == "1":
        reg_plat()
    if inp == "2":
        numbers()


if __name__ == '__main__':
    main()
