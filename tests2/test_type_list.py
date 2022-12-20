
def ident(x):
    return x

def hu(n, s=-1):
    return [1]


def test_list_misc():
    assert [[i] for i in range(5)] == [[0], [1], [2], [3], [4]]
    assert [(2*a, b) for a in range(4) if a > 0 for b in ['1','2']] == [(2, '1'), (2, '2'), (4, '1'), (4, '2'), (6, '1'), (6, '2')]
    assert ['' for i in range(2)] == ['', '']

    ah = []
    ident(ah).append(1)
    ident(ah).append(1.0)
    assert ah ==  [1, 1.0]

def test_list_comp():
    bla = [1,2]
    dinges = [1,2]
    jada = [1,2]
    assert [x for x in bla] == bla
    assert [[a for a in bla] for c in dinges] == [[1, 2], [1, 2]]
    assert [[[a for a in jada] for c in bla] for d in dinges] == [[[1, 2], [1, 2]], [[1, 2], [1, 2]]]
    assert [0 for s in ["hah"]] == [0]
    assert [bah.upper() for bah in ("hah", "bah")] == ['HAH', 'BAH']
    assert [0 for (str, bah) in [("hah", "bah")]] == [0]
    assert [i for i in hu(10)] == [1]

def test_list_nested():
    c = [[1,2],(3,4)]
    q = [[[1],[2]],[[3],[4]]]
    fs = [i+1.2 for i in [1, 1., 2., 3.2]]
    assert list(i+1.2 for i in [1, 1., 2., 3.2]) == [2.2, 2.2, 3.2, 4.4]

    assert c[0] == [1,2]
    assert c[1] == (3,4)
    assert q[0][0][0] == 1
    assert q[0][1][0] == 2
    assert q[1][0][0] == 3
    assert q[1][1][0] == 4


def test_list_slice():
    a = [1,2,3,4,5]
    assert a[:-1] == [1, 2, 3, 4]
    assert a[1:3] == [2, 3]
    assert a[::]  == [1, 2, 3, 4, 5]
    assert a[:3:] == [1, 2, 3]
    assert a[::-1] == [5, 4, 3, 2, 1]

def test_list_append():
    a = []
    a.append(1.0)
    assert a[0] == 1.0

    b = []
    b.append(1)
    assert b[0] == 1

    c = []
    c.append("astring")
    assert c[0] == "astring"

    d = []
    d.append("1")
    assert d[0] == "1"

    e = []
    e.append([1])
    assert e[0] == [1]

def test_tuple_in_list():
    list4 = [(1,2),(3,4)]
    assert (1,2) in list4


def test_list_assign():
    list5 = [(1,2),(3,4)]
    list5[0] = (2,2)
    assert list5 == [(2,2),(3,4)]

def test_list_length():
    puzzlecolumns = [1]
    assert puzzlecolumns.__len__() == 1

# def test_list_copy():
#     a = [(1,2),(3,4)]
#     b = list4.copy() # NotImplemented
#     assert b[0] == [1,2]

def test_all():
    test_list_assign()
    test_list_append()
    test_tuple_in_list()
    test_list_slice()
    test_list_length()
    test_list_comp()
    test_list_misc()


if __name__ == "__main__":
    test_all()


