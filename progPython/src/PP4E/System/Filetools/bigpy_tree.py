"""
Find the largest Python source file in an entire directory tree.
Search the Python source lib, use pprint to display results nicely.
"""

import sys
import os
import pprint

trace = False
if sys.platform.startswith('win'):
    DIRNAME = r'C:\Python31\Lib'  # Windows
else:
    DIRNAME = '/usr/lib/python3'  # Unix, Linux, Cygwin (Replaced python for python3)

allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(DIRNAME):
    if trace:
        print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace:
                print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
