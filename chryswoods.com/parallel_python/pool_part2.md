
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

***

# [Previous](multiprocessing.md) [Up](part2.md) [Next](mapreduce_part2.md)  
