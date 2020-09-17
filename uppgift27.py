import json
from pathlib import Path


p = Path('data.json')
s = p.read_text(encoding='utf8')
content = json.loads(s)


def main():
    print("Innehåll:")
    for element in content:
        if not element["rightalign"]:
            print(f'{element["what"]:25}{element["value"]:12}{element["unit"]}')
        elif element["rightalign"]:
            print(f'{element["what"]:>20}{element["value"]:17}{element["unit"]}')


if __name__ == '__main__':
    main()
