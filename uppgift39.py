def maximum(a, b, c):       # 39.1
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c


value = maximum(4, 5, 7)
print(value)


def total(num):      # 39.2

    count = 0
    for elem in num:
        count += elem
    return count


numbers = [1, 2, 3]
print(total(numbers))


def produkt(num):   # 39.3
    count = 1
    for elem in num:
        count *= elem
    return count


numbers2 = [2, 3, 4]
print(produkt(numbers2))
