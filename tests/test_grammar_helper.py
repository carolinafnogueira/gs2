import pytest 
from lib.grammar_helper import *

def test_correct_text():
    result = grammar_helper("This is a nice text!")
    assert result == "This is a nice text!"

def test_needs_capitalisation():
    result = grammar_helper("this needs to be capitalised.")
    assert result == "This needs to be capitalised."

def test_needs_final_punctuation():
    result = grammar_helper("it nEEds fiNal punctuation")
    assert result == "It needs final punctuation."

def test_suitable_final_puctuation():
    result = grammar_helper("This is the final sentence,")
    assert result == "This is the final sentence."

def test_uppercase_sentence():
    result = grammar_helper("THIS IS OK!")
    assert result == "THIS IS OK!"

def test_text_starts_with_whitespaces():
    result = grammar_helper("    text starts with whitespaces.")
    assert result == "Text starts with whitespaces."

def test_text_ends_with_whitespaces():
    result = grammar_helper("text ends with whitespaces   ")
    assert result == "Text ends with whitespaces."

def test_mixed_case_return_capitalised():
    result = grammar_helper("tExT to CHEck!")
    assert result == "Text to check!"

def test_empty_string():
    with pytest.raises(Exception) as e:
        grammar_helper("")
    error_message = str(e.value)
    assert error_message == "No text to check."