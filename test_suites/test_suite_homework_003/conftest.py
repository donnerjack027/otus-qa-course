"""
Фикстуры
"""
import pytest


@pytest.fixture(scope="module", autouse=True)
def module_notification():
    """
    Уведомление о работе модуля
    """
    print('\nmodule_start')
    yield
    print('\nmodule_end')


@pytest.fixture(scope="session", autouse=True)
def session_notification():
    """
    Уведомление о работе сессии
    """
    print('\nsession_start')
    yield
    print('\nsession_end')


@pytest.fixture(scope="function", autouse=True)
def function_notification():
    """
    Уведомление о работе функции
    """
    print('\nfunction_start')
    yield
    print('\nfunction_end')


@pytest.fixture(scope="function")
def function_addition_str():
    """
    Предустановки сложения строк
    """
    str1 = 'A'
    str2 = 'B'
    result = 'AB'
    return str1, str2, result


@pytest.fixture()
def math_message():
    """
    teardown для тестов математики с числами
    """
    yield
    print("\nsimple math test - finished")
