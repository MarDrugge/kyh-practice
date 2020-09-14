import json
from pathlib import Path


def compute_total(o):
    entries_list = o['entries']
    totals = []
    for entry in entries_list:
        totals.append(entry['total'])
    return sum(totals)


def main():

    p = Path('uppgift21.json')
    s = p.read_text(encoding='utf8')
    o = json.loads(s)
    total = compute_total(o)
    print(f'Total = {total}')


if __name__ == '__main__':
    main()
