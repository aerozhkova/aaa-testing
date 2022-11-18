# aaa-testing

## issue 1

Для запуска теста необходимо открыть терминал и запустить команду:
```
python -m doctest -o NORMALIZE_WHITESPACE -v tests/test_encode_morse_1.py
```

## issue 2

Для запуска теста необходимо открыть терминал и запустить команду:

```
python -m pytest tests/test_decode_morse_2.py
```

## issue 3

Для запуска теста необходимо открыть терминал и запустить команду:
```
python -m unittest tests/test_one_hot_encoder_unittest_3.py
```

## issue 4

Для запуска теста необходимо открыть терминал и запустить команду:
```
python -m pytest tests/test_one_hot_encoder_pytest_4.py -v
```

## issue 5

Для запуска теста необходимо открыть терминал и запустить команду:
```
python -m pytest tests/test_what_is_year_now_5.py -v
```
Для запуска теста с просмотром покрытия необходимо запустить команду:
```
python -m pytest -q tests/test_what_is_year_now_5.py --cov=what_is_year_now
```

В папке htmlcov находятся отчеты о покрытии с html файлами.
Для просмотра нужно скачать файл .html и открыть в браузере.
