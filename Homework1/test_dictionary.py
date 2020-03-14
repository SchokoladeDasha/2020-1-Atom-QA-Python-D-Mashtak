import pytest


class TestDictGeneration:

    def test_1(self):
        """
        создание словаря с помощью функции dict
        """
        d = dict([(1, 2), (4, 8)])
        assert d == {1: 2, 4: 8}

    def test_2(self):
        """
        создание словаря с помощью функции fromkeys
        """
        d = dict.fromkeys(['a', 'b'], 5)
        assert d == {'a': 5, 'b': 5}

    def test_3(self):
        """
        создание словаря генератором
        """
        d = {a: a + 2 for a in range(4)}
        assert d == {0: 2, 1: 3, 2: 4, 3: 5}


@pytest.mark.parametrize('methods, val', [('keys', [0, 2]), ('values', [1, 3])])
def test_4(methods, val):
    d = {0: 1, 2: 3}
    met = getattr(d, methods)
    assert list(met()) == val

def test_5():
    d = {0: 1, 1: 3}
    with pytest.raises(KeyError):
        a = d[2]
