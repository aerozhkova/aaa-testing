from hw5.what_is_year_now import what_is_year_now
from unittest.mock import patch
from io import StringIO
import pytest


def test_urlopen_dash_format():
    """ Проверяет работу функции при формате YYYY-MM-DD
            вернувшегося из поля даты значения """
    with patch('what_is_year_now.urllib.request.urlopen',
               return_value=StringIO('{"currentDateTime":"2019-03-01"}')) \
            as mocked_urlopen_cases:
        assert what_is_year_now() == 2019
        mocked_urlopen_cases.assert_called_once()


def test_urlopen_dot_format():
    """ Проверяет работу функции при формате DD.MM.YYYY
        вернувшегося из поля даты значения """
    with patch('what_is_year_now.urllib.request.urlopen',
               return_value=StringIO('{"currentDateTime":"01.03.2019"}')) \
            as mocked_urlopen_cases:
        assert what_is_year_now() == 2019
        mocked_urlopen_cases.assert_called_once()


def test_urlopen_unknown_format():
    """ Перехватывает исключение в случае
        неизвестного формата даты """
    with patch('what_is_year_now.urllib.request.urlopen',
               return_value=StringIO('{"currentDateTime":"01/03/2019"}')) \
            as mocked_urlopen_cases:
        with pytest.raises(ValueError):
            what_is_year_now()
        mocked_urlopen_cases.assert_called_once()
