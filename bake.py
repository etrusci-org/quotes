#!/usr/bin/env python3

import json




SOURCE_FILE = './_src.json'
OUT_FILE_JSON = './quotes.json'
OUT_FILE_JSON_MIN = './quotes.min.json'




def bake():
    with open(SOURCE_FILE, 'r') as src_f, \
         open(OUT_FILE_JSON, 'w') as out_f_json, \
         open(OUT_FILE_JSON_MIN, 'w') as out_f_json_min:

        src = json.load(src_f)

        print('_src.json > quotes.json')
        json.dump(src, out_f_json, ensure_ascii=True, indent=4)

        print('_src.json > quotes.min.json')
        json.dump(src, out_f_json_min, ensure_ascii=True)




if __name__ == '__main__':
    bake()
