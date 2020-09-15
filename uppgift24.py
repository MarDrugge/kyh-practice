import requests
from pprint import pprint


def main():
    r = requests.get("https://proagile.se/api/publicEvents")
    t = r.json()
    #pprint(t)
    for course in t:
        if 'startDate' in course:
            print(course['startDate'])


if __name__ == '__main__':
    main()
