#!/usr/bin/env python3

import json
import pathlib


OUT_DIR = pathlib.Path(__file__).parent.resolve()

SRC_FILE = OUT_DIR / 'source.json'

OUT_FILE_JSON = OUT_DIR / 'json' / 'quotes.json'
OUT_FILE_JSON_MIN = OUT_DIR / 'json' / 'quotes.min.json'

OUT_FILE_MD = OUT_DIR / 'markdown' / 'quotes.md'

OUT_FILE_AUTHORS_JSON = OUT_DIR / 'author' / 'authors.json'
OUT_FILE_AUTHORS_JSON_MIN = OUT_DIR / 'author' / 'authors.min.json'
OUT_FILE_AUTHORS_TXT = OUT_DIR / 'author' / 'authors.txt'


# -----------------------------------------------------------------------------


QUOTES = []
AUTHORS = []

with open(SRC_FILE, 'r') as f:
    QUOTES = json.load(f)

for v in QUOTES:
    if not v['author'] in AUTHORS:
        AUTHORS.append(v['author'])


# -----------------------------------------------------------------------------


def main():
    bake_json()
    bake_markdown()
    bake_authors()


def bake_json():
    with open(OUT_FILE_JSON, 'w') as f1, open(OUT_FILE_JSON_MIN, 'w') as f2:
        json.dump(QUOTES, f1, indent=4)
        json.dump(QUOTES, f2)


def bake_markdown():
    with open(OUT_FILE_MD, 'w') as f1:
        dump = {}
        for v in QUOTES:
            if not v['author'] in dump.keys():
                dump[v['author']] = []
            dump[v['author']].append(v['text'])
        f1.write(f'# Quotes\n')
        for author, quotes in dump.items():
            f1.write(f'\n\n## {author}\n\n')
            for v in quotes:
                f1.write(f'- {v}\n')


def bake_authors():
    with open(OUT_FILE_AUTHORS_TXT, 'w') as f1, open(OUT_FILE_AUTHORS_JSON, 'w') as f2, open(OUT_FILE_AUTHORS_JSON_MIN, 'w') as f3:
        f1.write('\n'.join(sorted(AUTHORS)))
        json.dump(AUTHORS, f2, indent=4)
        json.dump(AUTHORS, f3)


# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
