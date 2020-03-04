import pytest


class TestListGeneration:

    def test_1(self):
        """
        корректное создание пустого списка
        """
        empty_list = []
        assert empty_list == []

    def test_2(self):
        """
        корректное создание списка с объектами различных типов
        """
        list_1 = ['s', 23, ['words'], {'key': 'value'}, (2, 3, 4)]
        assert list_1 == ['s', 23, ['words'], {'key': 'value'}, (2, 3, 4)]

    def test_3(self):
        """
        корректная генерация элементов списка
        """
        list_2 = [c * 3 for c in 'hello']
        assert list_2 == ['hhh', 'eee', 'lll', 'lll', 'ooo']


def test_4():
    """
    отработка ошибки: выход за границы диапазона
    """
    list_3 = [1, 2, 3]
    with pytest.raises(IndexError):
        assert list_3[4]


@pytest.mark.parametrize('expected, i', [([[], 1, 2], 0), ([1, [], 2], 1), ([1, 2, []], 2)])
def test_5(expected, i):
    """
    корректное добавление пустого списка в существующий список
    """
    list_4 = [1, 2]
    list_4.insert(i, [])
    assert list_4 == expected
