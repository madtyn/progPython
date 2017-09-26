"find biggest/smallest .py files in a tree (visitor version)"

import sys
import os
import pprint
from .visitor import FileVisitor


class BigPy(FileVisitor):
    '''
    Visitor based version of a script looking
    for the biggest file in a tree
    '''
    def __init__(self, trace=0):
        FileVisitor.__init__(self, context=[], trace=trace)

    def visitfile(self, filepath):
        FileVisitor.visitfile(self, filepath)
        if filepath.endswith('.py'):
            print(filepath)
            self.context.append((os.path.getsize(filepath), filepath))


if __name__ == '__main__':
    walker = BigPy()
    walker.run(sys.argv[1] if len(sys.argv) > 1 else '.')
    print('Visited %d files and %d dirs' % (walker.fcount, walker.dcount))
    walker.context.sort()
    pprint.pprint(walker.context[:2])
    pprint.pprint(walker.context[-2:])