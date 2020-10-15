def main():
    X = 23
    Y = 110
    Z = 5

    if X < Y and X < Z:
        x = X
        if Y < Z:
            y = Y
            z = Z
        else:
            y = Z
            z = Y
    else:
        if Y < X and Y < Z:
            x = Y
            if X < Z:
                y = X
                z = Z
            else:
                y = Z
                z = X
        else:
            x = Z
            if X < Y:
                y = X
                z = Y
            else:
                y = Y
                z = X
    print(x, y, z)




if __name__ == '__main__':
    main()
