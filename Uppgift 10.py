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

    print("Del 4")
    total = 0
    for i in range(7, 1001):
        total += i
    print(total)

    print("Del 5")
    product = 1
    for i in range(1, 1001):
        product *= i
    print(product)


if __name__ == '__main__':
    main()
