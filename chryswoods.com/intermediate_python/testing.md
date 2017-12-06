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

    for a_, b_ in zip(a, b):
        c.append(a_ + b_)

    return c
```

Use `nano` to copy and paste the above script into a file called `addarrays.py`. Then open a new `ipython` session in the same directory as `addarrays.py` and type;

```python
from addarrays import addArrays
c = addArrays( [1,2,3], [4,5,6] )
print(c)
```

should show that `c` is equal to `[5, 7, 9]`. Now type;

```python
c = addArrays( [1,2], [4,5,6] )
print(c)
```

Now `c` is seen to be equal to `[5, 7]`. Is this what you expected?

The problem is that `addArrays` expects both arrays to contain the same number of items. The first array was smaller than the second, but it did not give any error. Should it have returned [5,7,6] instead?

To clean the function, we need to add a runtime test that checks that both arrays have the same length. If they don’t, then we need to report this back to the user using a sensible error message. We do this using an exception. Exit `ipython` and use `nano` to edit the `addarrays.py` script. Change it so that the function looks like this;

```python
def addArrays(a, b):
    """Function to add together the two passed arrays, returning
       the result."""

    if len(a) != len(b):
        raise ValueError("Both arrays must have the same length.")

    c = []

    for a_, b_ in zip(a, b):
        c.append(a_ + b_)

    return c
```

Here, we raise a `ValueError`, which indicates that something is wrong with the value of one of the arguments. A list of all Python exceptions is [here](http://docs.python.org/library/exceptions.html). Also note that you can create your own exceptions as well, instructions [here](http://docs.python.org/3/tutorial/errors.html#user-defined-exceptions) (although this is beyond what we have time to cover in this course).

Now when we call the function incorrectly, we get a sensible error message. Check this by opening a new `ipython` session and typing;

```python
from addarrays import addArrays
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
    print("Something went wrong calling addArrays")
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
from addarrays import addArrays

def test_add():
    a = [1,2,3]
    b = [4,5,6]
    expect = [5,7,9]
    c = addArrays(a,b)
    if c == expect:
        print("OK")
    else:
        print("BROKEN")

test_add()
```

You should see that the test passed and the string `OK` was printed to the screen.

Testing manually works but is time-consuming and error prone - we might forget to run a test. What we need is a way to collect together all of the tests and to automate them.

The first thing to do is to create a testing script for our module, which is typically called “test_MODULENAME.py”, so in our case, it would be “test_addarrays.py”. Into this file, we should add all of our tests, e.g. using `nano` copy and paste in the following;

```python
from addarrays import addArrays

def test_add():
    a = [1,2,3]
    b = [4,5,6]
    expect = [5,7,9]
    c = addArrays(a,b)
    assert expect == c
``` 

The only change here is that we have used `assert`. This is a statement that does nothing if the passed test is true, but that will raise an `AssertionError` exception if the test is false. We can run the test manually using ipython, e.g. in a new `ipython` session type:

```python
from test_addarrays import test_add
test_add()
```

You should see that nothing happens, as the test passes.

This is still a bit manual. Fortunately, there is a package called `pytest` which automates running test scripts like this. [pytest](https://pytest.org) automatically finds, runs and reports on tests. Exit `ipython` and then, on the command line type;

```
pytest
```

You should see printed to the screen;

```
============================= test session starts ==============================
platform linux -- Python 3.5.2, pytest-3.0.5, py-1.4.32, pluggy-0.4.0
rootdir: /panfs/panasas01/training/train01, inifile:
collected 1 items

test_addarrays.py .

=========================== 1 passed in 0.02 seconds ===========================
```

This automatically searched all the python files in the directory for functions that started with `test_` and ran them.
You can check this by breaking the code, e.g. edit `addarrays.py` and change the function to the following (replaces `a_ + b_` with `a_ - b_`);

```python
def addArrays(a, b):
    """Function to add together the two passed arrays, returning
       the result."""

    if len(a) != len(b):
        raise ValueError("Both arrays must have the same length.")

    c = []

    for a_, b_ in zip(a):
        c.append(a_ - b_)

    return c
```

Now go back to the command line and run `pytest` again, e.g.

```
pytest
```

You should now see something like

```
============================= test session starts ==============================
platform linux -- Python 3.5.2, pytest-3.0.5, py-1.4.32, pluggy-0.4.0
rootdir: /panfs/panasas01/training/train01, inifile:
collected 1 items

test_addarrays.py F

=================================== FAILURES ===================================
___________________________________ test_add ___________________________________

    def test_add():
        a = [1,2,3]
        b = [4,5,6]
        expect = [5,7,9]
        c = addArrays(a,b)
>       assert expect == c
E       assert [5, 7, 9] == [-3, -3, -3]
E         At index 0 diff: 5 != -3
E         Use -v to get the full diff

test_addarrays.py:8: AssertionError
=========================== 1 failed in 0.07 seconds ===========================
```

You can see that it has picked out the line at which the `assert` failed (marked with the `>` on the left).
What follows (on lines beginning with `E`) is then a little bit of help to see why it failed.
First it prints out the `assert` line again but with the variables expanded out so you can see exactly what it was comparing.
Then it tells you what part of the comparison failed, in this case it found that the first elements didn't match (`5 != -3`).

## When 1 + 1 = 2.0000001

One problem with testing that a calculation is correct is that computers don't do floating point arithmetic too well. For example, in a new `ipython` session type;

```python
expected = 0
actual = 0.1 + 0.1 + 0.1 - 0.3
assert expected == actual
```

While this may work, you will likely that an `AssertionError` exception was raised, e.g.

```
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-3-18a1029b2615> in <module>()
----> 1 assert expected == actual

AssertionError: 
```

We can see what caused the problem by printing the value of `actual`, e.g.

```python
print(actual)
```

On my machine, I get the value `5.55111512313e-17`.

The problem is that computers are continually rounding floating point numbers. Rounding errors can accumulate during a calculation and these can lead to seemingly wrong predictions such that `0.1 + 0.1 + 0.1 - 0.3 != 0`. Rounding errors can cause problems in your code, and also cause problems when writing tests. If you are going to compare floating point numbers, then you must make the comparison to within a threshold or delta, e.g. expected agrees with actual if `abs(expected - actual) < 0.0000000000000001`. Notice the use of python's inbuilt absolute value (`abs`) function - in this case, it is important that you specify this as the *absolute* difference. Otherwise, if ever `actual` is greater than `expected` (depsite being within the threshold), it will fail, not giving you what you were hoping for.

Thresholds are application-specific.
Fortunately, `pytest` provides an [`approx`](https://docs.pytest.org/en/latest/builtin.html#pytest.approx) function that allows you to compare floating point numbers to within different thresholds.
It does this by comparing two numbers up to a specified absolute or relative precision, e.g. type

```python 
import pytest
assert actual == pytest.approx(expected)
```

prints nothing, because `5.55111512313e-17` is equal to 0 to within a relative precision of `1e-6` (the default for `pytest.approx`).

Now type;

```python    
assert actual == pytest.approx(expected, abs=1e-10)
```

This again prints nothing, as `5.55111512313e-17` is equal to 0 up to 10 decimal places. Now try;

```python
assert actual == pytest.approx(expected, abs=1e-17)
```

This should now raise an `AssertionError` exception that looks like this;

```
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-44-c91bdbddaf67> in <module>()
----> 1 assert actual == pytest.approx(expected, abs=1e-17)

AssertionError:
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

One of the problems with testing is that you want to test if an action will be correct, without
necessarily performing the action. For example, you may want to test that your script will
correctly identify which files to remove, without actually removing those files. Or, you
may want to test that your script will correctly form the command line to run an external
program, without actually running that program. Mocking is the process of testing without
acting. If you want to learn more about mocking, see [this post](http://www.toptal.com/python/an-introduction-to-mocking-in-python).

***

## Exercise

Expand `test_addarrays.py` with more tests, e.g. a function to test that `addArrays` correctly adds together arrays of negative numbers, a function to test that `addArrays` correctly adds arrays of strings, and a function to test that `addArrays` correctly adds together empty arrays. Try to think of all of the things that could break the code. Also add a function that tests that `addArrays` correctly reports when the arrays are the wrong size, e.g.

```python
def test_wrongsize():
    a = [1, 2, 3]
    b = [4, 5]
    with pytest.raises(ValueError):
        addArrays(a, b)
```

Also add in tests for floating point addition, using `pytest.approx`.

Run your tests with `pytest`.

If you get stuck, an example test script is [here](test_addarrays.md)

# [Previous](objects.md) [Up](README.md) [Next](regexp.md)
