# aaa-testing

## issue 1

Для запуска теста необходимо открыть терминал и запустить команду:
```
python -m doctest -o NORMALIZE_WHITESPACE -v tests/test_encode_morse.py
```

## issue 2

Для запуска теста необходимо открыть терминал и запустить команду:

```
python -m pytest tests/test_decode_morse.py
```

## issue 3

Для запуска теста необходимо открыть терминал и запустить команду:
```
python -m unittest tests/test_one_hot_encoder_unittest.py
```

## issue 4

Для запуска теста необходимо открыть терминал и запустить команду:
```
python -m pytest tests/test_one_hot_encoder_pytest.py -v
```

## issue 5

Для запуска теста необходимо открыть терминал и запустить команду:
```
python -m pytest tests/test_what_is_year_now.py -v
```
Для запуска теста с просмотром покрытия необходимо запустить команду:
```
python -m pytest -q tests/test_what_is_year_now.py --cov=what_is_year_now
```

В папке htmlcov находятся отчеты о покрытии с html файлами.
Для просмотра нужно скачать файл .html и открыть в браузере.
