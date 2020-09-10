from pathlib import Path


lines = Path('TODO.txt')
read = lines.read_text(encoding='utf8')
split = read.splitlines()
n = "\n"


def alt_1():
    print(n.join(split))


def alt_2():
    ny = input("Lägg till Uppgift: ").strip()
    split.append(ny)
    lines.write_text(f'{n.join(split)}', encoding='utf8')


def main():
    alt = input(f'1. Lista TODO:\n2. Lägg till uppgift:\n3. Ta bort uppgift:\n4. Avbryt programmet:\nVälj alternativ: ')
    if alt == "1":
        alt_1()
    if alt == "2":
        alt_2()
    if alt == "4":
        print("Programmet avbryts")


if __name__ == '__main__':
    main()
