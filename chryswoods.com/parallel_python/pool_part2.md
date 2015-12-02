
# Part 2: Pool

One of the core multiprocessing features is `multiprocessing.Pool`. This
provides a pool of workers that can be used to parallelise a map.

For example, create a new script called `pool.py` and type into it;

```python
from multiprocessing import Pool, cpu_count

def square(x):
    """Function to return the square of the argument"""
    return x*x

if __name__ == "__main__":
    # print the number of cores
    print("Number of cores available equals %d" % cpu_count())

    # create a pool of workers
    pool = Pool()

    # create an array of 5000 integers, from 1 to 5000
    a = range(1,5001)

    result = pool.map( square, a )

    total = reduce( lambda x,y: x+y, result )

    print("The sum of the square of the first 5000 integers is %d" % total)
```

Run the script using the command

```
python pool.py
```

You should see that it prints out the result

```
Number of cores available equals 4
The sum of the square of the first 5000 integers is 41679167500
```

(the number of cores will depend on the number available on your machine)

So how does this work? The line

```python
pool = Pool()
```

has created a pool of worker copies of your script, with the number of workers
equalling the number of cores reported by `cpu_count()`. You can control the
number of copies by specifying the value of `processes` in the constructor for `Pool`, e.g.

```python
pool = Pool(processes=5)
```

would create a pool of five workers.

The line

```python
a = range(1,5001)
```

is a quick way to create a list of 5000 integers, from 1 to 5000. The parallel
work is conducted on the line

```python
result = pool.map( square, a )
```

This performs a map of the function `square` over the list of items of `a`. 
The map is divided up over all of the workers in the pool. This means that,
if you have 10 workers (e.g. if you have 10 cores), then each worker
will perform only one tenth of the work (e.g. calculating the square of 500
numbers). If you have 2 workers, then each worker will perform only half of 
the work (e.g. calculating the square of 2500 numbers).

The next line

```python
total = reduce( lambda x,y: x+y, result )
```

is just a standard `reduce` used to sum together all of the results.

You can verify that the `square` function is divided between your workers
by using a `multiprocessing.current_process().pid` call, which will
return the process ID (PID) of the worker process. Edit your `pool.py`
script and set the contents equal to;

```python
from multiprocessing import Pool, current_process

def square(x):
    """Function to return the square of the argument"""
    print("Worker %s calculating square of %d" % \
             (current_process().pid, x))
    return x*x

if __name__ == "__main__":
    nprocs = 2

    # print the number of cores
    print("Number of workers equals %d" % nprocs)

    # create a pool of workers
    pool = Pool(processes=nprocs)

    # create an array of 10 integers, from 1 to 10
    a = range(1,11)

    result = pool.map( square, a )

    total = reduce( lambda x,y: x+y, result )

    print("The sum of the square of the first 10 integers is %d" % total)
```

Run this script using

```
python pool.py
```

You should see output that is something like

```
Number of workers equals 2
Worker 6190 calculating square of 1
Worker 6190 calculating square of 2
Worker 6190 calculating square of 5
Worker 6190 calculating square of 6
Worker 6191 calculating square of 3
Worker 6191 calculating square of 4
Worker 6190 calculating square of 7
Worker 6190 calculating square of 8
Worker 6191 calculating square of 9
Worker 6191 calculating square of 10
The sum of the square of the first 10 integers is 385
```

(the exact PIDs of the workers, and the order in which they print
will be different on your machine)

You can see in the output that there are two workers, signified by the
two different worker PIDs. The work has been divided evenly amongst
them. Edit `pool.py` and change the value of `nprocs`. How is the work
divided as you change the number of workers?

## Using multiple pools in a single script

You can use more than one `multiprocessing.Pool` at a time in your script,
but you should ensure that you use them one after another. The way
`multiprocessing.Pool` works is to fork your script into the team of workers
 when you create a `Pool` object. Each worker contains a complete copy of all
of the functions and variables that exist *at the time of the fork*. This
means that any changes after the fork will not be held by the other workers,
e.g. open a new python script called `broken_pool.py` and type

```python
from multiprocessing import Pool

def square(x):
    """Return the square of the argument"""
    return x*x

if __name__ == "__main__":

    a = [1, 2, 3, 4, 5]

    pool = Pool()

    result = pool.map( square, a )

    print("Square result: %s" % result)

    def cube(x):
        """Return the cube of the argument"""
        return x*x*x

    result = pool.map( cube, a )

    print("Cube result: %s" % result)
```

If you run this script you should see an error such as

```
AttributeError: 'module' object has no attribute 'cube'
```

(you may also find that your python script hangs and cannot be
killed. To kill the script, hold `CTRL` and `Z` to background 
the task, then type `kill -9 %1` to kill the python script)

The problem is that `pool` was created before the `cube` function.
The worker copies of the script were thus created before `cube` 
was defined, and so don't contain a copy of this function. This
is one of the reasons why you should always define your functions
above the `if __name__ == "__main__"` block.

Alternatively, if you have to define the function in the 
`__main__` block, then ensure
that you create the pool after the definition. For example, one
fix here is to create a second pool for the second map, e.g.

```python
from multiprocessing import Pool

def square(x):
    """Return the square of the argument"""
    return x*x

if __name__ == "__main__":

    a = [1, 2, 3, 4, 5]

    pool = Pool()

    result = pool.map( square, a )

    print("Square result: %s" % result)

    def cube(x):
        """Return the cube of the argument"""
        return x*x*x

    pool2 = Pool()

    result = pool2.map( cube, a )

    print("Cube result: %s" % result)
```

Running this should print out

```
Square result: [1, 4, 9, 16, 25]
Cube result: [1, 8, 27, 64, 125]
```

## Pool Lifetime

The pool of workers is forked from your script when you create the 
`multiprocessing.Pool` object, and will have the same lifetime
as the containing object (e.g. `pool`). This means that it is good practice to delete this
object once you have finished with the pool, e.g. by setting the 
variable equal to `None` (e.g. by typing `pool = None`), such as here;

```python
from multiprocessing import Pool, current_process

def square(x):
    """Function to return the square of the argument"""
    print("Worker %s calculating square of %d" % \
             (current_process().pid, x))
    return x*x

if __name__ == "__main__":
    nprocs = 2

    # print the number of cores
    print("Number of workers equals %d" % nprocs)

    # create a pool of workers
    pool = Pool(processes=nprocs)

    # create an array of 10 integers, from 1 to 10
    a = range(1,11)

    result = pool.map( square, a )

    # delete the pool 
    pool = None

    total = reduce( lambda x,y: x+y, result )

    print("The sum of the square of the first 10 integers is %d" % total)
```

Alternatively, you can call `pool.close()` to close the pool.

Remembering to delete the pool object or calling `pool.close()`
can be a challenge, particularly when exceptions could be raised
by your mapping function. One
way to handle this automatically is to use Python's `with` statement.
For example;

```python
from multiprocessing import Pool
import contextlib

def square(x):
    """Return the square of the argument"""
    return x*x

if __name__ == "__main__":

    a = [1, 2, 3, 4, 5]

    with contextlib.closing( Pool() ) as pool:
        result = pool.map(square, a)

    print(result)
```

This `with` statement will assign the created `Pool()` object to the
variable `pool`. When the code in the `with` block exits (e.g.
because an exception is raised, or because all of the code in
the `with` block has been executed), it will
ensure that `pool.close()` is called. This is a safe way
to use a `multiprocessing.Pool`, ensuring that the pool is closed
properly after is has been used. It is also a safe way of using
multiple pools in a single script. You should use `with` for every
`map` you run, ensuring that you create a new pool each time, so
that you never risk having worker scripts having missing or different
functions to the master script. For example, the best way to write
the above multi-pool script is;

```python
from multiprocessing import Pool
import contextlib

def square(x):
    """Return the square of the argument"""
    return x*x

if __name__ == "__main__":

    a = [1, 2, 3, 4, 5]

    with contextlib.closing( Pool() ) as pool:
        result = pool.map( square, a )

    print("Square result: %s" % result)

    def cube(x):
        """Return the cube of the argument"""
        return x*x*x

    with contextlib.closing( Pool() ) as pool:
        result = pool.map( cube, a )

    print("Cube result: %s" % result)
```

***

# [Previous](multiprocessing.md) [Up](part2.md) [Next](mapreduce_part2.md)  
