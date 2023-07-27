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

