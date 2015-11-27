# Epilogue: Changes from Python 2 to Python 3

The syntax for functional and parallel programming in Python changed
slightly from Python 2 to Python 3. The changes are small, and relate
to the greater formality and cleanliness of the Python 3 language (e.g. greater use
of iterators, making nearly everything into a first class object 
and removing duplicate or confusing functionality).

Here are the things you will need to know if you want to 
use Python 3 to run this workshop;

## Standard map returns an iterator, not a list

Python 3 changed the return value of `map` from being a list of results to
being an iterator over the results. You convert from an iterator to
a list by typing `list(iterator)`, e.g.

```python

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

results = map( lambda x,y: x+y, a, b )
results = list(results)

print( results )
```

## The standard library no longer contains `reduce`

The developer of Python really doesn't like `reduce`, so it was
removed from the standard library. For the rationale, read
[this post](http://www.artima.com/weblogs/viewpost.jsp?thread=98196).

Fortunately, he was persuaded to change his mind, so `reduce`
was saved and moved to the `functools` module. If you want to use
`reduce`, type `from functools import reduce` at the top of your script, e.g.

```python
from functools import reduce

a = [ "cat", "dog", "fish" ]

result = reduce( lambda x,y: "%s %s" % (x,y), a )

print(result)
```

## Python 3 doesn't support auto-expansion of tuple arguments

The parallel `map` functions don't support functions with more
than one argument. We got around this by using a Python 2 feature
that supports auto-expansion of tuples in a function argument, e.g.

```python
def sum( (x,y) ):
    return x+y

print( sum( (4,5) ) )
```

Python 3 does not support this auto-expansion. Instead, you have
to expand the tuple manually as the first line of the function, e.g.

```python
def sum( args ):
    (x,y) = args
    return x+y

print( sum( (4,5) ) )
```

## Python >= 3.3 has a multiprocessing that supports context management

The `multiprocessing` module that comes with Python 3.3 or above has
been rewritten to support the context management protocol. This means
that you do not need to use `contextlib` when creating a `multiprocessing.Pool`
in a `with` statement. You are able to just write `with Pool() as pool:`,
and know that `pool.terminate()` will be automatically called when the
`with` block exits. For example, the multi-pool example from 
the [Part 2: Pool](pool_part2.md) section can be written as;

```python
from multiprocessing import Pool

def square(x):
    """Return the square of the argument"""
    return x*x

if __name__ == "__main__":

    a = [1, 2, 3, 4, 5]

    with Pool() as pool:
        result = pool.map( square, a )

    print("Square result: %s" % list(result))

    def cube(x):
        """Return the cube of the argument"""
        return x*x*x

    with Pool() as pool:
        result = pool.map( cube, a )

    print("Cube result: %s" % list(result))
```
 
***

# [Previous](epilogue.md) [Up](epilogue.md) [Next](gil.md)  
