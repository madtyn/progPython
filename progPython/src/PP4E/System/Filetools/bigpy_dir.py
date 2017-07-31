"""
Find the largest Python source file in a single directory.
Search Windows Python source lib, unless dir command-line arg.
"""

import os
import glob
import sys
DIRNAME = r'C:\Python31\Lib' if len(sys.argv) == 1 else sys.argv[1]

ALLPY = glob.glob(DIRNAME + os.sep + '*.py')
allsizes = []

for filename in ALLPY:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])
