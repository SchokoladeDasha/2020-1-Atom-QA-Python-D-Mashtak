import pytest


@pytest.mark.parametrize('value, res', [(1, {0, 1, 2}), (3, {0, 1, 2, 3})])
def test_1(value, res):
    """
    проверка уникальности добавления элемента
    """
    i = {0, 1, 2}
    i.add(value)
    assert i == res


class TestSetGeneration:

    def test_2(self):
        """
        проверка создания множества из символов строки
        """
        a = set('hello')
        assert a == {'h', 'e', 'l', 'o'}

    def test_3(self):
        """
        проверка генерации множенства
        """
        a = {i * 2 for i in range(5)}
        assert a == {0, 2, 4, 6, 8}


def test_4():
    """
    проверка метода len()
    """
    a = {1, 5, 6, 7}
    assert len(a) == 4


def test_5():
    """
    проверка метода issubset(otherset)
    """
    a = {1, 4, 6}
    b = {6, 1}
    assert b.issubset(a)
