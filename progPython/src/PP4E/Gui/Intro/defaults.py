def simple():
    '''
    simple sample function
    '''
    spam = 'ni'

    def action():
        '''
        action function
        '''
        print(spam)  # name maps to enclosing function
    return action


act = simple()  # make and return nested function
act()  # then call it: prints 'ni'


def normal():
    '''
    normal sample function
    '''
    def action():
        '''
        action function
        '''
        return spam  # really, looked up when used
    spam = 'ni'
    return action


act = normal()
print(act())  # also prints 'ni'


def weird():
    spam = 42
    return (lambda: spam * 2)  # remembers spam in enclosing scope


act = weird()
print(act())  # prints 84


def weird2():
    tmp = (lambda: spam * 2)  # remembers spam
    spam = 42  # even though not set till here
    return tmp


act = weird2()
print(act())  # prints 84


def weird3():
    spam = 42
    handler = (lambda: spam * 2)  # func doesn't save 42 now
    spam = 50
    print(handler())  # prints 100: spam looked up now
    spam = 60
    print(handler())  # prints 120: spam looked up again now


weird3()


def odd():
    '''
    odd function
    '''
    funcs = []
    for c in 'abcdefg':
        funcs.append((lambda: c))  # c will be looked up later
    return funcs  # does not remember current c


for func in odd():
    print(func(), end=' ')  # print 7 g's, not a,b,c,... !


print()


def odd2():
    funcs = []
    for c in 'abcdefg':
        funcs.append((lambda c=c: c))  # force to remember c now
    return funcs  # defaults eval now


for func in odd2():
    print(func(), end=' ')  # OK: now prints a,b,c,...


print()
funcs_ = []  # enclosing scope is module
for c in 'abcdefg':  # force to remember c now
    funcs_.append((lambda c=c: c))  # else prints 7 g's again

for func in funcs_:
    print(func(), end=' ')  # OK: prints a,b,c,...
