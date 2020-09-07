import random


def main():
    leveranssatt = ['Laddas ned till mobiltelefonen', 'Beställas på posten', 'Leveras personligen av Elon Musk', 'Fås som paket från tomten', 'Kan tillverkas hemma']
    nationalitet = ['Finnländare', 'Svenskar', 'Danskar', 'Norrmän', 'Amerikaner']
    kontakt = ['Kommit nära', 'Chattat med', 'Kramat', 'Vinkat åt', 'Sneglat åt']
    smitta = ['Coronavirus', 'Vattkoppor', 'Tjejbaciller', 'Killbaciller', 'Matkoma']
    plats = ["Sverige", "Västra Götaland", "Vintergatan", "Norden", "Europa"]
    goras = ["Strunta i", "Överväga", "Prova"]
    namn = ["Donald Trump", "Gunnar", "Markku Tervahauta", "Adam"]
    yrke = ["President över de förenta staterna, POTUS", "A-lagare utanför systembolaget, FULL", "Generaldirektör för Finska institutet för hälsa och välfärd, THL", "Chef för Svenska institutet för inre säkerhet, SIIS"]

    print(f"""En app som kan {random.choice(leveranssatt)} ska varna {random.choice(nationalitet)} som {random.choice(kontakt)} någon som smittats av {random.choice(smitta)}")
 - Du tycker att vi i {random.choice(plats)} borde {random.choice(goras)} att göra något liknande, säger {random.choice(namn)},")
 {random.choice(yrke)}.""")


if __name__ == '__main__':
    main()
