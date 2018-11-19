
# Part 2: Pool

One of the core multiprocessing features is `multiprocessing.Pool`. This
provides a pool of workers that can be used to parallelise a map.

For example, create a new script called `pool.py` and type into it;

```python
from functools import reduce
from multiprocessing import Pool, cpu_count

def square(x):
    """Function to return the square of the argument"""
    return x*x

if __name__ == "__main__":
    # print the number of cores
    print("Number of cores available equals %d" % cpu_count())

    # create a pool of workers
    with Pool() as pool:
        # create an array of 5000 integers, from 1 to 5000
        r = range(1, 5001)

        result = pool.map(square, r)


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
with Pool() as pool:
```

has created a pool of worker copies of your script, with the number of workers
equalling the number of cores reported by `cpu_count()`. You can control the
number of copies by specifying the value of `processes` in the constructor for `Pool`, e.g.

```python
with Pool(processes=5) as pool:
```

would create a pool of five workers.

The line

```python
r = range(1,5001)
```

is a quick way to create a list of 5000 integers, from 1 to 5000. The parallel
work is conducted on the line

```python
result = pool.map(square, r)
```

This performs a map of the function `square` over the list of items of `r`.
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
from functools import reduce
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
    with Pool(processes=nprocs) as pool:
        # create an array of 5000 integers, from 1 to 5000
        r = range(1, 21)

        result = pool.map(square, r)


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
Worker 25043 calculating square of 1
Worker 25043 calculating square of 2
Worker 25043 calculating square of 3
Worker 25044 calculating square of 4
Worker 25044 calculating square of 5
Worker 25044 calculating square of 6
Worker 25043 calculating square of 7
Worker 25043 calculating square of 8
Worker 25043 calculating square of 9
Worker 25044 calculating square of 10
Worker 25043 calculating square of 13
Worker 25044 calculating square of 11
Worker 25043 calculating square of 14
Worker 25044 calculating square of 12
Worker 25043 calculating square of 15
Worker 25043 calculating square of 16
Worker 25043 calculating square of 17
Worker 25043 calculating square of 18
Worker 25044 calculating square of 19
Worker 25044 calculating square of 20
The sum of the square of the first 5000 integers is 2870
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

    r = [1, 2, 3, 4, 5]

    with Pool() as pool:
        result = pool.map(square, r)

        print("Square result: %s" % result)

        def cube(x):
            """Return the cube of the argument"""
            return x * x * x

        result = pool.map(cube, r)

        print("Cube result: %s" % result)

```

If you run this script you should see an error such as

```
AttributeError: Can't get attribute 'cube' on <module '__main__' from 'pool.py'>
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

    r = [1, 2, 3, 4, 5]

    with Pool() as pool:
        result = pool.map(square, r)

        print("Square result: %s" % result)

    def cube(x):
        """Return the cube of the argument"""
        return x * x * x

    with Pool() as pool:
        result = pool.map(cube, r)

        print("Cube result: %s" % result)
```

Running this should print out

```
Square result: [1, 4, 9, 16, 25]
Cube result: [1, 8, 27, 64, 125]
```

***

# [Previous](multiprocessing.md) [Up](part2.md) [Next](mapreduce_part2.md)  
