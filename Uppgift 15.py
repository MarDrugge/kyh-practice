
def main():
    vowels = "aeiouy"
    vowel_count = 0
    def wordcount(txt):
        return len(txt.split())
    text = input("Skriv en text: ")
    count = wordcount(text)
    for c in text:
        if c in vowels:
            vowel_count += 1
    print(f'Antal ord: {count} \nAntal vokaler: {vowel_count}')

main()
