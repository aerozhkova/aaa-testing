from one_hot_encoder import fit_transform
import pytest


def test_fit_transform():
    """ Проверяет корректность работы функции """
    input_data = ['red',
                  'square',
                  'black',
                  'red',
                  'large']
    actual = fit_transform(input_data)
    expected = [
        ('red', [0, 0, 0, 1]),
        ('square', [0, 0, 1, 0]),
        ('black', [0, 1, 0, 0]),
        ('red', [0, 0, 0, 1]),
        ('large', [1, 0, 0, 0]),
    ]
    assert actual == expected


def test_fit_transform_raises_exception_on_input_type():
    """ Перехватывает исключение в случае
        типа int входных данных """
    input_data = 12345
    with pytest.raises(TypeError):
        fit_transform(input_data)


def test_fit_transform_isinstance():
    """ Проверяет результат на тип list """
    input_data = ['red',
                  'square',
                  'black',
                  'red',
                  'large']
    actual = fit_transform(input_data)
    expected = list
    assert type(actual) == expected


def test_fit_transform_input_string():
    """ Проверяет праавильность работы функции
        при входных данных, состоящих из одного элемента """
    input_data = 'red'
    actual = fit_transform(input_data)
    expected = [
        ('red', [1])
    ]
    assert actual == expected
