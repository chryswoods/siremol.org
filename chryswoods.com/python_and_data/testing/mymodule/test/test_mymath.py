""" Tests for the math functions in mymodule."""

from ..mymodule import *

import pytest

@pytest.mark.xfail(reason="Broken code. Working on a fix.")
def test_add():
    """ Test the add function. """

    assert add(1, 1) ==  2
    assert add(1, 2) == add(2, 1) == 3

@pytest.mark.parametrize("x, y, expected",
                        [(1, 2, -1),
                         (7, 3,  4),
                         (21, 58, -37)])
def test_sub(x, y, expected):
    """ Test the sub function. """

    assert sub(x, y) == -sub(y, x) == expected

@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [3, 4])
def test_mul(x, y):
    """ Test the mul function. """

    assert mul(x, y) == mul(y, x)

@pytest.mark.skip(reason="Not yet implemented.")
def test_div():
    """ Test the div function. """

    assert div(9, 2) == approx(4.5)

@pytest.mark.parametrize("x, y",
                        [(108, 56),
                         (-64, -333),
                         (3, 7),
                         (74, 15)])
def test_greaterThan(x, y):
    """ Test the greaterThan function. """

    if x > y:
        assert greaterThan(x, y)
    else:
        assert not greaterThan(x, y)

def test_lucky():
    """ Test for the isLucky function. """

    # Test a big range of numbers.
    for x in range(-1000, 1000):

        # The value of 'x' is lucky number seven.
        if x == '7':
            assert isLucky(x)
        # We're not lucky.
        else:
            assert not isLucky(x)

@pytest.mark.slow
def test_bigSum():
    """ Test the bigSum function. """

    assert bigSum() == 20000000100000000
