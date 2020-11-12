from pathlib import Path


lines = Path('TODO.txt')
read = lines.read_text(encoding='utf8')
split_ls = read.splitlines()
n = "\n"


def alt_1():
    num = 0
    print('\n')
    for elem in split_ls:
        num += 1
        print(f'{num}. {elem}')
    print('\n')


def alt_2():
    ny = input("Lägg till Uppgift: ").strip()
    split_ls.append(ny)
    lines.write_text(f'{n.join(split_ls)}', encoding='utf8')


def alt_3():
    del_task = int(input("Radera uppgift: "))
    index = del_task - 1
    del split_ls[index]
    lines.write_text(f'{n.join(split_ls)}', encoding='utf8')


def main():
    while True:
        alt = input(f'1. Lista TODO:\n2. Lägg till uppgift:\n3. Ta bort uppgift:\n4. Avbryt programmet:\nVälj alternativ: ')
        if alt == "1":
            alt_1()
        elif alt == "2":
            alt_2()
        elif alt == "3":
            alt_3()
        elif alt == "4":
            print("Programmet avbryts...")
            break


if __name__ == '__main__':
    main()
