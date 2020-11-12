from pathlib import Path


lines = Path('TODO.txt')
read = lines.read_text(encoding='utf8')
split = read.splitlines()
n = "\n"


def alt_1():
    num = 0
    for elem in split:
        num += 1
        print(f'{num}. {elem}')


def alt_2():
    ny = input("Lägg till Uppgift: ").strip()
    split.append(ny)
    lines.write_text(f'{n.join(split)}', encoding='utf8')


def alt_3():
    del_task = int(input("Radera uppgift: "))
    index = del_task - 1
    del split[index]
    lines.write_text(f'{n.join(split)}', encoding='utf8')


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
            print("Programmet avbryts")
            break


if __name__ == '__main__':
    main()
