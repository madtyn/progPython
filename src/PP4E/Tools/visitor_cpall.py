"""  #pylint: disable=anomalous-backslash-in-string
Use: "python ...\Tools\visitor_cpall.py fromDir toDir trace?"
Like System\Filetools\cpall.py, but with the visitor classes and os.walk;
does string replacement of fromDir with toDir at the front of all the names
that the walker passes in; assumes that the toDir does not exist initially;
"""

import os
from .visitor import FileVisitor  # visitor is in '.'
from PP4E.System.Filetools.cpall import copyfile  # PP4E is in a dir on path


class CpallVisitor(FileVisitor):
    '''
    This class, when run, copies the whole file tree to another location
    '''
    def __init__(self, fromDir, toDir, trace=True):
        self.fromDirLen = len(fromDir) + 1
        self.toDir = toDir
        FileVisitor.__init__(self, trace=trace)

    def visitdir(self, dirpath):
        '''
        Creates the current directory in the new location
        :param dirpath: the directory path
        '''
        # Concats the target dir with the dirname
        toPath = os.path.join(self.toDir, dirpath[self.fromDirLen:])
        if self.trace:
            print('d', dirpath, '=>', toPath)
        os.mkdir(toPath)
        self.dcount += 1

    def visitfile(self, filepath):
        '''
        Copies the current file to the new location
        :param filepath: the file path
        '''
        toPath = os.path.join(self.toDir, filepath[self.fromDirLen:])
        if self.trace:
            print('f', filepath, '=>', toPath)
        copyfile(filepath, toPath)
        self.fcount += 1


if __name__ == '__main__':
    import sys
    import time
    FROM_DIR, TO_DIR = sys.argv[1:3]
    TRACE = len(sys.argv) > 3
    print('Copying...')
    start = time.clock()
    walker = CpallVisitor(FROM_DIR, TO_DIR, TRACE)
    walker.run(startDir=FROM_DIR)
    print('Copied', walker.fcount, 'files,', walker.dcount, 'directories', end=' ')
    print('in', time.clock() - start, 'seconds')
