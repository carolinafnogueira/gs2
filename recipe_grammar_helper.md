# {{Grammar Helper}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def grammar_helper(text_string):
    """Checks a string for capitalised text and correct final punctuation 

    Parameters: (list all parameters and their types)
        a string: a string containing words (e.g. "this is an example to work on")

    Returns: (state the return value and its type)
        a capitalised string with appropriate end punctuation (e.g. "This is an example to work on!")

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

'''
returns the same text if it's capitalised and with correct punctuation
'''
grammar_helper("This is a nice text!") => ["This is a nice text!"]

'''
capitalises the text entered when it starts with lowercase
'''
grammar_helper("this needs to be capitalised.") => ["This needs to be capitalised."]

'''
adds full stop if there isn't any punctuation
'''
grammar_helper("It needs final punctuation") => ["It needs final punctuation."]

'''
changes puctuation to full stop if puctuation given isn't appropriate
inappropriate punctuations => ":", ",", ";",
appropiate punctuations => "!", "?", "."
'''
grammar_helper("This is the final sentence,") => ["This is the final sentence."]

'''
doesn't change the 1st letter if the text is uppercase
'''
grammar_helper("THIS IS OK!") => ["THIS IS OK!"]

'''
given a text started with whitespace
delete whitespaces and capitalises the text
'''
grammar_helper("    text starts with whitespaces.") => ["Text starts with whitespaces."]


'''
text ends with whitespaces
delete whitespaces before checking puctuation
'''
grammar_helper("text ends with whitespaces   ") => ["Text ends with whitespaces."]

'''
Mixed lower and uppercase
Returns capitalised text
'''
grammar_helper("tExT to CHEck!") => ["Text to check!"]

'''
returns a message if it's an empty string
(raises Exception)
'''
grammar_helper("") => ["No text to check."]


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]

```

Ensure all test function names are unique, otherwise pytest will ignore them!


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_function_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
