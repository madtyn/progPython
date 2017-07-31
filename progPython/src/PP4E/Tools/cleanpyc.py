"""
delete all .pyc bytecode files in a directory tree: use the
command line arg as root if given, else current working dir
"""

import os
import sys

FINDONLY = False
ROOTDIR = os.getcwd() if len(sys.argv) == 1 else sys.argv[1]

found = removed = 0
for (thisDirLevel, subsHere, filesHere) in os.walk(ROOTDIR):
    for filename in filesHere:
        if filename.endswith('.pyc'):
            fullname = os.path.join(thisDirLevel, filename)
            print('=>', fullname)
            if not FINDONLY:
                try:
                    os.remove(fullname)
                    removed += 1
                except:
                    type_, inst = sys.exc_info()[:2]
                    print('*' * 4, 'Failed:', filename, type_, inst)
            found += 1

print('Found', found, 'files, removed', removed)
