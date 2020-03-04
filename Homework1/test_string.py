import pytest


class TestStringMethods:

    def test_1(self):
        """
        проверка метода len(string)
        """
        str_1 = 'some'
        assert len(str_1) == 4

    def test_2(self):
        """
        проверка метода split(symbol)
        """
        str_2 = 'I_am_a_superhero'
        a = str_2.split('_')
        assert a == ['I', 'am', 'a', 'superhero']


@pytest.mark.parametrize('i, val', [(0,'h'),(1,'e'),(2,'l'),(3,'l'),(4,'o')])
def test_3(i, val):
    """
    проверка по индексу
    """
    str_3 = 'hello'
    assert str_3[i] == val


def test_4():
    """
    соединение строк с разным типом кавычек при задании
    """
    a = 'part1'
    b = "part2"
    assert a + b == 'part1part2'


def test_5():
    """
    отлов ошибки при попытке изменить строку
    """
    str_4 = 'abc'
    with pytest.raises(TypeError):
        str_4[1] = 'a'
        assert str_4 == 'aac'
