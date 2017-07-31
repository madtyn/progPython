"Use multiprocessing to start independent programs, os.fork or not"

import os
from multiprocessing import Process


def runprogram(arg):
    '''
    Runs the program
    :param arg: the argument
    '''
    os.execlp('python3', 'python3', 'child.py', str(arg))  # I had to change 'python' for 'python3' in both strings


if __name__ == '__main__':
    for i in range(5):
        Process(target=runprogram, args=(i,)).start()
    print('parent exit')
