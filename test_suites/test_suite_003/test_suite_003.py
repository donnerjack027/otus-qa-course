import pytest
from test_suites.common import fixtures


class TestSuite_003:

    @pytest.fixture(scope="module", autouse=True)
    def module_fix(self):
        print('\nmodule_start')

    def test_case_001_addition_of_2_lines(self, module_fix):
        print(module_fix)
        first_string = 'A'
        second_string = 'B'
        result = 'AB'
        assert result == first_string+second_string

    @pytest.mark.parametrize("input_num, result", [("5+5", 10), ("3*2", 6), ("9/3", 3)])
    def test_case_002_simple_math(self, input_num, result):
        print(input_num)
        print(result)
        assert eval(input_num) == result

    def test_case_003(self):
        print("3")

    def test_case_004(self):
        print("4")

    def test_case_005(self):
        print("5")

    def test_case_006(self):
        print("6")

    def test_case_007(self):
        print("7")

    def test_case_008(self):
        print("8")

    def test_case_009(self):
        print("9")

    def test_case_010(self):
        print("10")
