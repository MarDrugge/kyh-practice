from pathlib import Path


def run():
    for line in Path('system.log').read_text().splitlines():
        if 'BEAR' in line or 'X-RAY' in line:
            print(line)


if __name__ == '__main__':
    run()
