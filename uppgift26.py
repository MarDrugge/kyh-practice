import requests


def main():

    film = input('Sök film: ')
    r = requests.get("http://www.omdbapi.com/", params={"t": film, "apikey": "9f6d550c"})
    movie = r.json()

    if "Error" in movie:
        print('Hittar ingen film med det namnet')
        return

    print(f'\n*** Resultat från OMDB! ***\n')
    print(f'Titel:      {movie["Title"]}')
    print(f'Från:       {movie["Year"]}')
    print(f'Skådisar:   {movie["Actors"]}')
    print(f'IMDB:       {movie["imdbRating"]}')
    print(f'Awards:     {movie["Awards"]}')
    print(f'Längd:      {movie["Runtime"]}')
    print(f'\n****************************')


if __name__ == '__main__':
    main()
