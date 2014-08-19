# test_addarrays.py

```python
from addarrays import *
from nose.tools import assert_almost_equal

def test_add():
    a = [1,2,3]
    b = [4,5,6]
    expect = [5,7,9]
    c = addArrays(a,b)
    assert( expect == c )

def test_addneg():
    a = [-1, -2, -3]
    b = [-4, -5, -6]
    expect = [-5, -7, -9]
    c = addArrays(a,b)
    assert( expect == c )

def test_addstrings():
    a = ["Hello ", "ice-", "tea"]
    b = ["World", "cream", "bag"]
    expect = [ "Hello World", "ice-cream", "teabag" ]
    c = addArrays(a,b)
    assert( expect == c )

def test_addempty():
    a = []
    b = []
    expect = []
    c = addArrays(a, b)
    assert( expect == c )

def test_wrongsize():
    a = [1,2,3]
    b = [4,5]
    try:
        addArrays(a,b)
        assert(False)
    except ValueError:
        assert(True)

def test_addfloats():
    a = [0.1, 0.001, -0.00001]
    b = [0.00001, 0.001, 0.1]
    expect = [0.10001, 0.002, 0.09999]
    c = addArrays(a,b)

    for i in range(0, len(expect)):
        assert_almost_equal( expect[i], c[i], 10 )
```

# [Previous](testing.md) [Up](README.md) [Next](testing.md)
