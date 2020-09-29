def print_user(user):
    (name, age) = user
    print(f'Ditt namn är {name} och du är {age} år')


def swaptuple(t):
    (a, b) = t
    print(f'Input tuple: {t}')
    (a, b) = (b, a)
    print(f'Vänder på tuple...')
    t = (a, b)
    print(f'{t}')


def to_tuple(ls):
    return tuple(ls)


if __name__ == '__main__':
    print_user(("Martin", 23))
    swaptuple(("a", "b"))
    print(to_tuple([1, 2, 3]))