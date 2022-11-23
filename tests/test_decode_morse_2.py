from morse import decode
import pytest


@pytest.mark.parametrize(
    "source_string, result", [
        ('... ..- -.', 'SUN'),
        ('... ?23 ...', KeyError),
        (123, AttributeError)
    ], )
def test_decode_morse(source_string: str, result):
    """ Проверяет результат функции на принадлежность к типу строки,
        в обратном случае перехватывает исключение """
    if isinstance(result, str):
        assert decode(source_string) == result
    else:
        with pytest.raises(result):
            decode(source_string)
