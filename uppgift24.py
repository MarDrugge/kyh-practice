import requests
import datetime
from pprint import pprint


def main():
    r = requests.get("https://proagile.se/api/publicEvents")
    t = r.json()
    today = datetime.date.today()

    year = input("Skriv år: ")
    month = input("Skriv månad: ")
    date1 = f'{year}-{month}-01'
    date2 = f'{year}-{month}-31'

    for elements in t:
       if elements['startDate'] >= date1 and elements['startDate'] <= date2:
           print(f'Kursnamn: {elements["name"]}\nStartdatum: {elements["startDate"]}\nSlutdatum: {elements["endDate"]}')
           print(f'\n\n')


if __name__ == '__main__':
    main()
