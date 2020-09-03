def main():
    print("Del 1:")
    for i in range(1, 11):
        print(i)

    print("Del 2:")
    for i in range(1, 50):
        if i % 2 != 0:
            print(i)

    print("Del 3")
    for i in range(10, 0, -1):
        print(i)


if __name__ == '__main__':
    main()
