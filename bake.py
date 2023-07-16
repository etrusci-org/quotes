#!/usr/bin/env python3

import sys
import subprocess




jsModuleFile = './js/quotes-s9.js'
jsScriptFile = './js/quotes-s9-script.js'
jsonFile = './json/quotes-s9.json'




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




if __name__ == '__main__':
    bake()
