#!/usr/bin/env python3

import json




SOURCE_FILE = './_src.json'
OUT_FILE_JSON = './json/quotes.json'
OUT_FILE_JSON_MIN = './json/quotes.min.json'
OUT_FILE_MARKDOWN = './markdown/quotes.md'
OUT_FILE_AUTHORS = './authors.txt'




def bake():
    with open(SOURCE_FILE, 'r') as src_f, \
         open(OUT_FILE_JSON, 'w') as out_f_json, \
         open(OUT_FILE_JSON_MIN, 'w') as out_f_json_min, \
         open(OUT_FILE_MARKDOWN, 'w') as out_f_md, \
         open(OUT_FILE_AUTHORS, 'w') as out_f_authors:

        src = json.load(src_f)

        # src > json
        print(f'{SOURCE_FILE} > {OUT_FILE_JSON}')
        json.dump(src, out_f_json, ensure_ascii=True, indent=4)

        # src > json.min
        print(f'{SOURCE_FILE} > {OUT_FILE_JSON_MIN}')
        json.dump(src, out_f_json_min, ensure_ascii=True)

        # src > quotes.md
        print(f'{SOURCE_FILE} > {OUT_FILE_MARKDOWN}')
        dump = {}
        for v in src:
            if not v['author'] in dump.keys():
                dump[v['author']] = []
            dump[v['author']].append(v['text'])
        out_f_md.write(f'# Quotes\n')
        for author, quotes in dump.items():
            out_f_md.write(f'\n\n## {author}\n\n')
            for v in quotes:
                out_f_md.write(f'- {v}\n')

        # src > authors.txt
        print(f'{SOURCE_FILE} > {OUT_FILE_AUTHORS}')
        dump = []
        for v in src:
            if not v['author'] in dump:
                dump.append(v['author'])
        out_f_authors.write('\n'.join(sorted(dump)))


if __name__ == '__main__':
    bake()
