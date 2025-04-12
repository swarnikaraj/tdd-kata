import pytest

from src.string_calculator import StringCalculator

def test_empty_string():
    assert StringCalculator().add("") == 0

def test_single_number_return_value():
    calculator=StringCalculator()
    assert calculator.add("1")==1
    assert calculator.add("2")==2  

def test_two_numbers_return_value():
    calculator=StringCalculator()
    assert calculator.add("1,2")==3
    assert calculator.add("3,2")==5   