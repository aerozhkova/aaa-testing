# python -m pytest final_task_pizza/tests/test_deliver.py -v

from final_task_pizza.cli import deliver
from final_task_pizza.pizza import Margherita


def test_deliver_l_xl():
    """ Checks function deliver with L or XL pizza size.
    Returns True if result is in range [7,12]. """

    margherita = Margherita(size='L')
    actual = deliver(margherita)
    expected = range(7, 13)
    assert actual in expected


def test_deliver_size_not_l_xl():
    """ Checks function deliver with another pizza size (not L and XL).
    Function must return a message about wrong choice of pizza size."""

    margherita = Margherita(size='M')
    actual = deliver(margherita)
    expected = '❌️No such size of pizza. Please, choose L/XL.'
    assert actual == expected
