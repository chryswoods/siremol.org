""" Tests for the math functions in mymodule."""

from ..mymodule import *

import pytest

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
                        [(2, 1),
                         (9, 4),
                         pytest.param(3, 7, marks=pytest.mark.xfail(strict=False)),
                         pytest.param(6, 11, marks=pytest.mark.xfail(strict=True))])
def test_greaterThan(x, y):
    """ Test the greaterThan function. """

    assert greaterThan(x, y)

@pytest.mark.slow
def test_bigSum():
    """ Test the bigSum function. """

    assert bigSum() == 125000000250000000
