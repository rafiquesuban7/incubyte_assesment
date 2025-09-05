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


def test_negative_numbers_raise_with_all_negatives(calc):
    with pytest.raises(ValueError) as e:
        calc.add("1,-2,3,-4")
    assert "negative numbers not allowed: -2, -4" in str(e.value)


def test_ignore_numbers_greater_than_1000(calc):
    assert calc.add("2,1001") == 2
    assert calc.add("1000,1001,3") == 1003


def test_delimiters_of_any_length(calc):
    assert calc.add("//[***]\n1***2***3") == 6


def test_multiple_delimiters(calc):
    assert calc.add("//[*][%]\n1*2%3") == 6


def test_multiple_delimiters_with_length(calc):
    assert calc.add("//[***][%%]\n1***2%%3") == 6


def test_adjacent_delimiters_and_empty_tokens_are_ignored(calc):
    # Treat empty tokens as absent (common lenient behavior in kata solutions)
    assert calc.add("1,\n2") == 3

