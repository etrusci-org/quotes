#!/usr/bin/env python3

import sys
import subprocess
import json
import urllib.parse



jsModuleFile = './js/quotes-s9.js'
jsScriptFile = './js/quotes-s9-script.js'
jsonFile = './json/quotes-s9.json'
authorsFile = './authors.txt'
mdDir = './md'



def bake():
    # typescript module -> javascript module
    dump = subprocess.run(['/usr/bin/tsc', '-p', './tsconfig.json'])
    if dump.returncode != 0:
        print('failed to compile typescript to javascript')
        sys.exit(1)

    # javascript module -> javascript script
    with open(jsModuleFile, 'r') as mf, open(jsScriptFile, 'w') as sf:
        dump = mf.read()
        dump = f'"use strict";\n{dump}'
        dump = dump.replace('export ', '')
        sf.write(dump)

    # javascript script -> json
    with open(jsScriptFile, 'r') as sf, open(jsonFile, 'w') as jf:
        dump = sf.read()
        dump = dump.split(' = ')[1]
        dump = dump.replace('`', '"')
        dump = dump.replace(';', '')
        dump = dump.replace('author:', '"author":')
        dump = dump.replace('text:', '"text":')
        dump = dump.replace('},\n]', '}\n]')
        jf.write(dump)

    # authors -> txt
    with open(authorsFile, 'w') as af:
        dump = json.loads(dump)
        authors = []
        for v in dump:
            if not v['author'] in authors:
                authors.append(v['author'])
        af.write('\n'.join(authors))

    # json -> md
    with open(jsonFile, 'r') as jf:
        dump = json.loads(jf.read())

        quotes = {}
        for v in dump:
            if not v['author'] in quotes.keys():
                quotes[v['author']] = []
            quotes[v['author']].append(v['text'])

        for author, quotes in quotes.items():
            quotesFile = f'{mdDir}/Quotes {author}.md'
            with open(quotesFile, 'w') as qf:
                qf.write(f'# Quotes by {author}\n\n')
                qf.write('---\n\n')
                for q in quotes:
                    qf.write(f'- {q}\n')



if __name__ == '__main__':
    bake()
