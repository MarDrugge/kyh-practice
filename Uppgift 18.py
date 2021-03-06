people = {
    "Fredrik": "0702778511",
    "Olof": "123456789",
    "Lisa": "9999999999",
    "Bodil": "555-666-789"}


def sla_upp():
    print(f'Det finns {len(people)} kontakter i listan')
    vem = input("Vem vill du ringa? ")
    if vem not in people:
        print("Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog")
    else:
        number = people[vem]
        print(f"Numret till {vem} är {number}")


def lagg_till():
    namn = input("Ny kontakt: ")
    nummer = input("Nytt nummer: ")
    people[namn] = nummer
    print(f'Det finns {len(people)} kontakter i listan')
    main()


def main():
    print(f'1. Slå upp kontakt: \n2. Lägg till kontakt:')
    alt = input("Välj ett alternativ: ")
    if alt == "1":
        sla_upp()
    if alt == "2":
        lagg_till()


if __name__ == '__main__':
    main()
