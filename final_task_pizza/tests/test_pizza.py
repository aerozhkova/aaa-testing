# python -m pytest final_task_pizza/tests/test_pizza.py -v


from final_task_pizza.pizza import Pizza


def test_pizza_eq_equal():
    """ Проверяет метод __eq__ класса Pizza.
    Метод должен возвращать True при сравнении одинаковых пицц."""

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
    """ Проверяет метод __eq__ класса Pizza.
    Метод должен возвращать False при сравнении неодинаковых пицц."""

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
    """ Проверяет метод dict класса Pizza.
    Метод должен возвращать рецепт в виде словаря. """

    hawaiian = Pizza(name='Hawaiian',
                     ingredients=['tomato sauce', 'mozzarella', 'chicken',
                                  'pineapples'],
                     emoji='🍍')
    actual = hawaiian.dict()
    expected = {'ingredients': ['tomato sauce', 'mozzarella', 'chicken',
                                'pineapples']}
    assert actual == expected
