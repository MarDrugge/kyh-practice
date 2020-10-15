def main():
    notes = {
        "1": "George Washington",
        "2": "Thomas Jefferson",
        "5": "Abraham Lincoln",
        "10": "Alexander Hamilton",
        "20": "Andrew Jackson",
        "50": "Ulysses S. Grant",
        "100": "Benjamin Franklin"
    }

    value = input('Var god skriv valör på en us-sedel: ')
    if value not in notes:
        print('Tyvärr, ej giltig valör')
    else:
        print(f'Snubben på sedeln är {notes[value]}')

if __name__ == '__main__':
    main()
