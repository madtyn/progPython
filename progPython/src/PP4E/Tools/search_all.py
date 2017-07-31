"""  #pylint: disable=anomalous-backslash-in-string
################################################################################
Use: "python ...\Tools\search_all.py dir string".
Search all files at and below a named directory for a string; uses the
os.walk interface, rather than doing a find.find to collect names first;
similar to calling visitfile for each find.find result for "*" pattern;
################################################################################
"""

import os
import sys

LISTONLY = False
textexts = ['.py', '.pyw', '.txt', '.c', '.h']  # ignore binary files


def searcher(startdir, searchkey):
    '''
    With a directory and a string, it searches recursively all the files
    in that directory containing the required key string
    :param startdir: the directory in which we start
    :param searchkey: the string we're looking for
    '''
    global fcount, vcount
    fcount = vcount = 0
    for (thisDir, _, filesHere) in os.walk(startdir):
        for fname in filesHere:  # do non-dir files here
            fpath = os.path.join(thisDir, fname)  # fnames have no dirpath
            visitfile(fpath, searchkey)


def visitfile(fpath, searchkey):  # for each non-dir file
    '''
    It looks for a key string inside a text file
    :param fpath: the file path
    :param searchkey: the string we're looking for
    '''
    global fcount, vcount  # search for string
    print(vcount + 1, '=>', fpath)  # skip protected files
    try:
        if not LISTONLY:
            if os.path.splitext(fpath)[1] not in textexts:
                print('Skipping', fpath)
            elif searchkey in open(fpath).read():
                input('%s has %s' % (fpath, searchkey))
                fcount += 1
    except:
        print('Failed:', fpath, sys.exc_info()[0])
    vcount += 1


if __name__ == '__main__':
    searcher(sys.argv[1], sys.argv[2])
    print('Found in %d files, visited %d' % (fcount, vcount))
