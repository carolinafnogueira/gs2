import pytest 
from lib.grammar_helper import *

'''
Given a lower case text string
It returns the string with the first word capitalised, and end punctuation
'''
def test_capitalises_lower_case_string():
    result = grammar_helper("this is an example to work on") 
    assert result == "This is an example to work on."

# Given a string already capitalised and with appropriate end punctuation
# It returns the same string
def test_returns_appropriate_string_as_is():
    result = grammar_helper("This string is fine as it is.") 
    assert result == "This string is fine as it is."