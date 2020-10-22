# 51.1

def add_as_def(a, b):
    return a + b

add_as_lambda = lambda a, b: a + b
# print(add_as_def(3, 4))
# print(add_as_lambda(3, 4))

# 51.2

obj = lambda s: s.upper()

def obj(s):
    return s.upper()

# 51.3

join_as_lambda = lambda strings, inbetween: inbetween.join(strings)

# print(join_as_lambda("adasd", ","))

def inbetween_fnc(strings, inbetween):
    return inbetween.join(strings)

# print(inbetween_fnc("asdasdasf", ","))

# 51.4

anna = ("Anna", "Persson", 42)
lova = ("Lova", "Andersson", 35)
alex = ("Alex", "Börjesson", 10)
people = [anna, lova, alex]
on_surname = sorted(people, key=lambda p: p[1])
for (first, last, age) in on_surname:
    print(f"{first} {last} ({age} år)")

# 51.5

anna = ("Anna", "Persson", 42)
lova = ("Lova", "Andersson", 35)
alex = ("Alex", "Börjesson", 10)
people = [anna, lova, alex]
on_surname = sorted(people, key=lambda p: p[2])
for (first, last, age) in on_surname:
    print(f"{first} {last} ({age} år)")

# 51.6


anna = ("Anna", "Persson", 42)
lova = ("Lova", "Andersson", 35)
alex = ("Alex", "Börjesson", 10)
people = [anna, lova, alex]
def age_sorter(people):
    return people[2]
people.sort(key=age_sorter)
for (first, last, age) in people:
    print(f"{first} {last} ({age} år)")

# 51.7

