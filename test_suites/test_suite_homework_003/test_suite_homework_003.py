"""
Тест-сьют №3
"""
import pytest


def test_case_001_addition_of_2_lines(function_addition_str):
    """
    Проверка сложения 2 строк
    """
    assert function_addition_str[2] == function_addition_str[0]+function_addition_str[1]


def test_case_002_addition_of_2_num(math_message):
    """
    Проверка сложения 2 чисел
    """
    assert 5+5 == 10, "5+5 != 10"


def test_case_003_subtraction_of_2_num(math_message):
    """
    Проверка вычитания 2 чисел
    """
    assert 7-3 == 4, "7-3 != 4"


def test_case_003_multiplication_of_2_num(math_message):
    """
    Проверка умножения 2 чисел
    """
    assert 3*2 == 6, "3*2 != 6"


def test_case_004_division_of_2_num(math_message):
    """
    Проверка деления 2 чисел
    """
    assert 9/3 == 3, "9/3 != 3"


def test_case_005_multiplication_string():
    """
    Проверка умножения строки
    """
    assert 'A'*4 == 'AAAA'


@pytest.mark.parametrize("input_str, result", [("aunt", 4), ("uncle", 5), ("sister", 6)])
def test_case_006_check_the_length_of_string(input_str, result):
    """
    Проверка определения длины строки
    """
    assert len(input_str) == result


@pytest.mark.parametrize("first, second", [("one", "one"), ("immelman", "immelman")])
def test_case_007_check_parallele_str(first, second):
    """
    Проверка равенста строк
    """
    assert first == second


@pytest.mark.parametrize("param", [3, 4, 5, 6, 7])
def test_case_008_check_the_length_of_list(param):
    """
    Проверка определения длины списка
    """
    amount = param
    print("Количество элементов списка %s" % amount)
    numbers = [13] * amount
    print("Список: %s" % numbers)
    assert len(numbers) == amount
