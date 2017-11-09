# test_addarrays.py

```python
from addarrays import addArrays
import pytest

def test_add():
    a = [1, 2, 3]
    b = [4, 5, 6]
    expect = [5, 7,9]
    c = addArrays(a, b)
    assert expect == c

def test_addneg():
    a = [-1, -2, -3]
    b = [-4, -5, -6]
    expect = [-5, -7, -9]
    c = addArrays(a, b)
    assert expect == c

def test_addstrings():
    a = ["Hello ", "ice-", "tea"]
    b = ["World", "cream", "bag"]
    expect = ["Hello World", "ice-cream", "teabag"]
    c = addArrays(a, b)
    assert expect == c

def test_addempty():
    a = []
    b = []
    expect = []
    c = addArrays(a, b)
    assert expect == c

def test_wrongsize():
    """
    Ensure that the function raises the correct exception when passed different length lists.
    """
    a = [1, 2, 3]
    b = [4, 5]
    with pytest.raises(ValueError):
        addArrays(a, b)

def test_addfloats():
    a = [0.1, 0.001, -0.00001]
    b = [0.00001, 0.001, 0.1]
    expect = [0.10001, 0.002, 0.09999]
    c = addArrays(a, b)

    assert pytest.approx(expect, abs=1e-10) == c
```

# [Previous](testing.md) [Up](README.md) [Next](testing.md)
