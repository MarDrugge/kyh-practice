def rev_string(txt):    # 40.1
    return txt[::-1]


my_string = rev_string("Hur ser denna sträng ut baklänges?")
print(my_string)


def stor_bokstav(txt):     # 40.2
    count = 0
    for c in txt:
        if c.isupper():
            count += 1
    return count


my_string2 = 'Hur Många Stora Bokstäver Finns Det'
print(f'Antal stora bokstäver: {stor_bokstav(my_string2)}')


def in_range(value, min, max):  # 40.3
    if min < value < max:
        return True
    else:
        return False


print(in_range(1, 0, 2))
