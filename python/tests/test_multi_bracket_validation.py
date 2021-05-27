from challenges.multi_bracket_validation.multi_bracket_validation import *

def test_first():
    first = bracket_validation('{}')
    actual = first
    assert actual == first

def test_second():
    second = bracket_validation('{}(){}')
    actual = second
    assert actual == second

def test_third():
    third = bracket_validation('()[[Extra Characters]]')
    actual = third
    assert actual == third

def test_fourth():
    fourth = bracket_validation('(){}[[]]')
    actual = fourth
    assert actual == fourth

def test_fifth():
    fifth = bracket_validation('{}{Code}[Fellows](())')
    actual = fifth
    assert actual == fifth

def test_sixth():
    sixth = bracket_validation('[({}]')
    actual = sixth
    assert actual == sixth


# bracket_validation('{}')
# bracket_validation('{}(){}')
# bracket_validation('()[[Extra Characters]]')
# bracket_validation('(){}[[]]')
# bracket_validation('{}{Code}[Fellows](())')
# bracket_validation('[({}]')