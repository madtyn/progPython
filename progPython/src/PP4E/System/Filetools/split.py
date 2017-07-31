#!/usr/bin/python
"""
################################################################################
split a file into a set of parts; join.py puts them back together;
this is a customizable version of the standard Unix split command-line
utility; because it is written in Python, it also works on Windows and
can be easily modified; because it exports a function, its logic can
also be imported and reused in other applications;
################################################################################
"""

import sys
import os
KILOBYTES = 1024
MEGABYTES = KILOBYTES * 1000
CHUNKSIZE = int(1.4 * MEGABYTES)  # default: roughly a floppy


def split(fromfile, todir, chunksize=CHUNKSIZE):
    '''
    Splits one file in several chunks
    :param fromfile: source file to split
    :param todir: target directory
    :param chunksize: the chunksize in which we split
    '''
    if os.path.exists(todir):  # caller handles errors
        for fname in os.listdir(todir):  # delete any existing files
            os.remove(os.path.join(todir, fname))
    else:
        os.mkdir(todir)  # make dir, read/write parts

    partnum = 0
    input_ = open(fromfile, 'rb')  # use binary mode on Windows
    while True:  # eof=empty string from read
        chunk = input_.read(chunksize)  # get next part <= chunksize
        if not chunk:
            break
        partnum += 1
        filename = os.path.join(todir, ('part%04d' % partnum))
        fileobj = open(filename, 'wb')
        fileobj.write(chunk)
        fileobj.close()  # or simply open().write()
    input_.close()
    assert partnum <= 9999  # join sort fails if 5 digits
    return partnum


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: split.py [file-to-split target-dir [chunksize]]')
    else:
        if len(sys.argv) < 3:
            interactive = True
            fromfile = input('File to be split? ')  # input if clicked
            todir = input('Directory to store part files? ')
        else:
            interactive = False
            fromfile, todir = sys.argv[1:3]  # args in cmdline
            if len(sys.argv) == 4:
                CHUNKSIZE = int(sys.argv[3])
        absfrom, absto = [os.path.abspath(x) for x in [fromfile, todir]]
        print('Splitting', absfrom, 'to', absto, 'by', CHUNKSIZE)

        try:
            parts = split(fromfile, todir, CHUNKSIZE)
        except:
            print('Error during split:')
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            print('Split finished:', parts, 'parts are in', absto)
        if interactive:
            input('Press Enter key')  # pause if clicked
