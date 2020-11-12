
def main():
    vowels = "aeiouy"
    vowel_count = 0

    def wordcount(txt):
        return len(txt.split_ls())
    text = input("Skriv en text: ")
    count = wordcount(text)
    for c in text:
        if c in vowels:
            vowel_count += 1
    print(f'Antal ord: {count} \nAntal vokaler: {vowel_count}')

    runners_in_order = 'Lisa Lasse Louise Leopold Lova Love Lennart Lena Lisette Linus'.split()
    vem = input('Ange löpare du söker placering för: ')
    index = runners_in_order.index(vem)
    print(f'Löparen hamnade på plats nr {index}')


main()
