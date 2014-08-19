# Testing

Testing is extremely important. Without testing, you cannot be sure that your code is doing what you think.
Testing is an integral part of software development, and should be done *while* you are writing code, not 
after the code has been written.

There are two main types of tests, both of which you should include in your code.

* Runtime (sanity) tests - these are light-weight tests performed while the code is running to ensure that everything is ok, e.g. arguments passed to a function make sense and are valid inputs.

* Correctness (unit) tests - these are heavier tests, typically run and written separately from the code, that test that the functions give the correct answers and behave in the expected way.

## Runtime tests

These are run in a function to ensure that the function is being called correctly with sensible (sane) arguments. For example, lets consider the following script;

```python
"""Module containing functions used to demonstrate
   the need for testing"""

def addArrays(a, b):
    """Function to add together the two passed arrays, returning
       the result."""

    c = []

    for i in range(0,len(a)):
        c.append( a[i] + b[i] )

    return c
```

Use `nano` to copy and paste the above script into a file called `addarrays.py`. Then open a new `ipython` session in the same directory as `addarrays.py` and type;

```python
from addarrays import *
c = addArrays( [1,2,3], [4,5,6] )
print(c)
```

should show that `c` is equal to `[5, 7, 9]`. Now type;

```python
c = addArrays( [1,2], [4,5,6] )
print(c)
```

Now `c` is seen to be equal to `[5, 7]`. Is this what you expected?

Now type;

```python
c = addArrays( [1,2,3], [4,5] )
```

This last one should cause an error to be raised that looks something like this;

```
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-4-de656a8188a3> in <module>()
----> 1 addarrays.addArrays( [1,2,3], [4,5] )
    
/path/to/addarrays.py in addArrays(a, b)
      7 
      8     for i in range(0,len(a)): 
----> 9         c.append( a[i] + b[i] )
     10 
     11     return c

IndexError: list index out of range
```

The problem is that `addArrays` expects both arrays to contain the same number of items. In the first case, the first array was smaller than the second, and this worked (surprisingly - but did it do what the user would expect? - should it have returned [5,7,6] instead?). In the second case, the function failed with a scary-looking error message.

To clean the function, we need to add a runtime test that checks that both arrays have the same length. If they don’t, then we need to report this back to the user using a sensible error message. We do this using an exception. Exit `ipython` and use `nano` to edit the `addarrays.py` script. Change it so that the function looks like this;

```python
def addArrays(a, b):
    """Function to add together the two passed arrays, returning
       the result."""

    if len(a) != len(b):
        raise ValueError("Both arrays must have the same length.")

    c = []

    for i in range(0,len(a)):
        c.append( a[i] + b[i] )

    return c
```

Here, we raise a `ValueError`, which indicates that something is wrong with the value of one of the arguments. A list of all Python exceptions is [here](http://docs.python.org/2/library/exceptions.html#exceptions.Exception). Also note that you can create your own exceptions as well, instructions [here](http://docs.python.org/2/tutorial/errors.html#user-defined-exceptions) (although this is beyond what we have time to cover in this course).

Now when we call the function incorrectly, we get a sensible error message. Check this by opening a new `ipython` session and typing;

```python
from addarrays import *
c = addArrays([1,2], [3,4,5])
```

and you should see;

```
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-2-fdd61ba0cb11> in <module>()
----> 1 addarrays.addArrays([1,2], [3,4,5])
    
/path/to/addarrays.py in addArrays(a, b)
      5 
      6     if len(a) != len(b):
----> 7         raise ValueError("Both arrays must have the same length.")
      8 
      9     c = []

ValueError: Both arrays must have the same length.
```

The benefit of an exception is that it provides a way for your function to test and report when something has gone wrong. If something has gone wrong, it can be reported back to the user with a sensible error message. Also, unlike just printing a message and exiting the program, exceptions provide a way to recover from errors. This is achieved using “try” blocks. For example try typing the following;

```python
a = [1,2]
b = [3,4,5]

try:
    c = addArrays(a,b)
    print(c)
except ValueError:
    print "Something went wrong calling addArrays"
```

You should see that the string `Something went wrong calling addArrays` is now printed to the screen.

A `try` block lets you try to run a piece of code. If an exception is raised, then the exception is caught in the `except` block. This can be used either to present an even cleaner error message, or to fix the problem, e.g. try typing this;

```python
a = [1,2]
b = [3,4,5]

try:
    c = addArrays(a,b)
except ValueError:
    while len(a) < len(b):
        a.append(0)
    while len(b) < len(a):
        b.append(0)
    c = addArrays(a,b)

print( c )
```

Now you will see that the `c` is equal to the array `[4, 6, 5]`. Because the arrays `a` and `b` were not the same length, the first call to `addArrays` in the `try` block caused a `ValueError` exception to be raised. This was caught in the `except ValueError` block. In here, because `a` was smaller than `b`, zeroes were appended onto `a` until it had the same size as `b`. Now the next call of `addArrays` in the `except ValueError` block was successful, allowing `c` to be created and printed at the end.

So you can see that exceptions allow us to fix problems in the context of how the function is called. Note that it would not be appropriate to add this fix into `addArrays` itself, as `addArrays` cannot know itself whether or not the arrays contain numbers, or whether or not it would be appropriate to make the arrays equal by padding with zeroes. Only the code that calls `addArrays` knows the context of the call, and thus what an appropriate fix would be. Exceptions provide a way for `addArrays` to signal that a problem has occurred, and the `try` block provides the way for the caller to fix the problem.

## Correctness tests

The second set of tests are correctness (also called unit) tests. These are tests that are run on a function to test that it is giving the correct output. For example, we can test that `addArrays` is adding together numbers correctly by creating a new function to test it, e.g. in a new `ipython` session type;

```python
from addarrays import *

def test_addArrays():
    a = [1,2,3]
    b = [4,5,6]
    expect = [5,7,9]
    c = addArrays(a,b)
    if c == expect:
        print "OK"
    else:
        print "BROKEN"

test_addArrays()
```

You should see that the test passed and the string `OK` was printed to the screen.

Testing manually works but is time-consuming and error prone - we might forget to run a test. What we need is a way to collect together all of the tests and to automate them.

The first thing to do is to create a testing script for our module, which is typically called “test_MODULENAME.py”, so in our case, it would be “test_addarrays.py”. Into this file, we should add all of our tests, e.g. using `nano` copy and paste in the following;

```python
from addarrays import *

def test_add():
    a = [1,2,3]
    b = [4,5,6]
    expect = [5,7,9]
    c = addArrays(a,b)
    assert( expect == c )
``` 

The only change here is that we have used `assert`. This is a function that does nothing if the passed test is true, but that will raise an `AssertationError` exception if the test is false. We can run the test manually using ipython, e.g. in a new `ipython` session type;

```python
from test_addarrays import *
test_add()
```

You should see that nothing happens, as the test passes.

This is still a bit manual. Fortunately, Python comes with `nosetests` which automates running test scripts like this. [nose](https://pypi.python.org/pypi/nose/) automatically finds, runs and reports on tests. Exit `ipython` and then, on the command line type;

```
nosetests test_addarrays.py
```

You should see printed to the screen;

```
.
----------------------------------------------------------------------
Ran 1 test in 0.004s
 
OK
```

This automatically ran all functions that started with “test_”. You can check this by breaking the code, e.g. edit `addarrays.py` and change the function to the following (replaces `a[i] + b[i]` with `a[i] - b[i]`);

```python
def addArrays(a, b):
    """Function to add together the two passed arrays, returning
       the result."""

    if len(a) != len(b):
        raise ValueError("Both arrays must have the same length.")

    c = []

    for i in range(0,len(a)):
        c.append( a[i] - b[i] )

    return c
```

Now go back to the command line and run `nosetests` again, e.g.

```
nosetests test_addarrays.py
```

You should now see something like

```
F
======================================================================
FAIL: test_addarrays.test_add
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/path/to/nose/case.py", line 197, in runTest
    self.test(*self.arg)
  File "/path/to/test_addarrays.py", line 9, in test_add
    assert( expect == c )
AssertionError

----------------------------------------------------------------------
Ran 1 test in 0.005s

FAILED (failures=1)
```

## When 1 + 1 = 2.0000001

One problem with testing that a calculation is correct is that computers don't do floating point arithmetic too well. For example, in a new `ipython` session type;

```python
expected = 0
actual = 0.1 + 0.1 + 0.1 - 0.3
assert(expected == actual)
```

While this may work, you will likely that an `AssertationError` exception was raised, e.g.

```
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-3-18a1029b2615> in <module>()
----> 1 assert(expected == actual)

AssertionError: 
```

We can see what caused the problem by printing the value of `actual`, e.g.

```python
print( actual )
```

On my machine, I get the value `5.55111512313e-17`.

The problem is that computers are continually rounding floating point numbers. Rounding errors can accumulate during a calculation and these can lead to seemingly wrong predictions such that `0.1 + 0.1 + 0.1 - 0.3 != 0`. Rounding errors can cause problems in your code, and also cause problems when writing tests. If you are going to compare floating point numbers, then you must make the comparison to within a threshold or delta, e.g. expected == actual  if expected - actual < 0.0000000000000001.

Thresholds are application-specific. Fortunately, `nose` provides an `assert_almost_equal` function that allows you to compare floating point numbers to within different thresholds. It does this by comparing two numbers up to a specified number of decimal places, e.g. type

```python 
from nose.tools import assert_almost_equal
assert_almost_equal(expected, actual, 0)
```

does nothing, because `5.55111512313e-17` is equal to 0 up to 0 decimal places.

Now type;

```python    
assert_almost_equal(expected, actual, 10)
```

This again does nothing, as `5.55111512313e-17` is equal to 0 up to 10 decimal places. Now try;

```python
assert_almost_equal(expected, actual, 16)
```

This should now raise an `AssertationError` exception that looks like this;

```
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-9-df3b297d7739> in <module>()
----> 1 assert_almost_equal(expected, actual, 16)

/path/to/unittest/case.pyc in assertAlmostEqual(self, first, second, places, msg, delta)
    561                                                           places)
    562         msg = self._formatMessage(msg, standardMsg)
--> 563         raise self.failureException(msg)
    564 
    565     def assertNotAlmostEqual(self, first, second, places=None, msg=None, delta=None):
    
AssertionError: 0 != 5.551115123125783e-17 within 16 places
```

## When should we test?

Testing is extremely important, and is the only way that you can check whether or not your code performs as you expect. Documentation tells the user what a function is supposed to do, while tests provide the guarantee that the function actually does it. Ideally you should write tests continually during development of software. For example, my workflow is to plan a new function, then write the documentation for the function (so that I don't forget my plan!), then write the function, and then write tests to ensure that the function is working. I am then able to move onto the next function I need to write, safe in the knowledge that the previous functions I have written will work and will not cause obscure and difficult to find bugs. Then, as I continue to develop the software, and it is used by other people, I will discover new bugs or will receive bug reports. I then turn these bug reports into new unit tests, so that, once fixed, those bugs cannot reappear in my code.

Obviously, we can't write tests to cover every problem, and indeed trying to write too large a test suite would cost us more time than would be worthwhile. However, you will quickly work out how much is the _right_ amount of testing, through trial and error. There is definitely no excuse for never testing, and any effort expended in writing tests is less painful than dealing with the aftermath of either;

* A bug being discovered in your script just before you publish a paper on the results, leading you to have to delay publication or, worse, have to make a retraction.
* Or (as happened once to myself) having to tell another scientist that all of their calculations have to be run again as the script they had been using had a bug that rendered all output incorrect.

In addition, you should also periodically review your tests, like code, to avoid

* Pass when they should fail, false positives.
* Fail when they should pass, false negatives.
* Don't test anything. 

Also, never, ever write 'empty' tests, such as;

```python
    def test_critical_correctness():
        # TODO - will complete this tomorrow!
        pass
```

These give a false sense of security!

## Summary

Testing

* Costs time while coding, but saves time in the long run (less effort spent debugging, less effort spent recovering from bugs found just before paper publication).
* Gives confidence that code does what we want and expect it to.
* Promotes trust that code, and so research, is correct.
* Mirrors your documentation. Documentation provides the promise of what the code will do. Tests provide the proof.

***

## Exercise

Expand `test_addarrays.py` with more tests, e.g. a function to test that `addArrays` correctly adds together arrays of negative numbers, a function to test that `addArrays` correctly adds arrays of strings, and a function to test that `addArrays` correctly adds together empty arrays. Try to think of all of the things that could break the code. Also add a function that tests that `addArrays` correctly reports when the arrays are the wrong size, e.g.

```python
def test_wrongsize():
    a = [1,2,3]
    b = [4,5]
    try:
        addArrays(a,b)
        assert(False)
    except ValueError:
        assert(True)
```

Also add in tests for floating point addition, using assert_almost_equal. Note that you will need to test each element of the array, one by one.

Run your tests with `nosetests`. 

If you get stuck, an example test script is [here](test_addarrays.md)

# [Previous](objects.md) [Up](README.md) [Next](whatnext.md)
