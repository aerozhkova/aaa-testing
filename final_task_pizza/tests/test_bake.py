# python -m pytest final_task_pizza/tests/test_bake.py -v

from final_task_pizza.cli import bake
from final_task_pizza.pizza import Margherita


def test_bake_l():
    """ Проверяет функцию bake при размере пиццы L.
    Возвращает True, если результат входит в диапазон [3,6]."""

    margherita = Margherita(size='L')
    actual = bake(margherita)
    expected = range(3, 7)
    assert actual in expected


def test_bake_xl():
    """ Проверяет функцию bake при размере пиццы XL.
    Возвращает True, если результат входит в диапазон [3,6]."""

    margherita = Margherita(size='XL')
    actual = bake(margherita)
    expected = range(5, 9)
    assert actual in expected


def test_bake_size_not_l_xl():
    """ Проверяет функцию bake при другом размере пиццы (не L и XL).
    Функция должна возвращать сообщение о неверном выборе размера."""

    margherita = Margherita(size='M')
    actual = bake(margherita)
    expected = '❌️No such size of pizza. Please, choose L/XL.'
    assert actual == expected
