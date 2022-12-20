

xs = range(10)

seq = [(1,2), (3,4)]

cube = [(1,2),(3,4),(5,6)]

def hoei(cube):
    for pos in cube:
        x = pos
    return x



def test_for_range():
    result = []
    for i in xs:
        result.append(i)
    assert result == [0,1,2,3,4,5,6,7,8,9]

def test_for_tuple():
    result = []
    for i in seq:
        result.append(i)
    assert result == seq

def test_for_fn():
    assert hoei(cube) == (5,6)

def test_for_enumerate():
    result_i = []
    result_o = []
    for i, o in enumerate(cube):
        result_i.append(i)
        result_o.append(o)
    assert result_i == [0,1,2]
    assert result_o == cube


def test_all():
    test_for_range()
    test_for_tuple()
    test_for_fn()
    test_for_enumerate()

if __name__ == '__main__':
    test_all() 

