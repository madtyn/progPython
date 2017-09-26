#!/usr/bin/python
"""
################################################################################
Return all files matching a filename pattern at and below a root directory;

custom version of the now deprecated find module in the standard library:
import as "PP4E.Tools.find"; like original, but uses os.walk loop, has no
support for pruning subdirs, and is runnable as a top-level script;

find() is a generator that uses the os.walk() generator to yield just
matching filenames: use findlist() to force results list generation;
################################################################################
"""

import fnmatch
import os


def find(pattern, startdir=os.curdir):
    '''
    Finds the ocurrences of the pattern in the full tree starting at startdir
    :param pattern: the pattern that results should match with
    :param startdir: the directory from which this method starts to search
    '''
    for (thisDir, subsHere, filesHere) in os.walk(startdir):
        for name in subsHere + filesHere:
            if fnmatch.fnmatch(name, pattern):
                fullpath = os.path.join(thisDir, name)
                yield fullpath


def findlist(pattern, startdir=os.curdir, dosort=False):
    '''
    Returns the results from find() as a list. Results can be sorted.
    :param pattern: the pattern that results should match with
    :param startdir: the directory from which this method starts to search
    :param dosort: True if the results should be sorted, False otherwise
    '''
    matches = list(find(pattern, startdir))
    if dosort:
        matches.sort()
    return matches


if __name__ == '__main__':
    import sys
    namepattern, startdir = sys.argv[1], sys.argv[2]
    for name in find(namepattern, startdir):
        print(name)
