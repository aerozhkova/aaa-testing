# python -m pytest final_task_pizza/tests/test_bake.py -v

from final_task_pizza.cli import bake
from final_task_pizza.pizza import Margherita


def test_bake_l():
    """ Checks function bake with L pizza size.
    Returns True if result is in range [3,6]."""

    margherita = Margherita(size='L')
    actual = bake(margherita)
    expected = range(3, 7)
    assert actual in expected


def test_bake_xl():
    """ Checks function bake with XL pizza size.
    Returns True if result is in range [5,8]."""

    margherita = Margherita(size='XL')
    actual = bake(margherita)
    expected = range(5, 9)
    assert actual in expected


def test_bake_size_not_l_xl():
    """ Checks function bake with another pizza size (not L and XL).
    Function must return a message about wrong choice of pizza size."""

    margherita = Margherita(size='M')
    actual = bake(margherita)
    expected = '❌️No such size of pizza. Please, choose L/XL.'
    assert actual == expected
