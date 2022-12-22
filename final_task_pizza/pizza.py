class Pizza:
    """
    A class to represent a pizza.

    ...

    Attributes
    ----------
    name : str
        first name of the pizza
    emoji : str
        emoji that represents the pizza
    ingredients : list
        list of ingredients

    Methods
    -------
    __eq__():
        Returns True if two pizzas are equal else returns False.
    dict():
        Return recipe as a dict.
    """

    def __init__(self, name: str, emoji: str, ingredients: list):
        """
        Constructs all the necessary attributes for the pizza object.

        Parameters
        ----------
            name : str
                first name of the pizza
            emoji : str
                emoji that represents the pizza
            ingredients : list
                list of ingredients
        """

        self.name = name
        self.emoji = emoji
        self.ingredients = ingredients

    def __eq__(self, other: "Pizza") -> bool:
        """
        Returns True if two pizzas are equal else returns False.
        """

        if sorted(self.ingredients) == sorted(other.ingredients) \
                and self.name == other.name:
            return True
        return False

    def dict(self) -> dict:
        """
        Return recipe as a dict.
        """

        recipe = dict()
        recipe['ingredients'] = self.ingredients
        return recipe


class Margherita(Pizza):
    """
    Inherits after Pizza, has attributes of Margherita pizza.
    """

    name = 'Margherita'
    emoji = '🍅'
    ingredients = ['tomato sauce', 'mozzarella', 'tomatoes']

    def __init__(self, size: str):
        super().__init__(name=Margherita.name, emoji=Margherita.emoji,
                         ingredients=Margherita.ingredients)
        self.size = size


class Pepperoni(Pizza):
    """
    Inherits after Pizza, has attributes of Pepperoni pizza.
    """

    name = 'Pepperoni'
    emoji = '🍕'
    ingredients = ['tomato sauce', 'mozzarella', 'pepperoni']

    def __init__(self, size: str):
        super().__init__(name=Pepperoni.name, emoji=Pepperoni.emoji,
                         ingredients=Pepperoni.ingredients)
        self.size = size


class Hawaiian(Pizza):
    """
    Inherits after Pizza, has attributes of Hawaiian pizza.
    """

    name = 'Hawaiian'
    emoji = '🍍'
    ingredients = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']

    def __init__(self, size: str):
        super().__init__(name=Hawaiian.name, emoji=Hawaiian.emoji,
                         ingredients=Hawaiian.ingredients)
        self.size = size


if __name__ == '__main__':
    margherita_1 = Margherita(size='L')
    margherita_2 = Margherita(size='XL')
    pepperoni = Pepperoni(size='XL')

    print(margherita_1 == margherita_2)
    print(margherita_1 == pepperoni)
    print(margherita_1.dict())
