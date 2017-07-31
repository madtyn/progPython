"""
start up 10 copies of child.py running in parallel;
use spawnv to launch a program on Windows (like fork+exec);
P_OVERLAY replaces, P_DETACH makes child stdout go nowhere;
or use portable subprocess or multiprocessing options today!
"""

import os
import sys

for i in range(10):
    if sys.platform[:3] == 'win':
        PY_PATH = sys.executable
        os.spawnv(os.P_NOWAIT, PY_PATH, ('python3', 'child.py', str(i)))  # I had to replace 'python' for 'python3'
    else:
        pid = os.fork()
        if pid != 0:
            print('Process %d spawned' % pid)
        else:
            os.execlp('python3', 'python3', 'child.py', str(i))  # I had to replace 'python' for 'python3'
print('Main process exiting.')
