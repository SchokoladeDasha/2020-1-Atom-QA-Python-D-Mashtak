import pytest


def test_1():
    """
    проверка типа
    """
    a = 5
    assert type(a) == int


@pytest.mark.parametrize('sign, value', [('__add__',13), ('__sub__',3), ('__mul__',40), ('__floordiv__',1)])
def test_2(sign, value):
    """
    проверка основных операций c целыми числами
    """
    a = 8
    b = 5
    met = getattr(a, sign)
    assert met(b) == value


class TestIntMethods:

    def test_3(self):
        """
        проверка метода bit_length()
        """
        x = 204
        assert x.bit_length() == 8

    def test_4(self):
        """
        проверка метода to_bytes(length, byteorder)
        """
        x = 129
        assert x.to_bytes(2, 'big') == b'\x00\x81'

    def test_5(self):
        """
        проверка метода from_bytes(bytes, byteorder)
        """
        x = int.from_bytes(b'\x00\x7f', 'big')
        assert x == 127
