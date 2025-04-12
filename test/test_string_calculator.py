import pytest

from src.string_calculator import StringCalculator

def test_empty_string():
    assert StringCalculator().add("") == 0

def test_single_number_return_value():
    calculator=StringCalculator()
    assert calculator.add("1")==1
    assert calculator.add("2")==2  

def test_handle_any_amount_of_numbers():
    calculator=StringCalculator()
    assert calculator.add("1,2")==3
    assert calculator.add("3,2,4")==9  

def test_handle_newlines_between_numbers():
    calculator=StringCalculator()
    assert calculator.add("1\n2,3")==6    

def test_support_different_delimiters():
    calculator=StringCalculator()
    assert calculator.add("//;\n1;2")==3    