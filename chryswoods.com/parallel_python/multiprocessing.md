
# Part 2: Multiprocessing

Python has many libraries available to help you parallelise your
scripts across the cores of a single multicore computer. 
The established option is the `multiprocessing` library. You can import
`multiprocessing` by typing into ipython

```python
import multiprocessing
```

You can read the documentation for this module by typing

```python
help(multiprocessing)
```

One of the useful functions in `multiprocessing` is `cpu_count()`. 
This returns the number of CPUs (computer cores) available on
your computer to be used for a parallel program. Type into 
ipython

```python
print(multiprocessing.cpu_count())
```

to see how many cores you have available.

Nearly all modern computers have several processor cores, so you should
see that you have at least 2, and perhaps as many as 40 available 
on your machine. Each of these cores is available to do work, in 
parallel, as part of your Python script. For example, if you have
two cores in your computer, then your script should ideally be
able to do two things at once. Equally, if you have forty cores 
available, then your script should ideally be able to do forty
things at once.

Multiprocessing allows your script to do lots of things at once
by actually running multiple copies of your script in parallel,
with (normally) one copy per processor core on your computer.
One of these copies is known as the master copy, and is
the one that is used to control all of worker copies. Because
of this, multiprocessing python code has to be written into
a text file and executed using the `python` interpreter. It
is not recommended to try to run a multiprocessing python script
interactively, e.g. via ipython or ipython notebook. In addition,
because multiprocessing achieves parallelism by running multiple
copies of your script, it forces you to write it in a particular way. All
imports should be at the top of the script, followed by all
function and class definitions. This is to ensure that all
copies of the script have access to the same modules, functions
and classes. Then, you should ensure that only
the master copy of the script runs the code by protecting it
behind an `if __name__ == "__main__"` statement. 

An example (non-functional) script is shown below;

```python
# all imports should be at the top of your script
import multiprocessing
import sys
import os

# all function and class definitions must be next
def add(x, y):
    """Function to return the sum of the two arguments"""
    return x+y

def product( x, y ):
    """Function to return the product of the two arguments"""
    return x*y

if __name__ == "__main__":
    # You must now protect the code being run by
    # the master copy of the script by placing it

    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]

    # Now write your parallel code...
    etc. etc.
```

(if you are interested, take a [look here](gil.md) for more information
about why parallel Python is based on forking multiple processes,
rather than splitting multiple threads)

***

# [Previous](part2.md) [Up](part2.md) [Next](pool_part2.md)  
