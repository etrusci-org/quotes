#!/usr/bin/env python3

import datetime
import json
import pathlib


OUT_DIR = pathlib.Path(__file__).parent.resolve()

SRC_FILE = OUT_DIR / 'source.json'

OUT_FILE_JSON = OUT_DIR / 'json' / 'quotes.json'
OUT_FILE_JSON_MIN = OUT_DIR / 'json' / 'quotes.min.json'

OUT_FILE_MD = OUT_DIR / 'markdown' / 'quotes.md'

# OUT_FILE_STREAMERBOT = OUT_DIR / 'streamerbot' / 'quotes.dat'

OUT_FILE_TEXT = OUT_DIR / 'text' / 'quotes.txt'

OUT_FILE_AUTHORS_JSON = OUT_DIR / 'author' / 'authors.json'
OUT_FILE_AUTHORS_JSON_MIN = OUT_DIR / 'author' / 'authors.min.json'
OUT_FILE_AUTHORS_TXT = OUT_DIR / 'author' / 'authors.txt'

TEXT_QUOTE_FORMAT = '"{text}" ― {author}'

# STREAMERBOT_USER_ID = '1076439190'
# STREAMERBOT_USER_NAME = 'g6_b2'
# STREAMERBOT_PLATFORM_NAME = 'twitch'
# STREAMERBOT_GAME_ID = '26936'
# STREAMERBOT_GAME_NAME = 'Music'


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
    # bake_streamerbot()
    bake_text()


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


# def bake_streamerbot():
#     with open(OUT_FILE_STREAMERBOT, 'w') as f:
#         dump = {
#             'version': 3,
#             't': '',
#             'quotes': [],
#         }
#         for id, quote in enumerate(QUOTES, start=1):
#             timestamp = datetime.datetime.now().isoformat()
#             dump['quotes'].append({
#                 'timestamp': timestamp,
#                 'id': id,
#                 'userId': STREAMERBOT_USER_ID,
#                 'user': STREAMERBOT_USER_NAME,
#                 'platform': STREAMERBOT_PLATFORM_NAME,
#                 'gameId': STREAMERBOT_GAME_ID,
#                 'gameName': STREAMERBOT_GAME_NAME,
#                 'quote': TEXT_QUOTE_FORMAT.format(**quote),
#             })
#         dump['t'] = timestamp
#         json.dump(dump, f, indent=4)


def bake_text():
    dump = [TEXT_QUOTE_FORMAT.format(**v) for v in QUOTES]
    with open(OUT_FILE_TEXT, 'w') as f:
        f.write('\n'.join(dump))


# -----------------------------------------------------------------------------


if __name__ == '__main__':
    main()
