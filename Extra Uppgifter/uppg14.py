def biggest(first, second, third):
    if first > second and first > third:
        return first
    if second > first and second > third:
        return second
    else:
        return third


def main():
    biggest_num = biggest(5, 4, 1)
    print(biggest_num)


if __name__ == '__main__':
    main()
