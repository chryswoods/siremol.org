""" Possible answers to section 03: Pytest - Writing """

import pytest

def add(x, y):
    """ A function to add two numbers. """
    return x + y

@pytest.mark.parametrize("x, y, expected",
                        [(1, 2, 3),
                         (-4, 12,  8),
                         (37, 22, 59)])
def test_add(x, y, expected):
    """ Test the add function. """

    assert add(x, y) == pytest.approx(add(y, x)) == pytest.approx(expected)

def div(x, y):
    """ A function to divide two numbers. """
    return x / y

def test_div():
    """ Test the div function. """

    assert div(9, 2) == pytest.approx(4.5)

def isLucky(x):
    """ Return whether x is lucky number 7. """
    return x == 7

def test_isLucky():
    """ Test for the isLucky function. """

    # Test a big range of numbers.
    for x in range(-1000, 1000):

        # The value of 'x' is lucky number seven.
        if x == 7:
            assert isLucky(x)
        # We're not lucky.
        else:
            assert not isLucky(x)

def keyError():
    """ A function that raises a KeyError. """
    d = {}
    d['cat']

def test_keyError():
    with pytest.raises(KeyError):
        keyError()

def mul(x, y):
    """ A function to multiply two numbers. """
    return x * y

@pytest.mark.critical
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [3, 4])
def test_mul(x, y):
    """ Test the mul function. """

    assert mul(x, y) == pytest.approx(mul(y, x))
