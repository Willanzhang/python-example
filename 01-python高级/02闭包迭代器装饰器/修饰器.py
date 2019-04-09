def w1(func):
    def inner(*args, **kwargs):
        print(*args, kwargs)
        func('1')
    return inner

@w1
def f1(a):
    print('f1', a)
    return 'xxx'

# f1('zbw',c=12)

def w2(pre='xx'):
    def outer(func):
        def inner(*args):
            print('this is %s'%pre)
            return func(*args)
        return inner
    return outer

@w2('itcast')
def f2(a):
    print('哈哈哈%s'%a)
f2(': 123')