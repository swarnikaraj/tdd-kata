import pytest

from src.string_calculator import StringCalculator

def test_empty_string():
    assert StringCalculator().add("") == 0


def test_single_number_return_value():
    assert StringCalculator().add("1")==1  