'''
    Class representing a set
'''


class Set:
    '''
    Class representing a set
    '''
    def __init__(self, value=[]):  # on object creation
        self.data = []  # manages a local list
        self.concat(value)

    def intersect(self, other):  # other is any sequence type
        '''
        Returns the intersection with the other set
        :param other: the set to intersect with
        '''
        res = []  # self is the instance subject
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)  # return a new Set

    def union(self, other):
        '''
        Returns the union with the other set
        :param other: the set to unite with
        '''
        res = self.data[:]  # make a copy of my list
        for x in other:
            if x not in res:
                res.append(x)
        return Set(res)

    def concat(self, value):  # value: a list, string, Set...
        '''
        Appends a value to this set's data
        :param value: the value to append
        '''
        for x in value:
            if x not in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return '<Set:' + repr(self.data) + '>'
