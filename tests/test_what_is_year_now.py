from what_is_year_now import what_is_year_now
from unittest.mock import patch
from io import StringIO


def test_urlopen_case1():
    with patch('what_is_year_now.urllib.request.urlopen') \
            as mocked_urlopen_cases:
        mocked_urlopen_cases.return_value = \
            StringIO('{"currentDateTime":"2019-03-01"}')
        assert what_is_year_now() == 2019
        mocked_urlopen_cases.assert_called_once()


def test_urlopen_case2():
    with patch('what_is_year_now.urllib.request.urlopen') \
            as mocked_urlopen_cases:
        mocked_urlopen_cases.return_value = \
            StringIO('{"currentDateTime":"01.03.2019"}')
        assert what_is_year_now() == 2019
        mocked_urlopen_cases.assert_called_once()


def test_urlopen_case3():
    with patch('what_is_year_now.urllib.request.urlopen') \
            as mocked_urlopen_cases:
        mocked_urlopen_cases.return_value = \
            StringIO('{"currentDateTime":"01/03/2019"}')
        try:
            assert what_is_year_now() == 2019
        except ValueError:
            pass
        mocked_urlopen_cases.assert_called_once()
