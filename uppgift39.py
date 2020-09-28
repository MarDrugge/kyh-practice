def maximum(a, b, c):       # 39.1
    if b < a < c:
        return a
    if a < b < c:
        return b
    if a < c < b:
        return c


value = maximum(4, 5, 7)
print(value)


def total(num):      # 39.2

    count = 0
    for elem in num:
        count += elem
    print(count)


numbers = [1, 2, 3]
total(numbers)


def produkt(num):   # 39.3
    count = 1
    for elem in num:
        count *= elem
    print(count)


numbers2 = [2, 3, 4]
produkt(numbers2)
