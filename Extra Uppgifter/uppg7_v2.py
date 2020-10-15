def main():
    X = 23
    Y = 110
    Z = 5

    if X < Y < Z:
        x = X
        y = Y
        z = Z
    if X < Z < Y:
        x = X
        y = Z
        z = Y
    if Y < X < Z:
        x = Y
        y = X
        z = Z
    if Y < Z < X:
        x = Y
        y = Z
        z = X
    if Z < X < Y:
        x = Z
        y = X
        z = Y
    if Z < Y < X:
        x = Z
        y = Y
        z = X

    print(x, y, z)


if __name__ == '__main__':
    main()
