def is_it_too_long(name, length):
    return len(name) > length


def main():
    try:
        length = int(input("Maxlängd på namn? "))
    except ValueError:
        print("Sätter maxlängd till 5")
        length = 5
    students = input("Ange namn med komma imellan: ").split(",")
    for name in students:
        if is_it_too_long(name, length):
            print(f"{name.title()} är för långt!")


if __name__ == '__main__':
    main()
