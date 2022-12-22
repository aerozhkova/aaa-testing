# python -m pytest final_task_pizza/tests/test_pizza.py -v

from final_task_pizza.pizza import Pizza


def test_pizza_eq_equal():
    """ Checks method __eq__ of class Pizza.
    Method must return True if pizzas are equal."""

    margherita_1 = Pizza(name='Margherita',
                         ingredients=['tomato sauce', 'mozzarella',
                                      'tomatoes'],
                         emoji='🍅')
    margherita_2 = Pizza(name='Margherita',
                         ingredients=['tomato sauce', 'mozzarella',
                                      'tomatoes'],
                         emoji='🍅')
    actual = margherita_1 == margherita_2
    expected = True
    assert actual == expected


def test_pizza_eq_not_equal():
    """ Checks method __eq__ of class Pizza.
    Method must return False if pizzas are unequal."""

    margherita = Pizza(name='Margherita',
                       ingredients=['tomato sauce', 'mozzarella', 'tomatoes'],
                       emoji='🍅')
    pepperoni = Pizza(name='Pepperoni',
                      ingredients=['tomato sauce', 'mozzarella', 'pepperoni'],
                      emoji='🍕')
    actual = margherita == pepperoni
    expected = False
    assert actual == expected


def test_pizza_dict():
    """ Checks method dict of class Pizza.
    Method must return recipe as a dict. """

    hawaiian = Pizza(name='Hawaiian',
                     ingredients=['tomato sauce', 'mozzarella', 'chicken',
                                  'pineapples'],
                     emoji='🍍')
    actual = hawaiian.dict()
    expected = {'ingredients': ['tomato sauce', 'mozzarella', 'chicken',
                                'pineapples']}
    assert actual == expected
