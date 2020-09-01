import random

n = random.randint(1, 100)
print("Jag tänker på ett nummer mellan 1 & 100. Vilket?")


def ask_number():
    text = input("Din Gissning: ")
    as_number = int(text)
    return as_number


def mainloop(n):
    chances = 0
    while True:
        as_number = ask_number()
        chances += 1
        if as_number == n:
            print("Korrekt!")
            print("Antal gissningar:", chances)
            break

        if as_number < n:
            print("Fel, mitt nummer är högre. Försök igen!")

        if as_number > n:
            print("Fel, mitt nummer är lägre. Försök igen!!")
    return


mainloop(n)
