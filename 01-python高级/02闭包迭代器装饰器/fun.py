def w1(func):
    print('1111')
    def inner():
      return '1111' + func() + '11111'
    return inner

def w2(func):
    print('2222')
    def inner():
      return '2222' + func() + '22222'
    return inner

@w1
@w2
def foo():
    return 'hello world'
# foo = lambda x: x + 1

print(foo())

def spaceName():
    print('spaceName111111')
