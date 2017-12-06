""" Tests for the error throwing functions in mymodule."""

from ..mymodule import *

import pytest
import sys

def test_indexError():
    with pytest.raises(IndexError):
        indexError()

@pytest.mark.skipif(sys.platform != 'win32', reason="Only runs on Windows.")
def test_BSoD():
    blueScreenOfDeath()
