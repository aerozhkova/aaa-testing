# python -m pytest final_task_pizza/tests/test_deliver.py -v

from final_task_pizza.cli import deliver
from final_task_pizza.pizza import Margherita


def test_deliver_l_xl():
    """ Проверяет функцию bake при размере пиццы L.
    Возвращает True, если результат входит в диапазон [3,6]."""

    margherita = Margherita(size='L')
    actual = deliver(margherita)
    expected = range(7, 13)
    assert actual in expected


def test_deliver_size_not_l_xl():
    """ Проверяет функцию bake при другом размере пиццы (не L и XL).
    Функция должна возвращать сообщение о неверном выборе размера."""

    margherita = Margherita(size='M')
    actual = deliver(margherita)
    expected = '❌️No such size of pizza. Please, choose L/XL.'
    assert actual == expected
