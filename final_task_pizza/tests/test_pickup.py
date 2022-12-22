# python -m pytest final_task_pizza/tests/test_pickup.py -v

from final_task_pizza.cli import pick_up
from final_task_pizza.pizza import Margherita


def test_pick_up_l_xl():
    """ Checks function pick_up with L or XL pizza size.
    Returns True if result is in range [5,10]. """

    margherita = Margherita(size='L')
    actual = pick_up(margherita)
    expected = range(5, 11)
    assert actual in expected


def test_pick_up_size_not_l_xl():
    """ Checks function pick_up with another pizza size (not L and XL).
    Function must return a message about wrong choice of pizza size."""

    margherita = Margherita(size='M')
    actual = pick_up(margherita)
    expected = '❌️No such size of pizza. Please, choose L/XL.'
    assert actual == expected
