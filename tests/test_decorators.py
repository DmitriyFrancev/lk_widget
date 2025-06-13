import os.path

import pytest

from src.decorators import log


@log()
def simple_sum(x, y):
    return x + y


@log()
def simple_division(x, y):
    return x / y


@log('test_log_file.txt')
def simple_sum_test (x, y):
    return x + y


def test_log_decorator_ok(capsys):
    simple_sum(12, 45)
    captured = capsys.readouterr()
    assert captured.out == 'simple_sum ok\n\n'


def test_log_decorator_error(capsys):
    simple_division(4, 0)
    captured = capsys.readouterr()
    assert captured.out == 'simple_division error: ZeroDivisionError. Inputs: (4, 0),{})\n\n'


def test_log_decorator_filename_ok():
    simple_sum_test(12, 12)
    assert os.path.exists('test_log_file.txt')
    with open ('test_log_file.txt', 'r') as file:
        content = file.read()
    assert 'simple_sum ok\n' in content
    os.remove('test_log_file.txt')


def test_log_decorator_filename_error():
    simple_sum_test(12, 'abc')
    assert os.path.exists('test_log_file.txt')
    with open ('test_log_file.txt', 'r') as file:
        content = file.read()
    assert "test_simple_sum error: TypeError. Inputs: (12, 'abc'),{})\n" in content
    os.remove('test_log_file.txt')



