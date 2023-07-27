import pytest
from lib.personal_diary_system import *

'''
return first five words of given string
'''

def test_diary_returns_first_five_words_of_string():
    result = personal_diary_system("return first five words is")
    assert result == "return first five words is"

'''
if string is longer than 5 words
return first 5 words followed by ... instead of rest of string
'''

def test_diary_returns_more_than_five_words_of_string():
    result = personal_diary_system("return first five words is next step")
    assert result == "return first five words is..."
'''
if string is empty
return just the string
'''
def test_diary_returns_empty_string():
    result = personal_diary_system("")
    assert result == ""
'''
if argument is an integer
return error
'''
def test_diary_returns_error_for_non_string():
    # personal_diary_system(5)
    with pytest.raises(Exception) as e:
        result = personal_diary_system(5)
    error_message = str(e.value)
    assert error_message == "Please enter a string"