
def numbers():
    numbers = input("Ange tal med komma imellan: ")
    num = [int(elem) for elem in numbers.split(',')]
    odd_num = [str(elem) for elem in num if elem % 2 == 1]
    even_num = [str(elem) for elem in num if elem % 2 == 0]
    o_n = ",".join(odd_num)
    e_n = ",".join(even_num)

    print(f'Första talet: {numbers[0]}\nSista Talet: {numbers[-1]}\nSumma av Talen: {sum(num)}')
    print(f'Udda Tal: {o_n}\nJämna Tal: {e_n}')
    print(f'Talen baklänges: {numbers[::-1]}')


if __name__ == '__main__':
    numbers()
