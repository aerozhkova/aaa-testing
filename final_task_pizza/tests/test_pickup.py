# python -m pytest final_task_pizza/tests/test_pickup.py -v

from final_task_pizza.cli import pick_up
from final_task_pizza.pizza import Margherita


def test_pick_up_l_xl():
    """ Проверяет функцию bake при размере пиццы L.
    Возвращает True, если результат входит в диапазон [3,6]."""

    margherita = Margherita(size='L')
    actual = pick_up(margherita)
    expected = range(5, 11)
    assert actual in expected


def test_pick_up_size_not_l_xl():
    """ Проверяет функцию bake при другом размере пиццы (не L и XL).
    Функция должна возвращать сообщение о неверном выборе размера."""

    margherita = Margherita(size='M')
    actual = pick_up(margherita)
    expected = '❌️No such size of pizza. Please, choose L/XL.'
    assert actual == expected
