"""
Тест-сьют №3
"""
import pytest


def test_case_001_addition_of_2_lines(function_addition_str):
    """
    Проверка сложения 2 строк
    """
    assert function_addition_str[2] == function_addition_str[0]+function_addition_str[1]


@pytest.mark.parametrize("input_num, result", [("5+5", 10), ("7-3", 4), ("3*2", 6), ("9/3", 3)])
def test_case_002_simple_math(input_num, result, math_message):
    """
    Проверка простых математических операций с числами
    """
    assert eval(input_num) == result


def test_case_003_multiplication_string():
    """
    Проверка умножения строки
    """
    assert 'A'*4 == 'AAAA'


@pytest.mark.parametrize("input_str, result", [("aunt", 4), ("uncle", 5), ("sister", 6)])
def test_case_004_check_the_length_of_string(input_str, result):
    """
    Проверка определения длины строки
    """
    assert len(input_str) == result


@pytest.mark.parametrize("first, second", [("one", "one"), ("immelman", "immelman")])
def test_case_005_check_parallele_str(first, second):
    """
    Проверка равенста строк
    """
    assert first == second


@pytest.mark.parametrize("param", [3, 5, 7])
def test_case_006_check_the_length_of_list(param):
    """
    Проверка определения длины списка
    """
    amount = param
    print("Количество элементов списка %s" % amount)
    numbers = [13] * amount
    print("Список: %s" % numbers)
    assert len(numbers) == amount


def test_case_007_check_addition_of_2_list():
    """
    Проверка сложения 2 списков
    """
    list1 = [2]*2
    list2 = [3]*3
    list1.extend(list2)
    assert list1 == [2, 2, 3, 3, 3]


@pytest.mark.parametrize("check_tuple, result", [((3, 5, 7), 3), ((2, 4), 2)])
def test_case_008_check_the_length_of_tuple(check_tuple, result):
    """
    Проверка определения длины кортежа
    """
    print("Количество элементов кортежа %s" % result)
    print("Кортеж: ", check_tuple)
    assert len(check_tuple) == result


def test_case_009_check_addition_of_2_tuple():
    """
    Проверка сложения 2 кортежей
    """
    tuple1 = ('One', 'Two', 'Three')
    tuple2 = ('GO', '!')
    assert tuple1 + tuple2 == ('One', 'Two', 'Three', 'GO', '!')


def test_case_010_check_copy_of_dict():
    """
    Проверка копирования словаря
    """
    dict_one = {1: 2, 2: 4, 3: 9, 4: 16}
    dict_two = dict_one.copy()
    assert dict_one == dict_two
