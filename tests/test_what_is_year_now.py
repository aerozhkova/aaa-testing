from what_is_year_now import what_is_year_now
from unittest.mock import patch
from io import StringIO
import pytest


def test_urlopen_format1():
    with patch('what_is_year_now.urllib.request.urlopen') \
            as mocked_urlopen_cases:
        mocked_urlopen_cases.return_value = \
            StringIO('{"currentDateTime":"2019-03-01"}')
        assert what_is_year_now() == 2019
        mocked_urlopen_cases.assert_called_once()


def test_urlopen_format2():
    with patch('what_is_year_now.urllib.request.urlopen') \
            as mocked_urlopen_cases:
        mocked_urlopen_cases.return_value = \
            StringIO('{"currentDateTime":"01.03.2019"}')
        assert what_is_year_now() == 2019
        mocked_urlopen_cases.assert_called_once()


def test_urlopen_other_format():
    with patch('what_is_year_now.urllib.request.urlopen') \
            as mocked_urlopen_cases:
        mocked_urlopen_cases.return_value = \
            StringIO('{"currentDateTime":"01/03/2019"}')
        with pytest.raises(ValueError):
            what_is_year_now()
        mocked_urlopen_cases.assert_called_once()
