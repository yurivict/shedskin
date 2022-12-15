def baz(x, y, z = 3):
    return x, y, z

def boo(x, y, z='g'):
    return x, y, z

# default argument problem
def msplit(sep=0, spl=-1):
    return [""]

# def foo(*args): # this is not yet supported
#     return args

# def moo(**kwds): # this is not yet supported
#     return kwds

# def test_foo():
#     assert foo(1,2,3) == (1,2,3)
#     assert moo(a=1) == {'a':1}

class Klass:
    def foo(self, x = 3, y = 'hello'):
        return x, y

def test_baz():
    assert baz(1, 2, 3) == (1, 2, 3)
    assert baz(1, 3) == (1, 3, 3)

def test_boo():
    assert boo(z = 'z', y = 'y', x = 'x') == ('x', 'y', 'z')
    assert boo(y = 'y', x = 'x') == ('x', 'y', 'g')
    assert boo('x', y = 'y') == ('x', 'y', 'g')

def test_klass():
    assert Klass().foo(y = 'world', x = 42) == (42, 'world')

def test_msplit():
    assert msplit() == [""]


if __name__ == '__main__':
    test_baz()
    test_boo()
    # test_foo()
    test_klass()
    test_msplit()

