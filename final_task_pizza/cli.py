import click
import random
from typing import Union
from final_task_pizza.pizza import Margherita, Pepperoni, Hawaiian


@click.group()
def cli():
    pass


def log(pattern: str):
    def decorator(func):
        def wrapper(func_input):
            func_res = func(func_input)
            if isinstance(func_res, int):
                print(f'{pattern.format(func_res)}')
            else:
                print(func_res)
            return func_res

        return wrapper

    return decorator


@log('🧑🏻‍🍳 Приготовили за {}с!')
def bake(pizza: Union[Margherita, Pepperoni, Hawaiian]) -> Union[int, str]:
    """Bakes pizza"""

    if pizza.size == 'L':
        return random.randint(3, 6)
    elif pizza.size == 'XL':
        return random.randint(5, 8)
    else:
        return '❌️No such size of pizza. Please, choose L/XL.'


@log('🛵 Доставили за {}с!')
def deliver(pizza: Union[Margherita, Pepperoni, Hawaiian]) -> Union[int, str]:
    """Delivers pizza"""

    if pizza.size in ['L', 'XL']:
        return random.randint(5, 10)
    else:
        return '❌️No such size of pizza. Please, choose L/XL.'


@log('🏠 Забрали за {}с!')
def pick_up(pizza: Union[Margherita, Pepperoni, Hawaiian]) -> Union[int, str]:
    """Pick-up"""

    if pizza.size in ['L', 'XL']:
        return random.randint(7, 12)
    else:
        return '❌️No such size of pizza. Please, choose L/XL.'


@cli.command()
def menu():
    """Prints menu"""

    for pizza in (Margherita, Pepperoni, Hawaiian):
        print(f'- {pizza.name} {pizza.emoji}: {", ".join(pizza.ingredients)}')


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--pickup', default=False, is_flag=True)
@click.argument('pizza_name', nargs=1)
@click.argument('size', nargs=1)
def order(pizza_name: str, size: str, delivery: bool, pickup: bool):
    """Bakes and delivers pizza"""

    if pizza_name not in ('Margherita', 'Pepperoni', 'Hawaiian'):
        print('❌No such pizza in the menu')
        return None
    if pizza_name == 'Margherita':
        pizza = Margherita(size)
    elif pizza_name == 'Pepperoni':
        pizza = Pepperoni(size)
    else:
        pizza = Hawaiian(size)

    bake(pizza)

    if delivery:
        deliver(pizza)
    if pickup:
        pick_up(pizza)


if __name__ == '__main__':
    cli()
