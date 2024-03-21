#!/usr/bin/env python3

import json




SOURCE_FILE = './_src.json'
OUT_FILE_JSON = './json/quotes.json'
OUT_FILE_JSON_MIN = './json/quotes.min.json'
OUT_FILE_MARKDOWN = './markdown/quotes.md'
OUT_FILE_AUTHORS_JSON = './authors.json'
OUT_FILE_AUTHORS_JSON_MIN = './authors.min.json'
OUT_FILE_AUTHORS_TXT = './authors.txt'




def bake():
    with open(SOURCE_FILE, 'r') as src_f, \
         open(OUT_FILE_JSON, 'w') as out_f_json, \
         open(OUT_FILE_JSON_MIN, 'w') as out_f_json_min, \
         open(OUT_FILE_MARKDOWN, 'w') as out_f_md, \
         open(OUT_FILE_AUTHORS_TXT, 'w') as out_f_authors_txt, \
         open(OUT_FILE_AUTHORS_JSON, 'w') as out_f_authors_json, \
         open(OUT_FILE_AUTHORS_JSON_MIN, 'w') as out_f_authors_json_min:

        print(f'< {SOURCE_FILE}')
        src = json.load(src_f)

        authors = []
        for v in src:
            if not v['author'] in authors:
                authors.append(v['author'])

        # src > quotes.json
        print(f'> {OUT_FILE_JSON}')
        json.dump(src, out_f_json, indent=4)

        # src > quotes.min.json
        print(f'> {OUT_FILE_JSON_MIN}')
        json.dump(src, out_f_json_min)

        # src > quotes.md
        print(f'> {OUT_FILE_MARKDOWN}')
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
        print(f'> {OUT_FILE_AUTHORS_TXT}')
        out_f_authors_txt.write('\n'.join(sorted(authors)))

        # src > authors.json
        print(f'> {OUT_FILE_AUTHORS_JSON}')
        json.dump(authors, out_f_authors_json, indent=4)

        # src > authors.min.json
        print(f'> {OUT_FILE_AUTHORS_JSON_MIN}')
        json.dump(authors, out_f_authors_json_min)




if __name__ == '__main__':
    bake()
