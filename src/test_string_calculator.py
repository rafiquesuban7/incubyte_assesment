import pytest

from string_calculator import StringCalculator


@pytest.fixture
def calc():
    return StringCalculator()


def test_empty_string_returns_zero(calc):
    assert calc.add("") == 0


def test_single_number_returns_value(calc):
    assert calc.add("7") == 7


def test_two_numbers_comma_delimited(calc):
    assert calc.add("1,2") == 3


def test_unknown_amount_of_numbers(calc):
    assert calc.add("1,2,3,4,5") == 15


def test_newline_as_delimiter(calc):
    assert calc.add("1\n2,3") == 6


def test_custom_single_delimiter(calc):
    assert calc.add("//;\n1;2;3") == 6