"Plus much more: process pools, managers, locks, condition,..."

from multiprocessing import Pool


def powers(x):
    '''
    Powers 2 to x
    :param x: the exponent
    '''
    # import os
    # print(os.getpid())                  # enable to watch children
    return 2 ** x


if __name__ == '__main__':
    workers = Pool(processes=5)

    results = workers.map(powers, [2] * 100)
    print(results[:16])
    print(results[-2:])

    results = workers.map(powers, range(100))
    print(results[:16])
    print(results[-2:])
