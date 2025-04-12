import pytest

from string_calculator import StringCalculator

def test_empty_string():
    assert StringCalculator().add("") == 0