# python -m pytest --cov .

from morse import decode
import pytest


@pytest.mark.parametrize(
    "source_string, result", [
        ('... ..- -.', 'SUN'),
        ('... ?23 ...', KeyError),
        (123, AttributeError)
    ], )
def test_decode_morse(source_string: str, result):
    try:
        decode(source_string) == result
    except (KeyError, AttributeError):
        print(f'Test raised {result} at ', source_string)
