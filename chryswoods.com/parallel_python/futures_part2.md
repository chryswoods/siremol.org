# Part 2: Asynchronous Functions and Futures

The `Pool.map` function allows you to map a single function across
an entire list of data. But what if you want to apply lots of different
functions? The solution is to tell individual workers to run different
functions, by applying functions to workers.

The `Pool` class comes with the function `apply`. This is used to
tell one process in the worker pool to run a specified function. For example,
create a new script called `poolapply.py` and type into it;

```python
from multiprocessing import Pool, current_process
import contextlib 
import time

def slow_function( nsecs ):
    """Function that sleeps for 'nsecs' seconds, returning
       the number of seconds that it slept"""

    print("Process %s going to sleep for %d second(s)" \
              % (current_process().pid,nsecs))

    # use the time.sleep function to sleep for nsecs seconds
    time.sleep(nsecs)

    print("Process %s waking up" % current_process().pid)

    return nsecs

if __name__ == "__main__":
    print("Master process is PID %d" % current_process().pid)

    with contextlib.closing( Pool() ) as pool:
        r = pool.apply( slow_function, [5] )

    print("Result is %s" % r)
```

Run this script using `python poolapply.py`. You should see the 
something like this printed to the screen

```
Master process is PID 8691
Process 8692 going to sleep for 5 second(s)
Process 8692 waking up
Result is 5
```

(with a delay of five seconds when the worker process sleeps)

The key line in this script is

```python
r = pool.apply( slow_function, [5] )
```

The `pool.apply` function will request that one of the workers
in the pool should run the passed function (in this case 
`slow_function`), with the arguments passed to the function
held in the list (in this case `[5]`). The `pool.apply` function
will wait until the passed function has finished, and will return
the result of that function (here copied into `r`).

The arguments to the applied function must be placed into
a list. This is the case, even if the applied function has
just a single argument (i.e. this is why we had to write
`[5]` rather than just `5`. The list of arguments must contain
the same number of arguments as needed by the applied function,
in the same order as declared in the function. For example,
edit your `poolapply.py` function to read;

```python
from multiprocessing import Pool, current_process
import contextlib
import time

def slow_sum( nsecs, x, y ):
    """Function that sleeps for 'nsecs' seconds, and
       then returns the sum of x and y"""
    print("Process %s going to sleep for %d second(s)" \
              % (current_process().pid,nsecs))

    time.sleep(nsecs)

    print("Process %s waking up" % current_process().pid)

    return x+y

if __name__ == "__main__":
    print("Master process is PID %d" % current_process().pid)

    with contextlib.closing( Pool() ) as pool:
        r = pool.apply( slow_sum, [1,6,7] )

    print("Result is %s" % r)
```

Here we have edited `slow_function` to `slow_sum`, with this function 
accepting three arguments. These three arguments are passed using the list
in `pool.apply( slow_sum, [1,6,7] )`.

Running this script using `python poolapply.py` should give output similar to

```
Master process is PID 8893
Process 8895 going to sleep for 1 second(s)
Process 8895 waking up
Result is 13
```

## Asynchronous Functions

A major problem of `Pool.apply` is that the master process is blocked until
the worker has finished processing the applied function. This is obviously
an issue if you want to run multiple applied functions in parallel!

Fortunately, `Pool` has an `apply_async` function. This is an asynchronous
version of `apply` that applies the function in a worker process, but
without blocking the master. Create a new python script called `applyasync.py`
and copy into it;

```python
from multiprocessing import Pool, current_process
import contextlib
import time

def slow_sum( nsecs, x, y ):
    """Function that sleeps for 'nsecs' seconds, and
       then returns the sum of x and y"""
    print("Process %s going to sleep for %d second(s)" \
              % (current_process().pid,nsecs))

    time.sleep(nsecs)

    print("Process %s waking up" % current_process().pid)

    return x+y

if __name__ == "__main__":
    print("Master process is PID %d" % current_process().pid)

    with contextlib.closing( Pool() ) as pool:
        r1 = pool.apply_async( slow_sum, [1,6,7] )
        r2 = pool.apply_async( slow_sum, [1,2,3] )

        r1.wait()
        print("Result one is %s" % r1.get())

        r2.wait()
        print("Result two is %s" % r2.get())
```

Run this script using `python applyasync.py` and you should see results
similar to

```
Master process is PID 8717
Process 8719 going to sleep for 1 second(s)
Process 8720 going to sleep for 1 second(s)
Process 8719 waking up
Process 8720 waking up
Result one is 13
Result two is 5
```

The keys lines of this script are

```
r1 = pool.apply_async( slow_sum, [1,6,7] )
r2 = pool.apply_async( slow_sum, [1,2,3] )
```

The `apply_async` function is identical to `apply`, except that it returns
control to the master process immediately. This means that the master process
is free to continue working (e.g. here, it `apply_async`s a second `slow_sum`
function). In this case, it allows us to run two `slow_sums` in parallel.

## Futures

An issue with running a function asynchronously is that the return
value of the function is not available immediately. This means that, 
when running an asynchronous function, you don't get the return value
directly. Instead, `apply_async` returns a placeholder for the return
value. This placeholder is called a "future", and is a variable that
in the future will be given the result of the function.

Futures are a very common variable type in parallel programming across
many languages. Futures provide several common functions;

* Block (wait) until the result is available. In `multiprocessing`, this is 
via the `.wait()` function, e.g. `r1.wait()` in the above script.

* Retrieve the result when it is available (blocking until it is 
  available). This is the `.get()` function, e.g. `r1.get()`.

* Test whether or not the result is available. This is the `.ready()`
  function, which returns `True` when the asynchronous function has
  finished and the result is available via `.get()`.

* Test whether or not the function was a success, e.g. whether or
  not an exception was raised when running the function. This is
  the `.successful()` function, which returns `True` if the
  asynchronous function completed without raising an exception. 
  Note that this function should only be called after
  the result is available (e.g. when `.ready()` returns `True`).

In the above example, `r1` and `r2` were both futures for the results
of the two asynchronous calls of `slow_sum`. The two `slow_sum` calls
were processed by two worker processes. The master process was then
blocked using `r1.wait()` to wait for the result of the first call,
and then blocked using `r2.wait()` to wait or the result of the
second call.

(note that we had to wait for all of the results to be delivered to
our futures before we exited the `with` block, or else the pool of
workers could be destroyed before the functions have completed and
the results are available)

We can explore this more using the following example. Create
a script called `future.py` and copy into it;

```python
from multiprocessing import Pool
import contextlib
import time

def slow_sum( nsecs, x, y ):
    """Function that sleeps for 'nsecs' seconds, and
       then returns the sum of x and y"""
    time.sleep(nsecs)
    return x+y

def slow_diff( nsecs, x, y ):
    """Function that sleeps for 'nsecs' seconds, and
       then retruns the difference of x and y"""
    time.sleep(nsecs)
    return x-y

def broken_function( nsecs ):
    """Function that deliberately raises an AssertationError"""
    time.sleep(nsecs)
    raise ValueError("Called broken function")

if __name__ == "__main__":
    futures = []

    with contextlib.closing( Pool() ) as pool:
        futures.append( pool.apply_async( slow_sum, [3,6,7] ) )
        futures.append( pool.apply_async( slow_diff, [2,5,2] ) )
        futures.append( pool.apply_async( slow_sum, [1,8,1] ) )
        futures.append( pool.apply_async( slow_diff, [5,9,2] ) )
        futures.append( pool.apply_async( broken_function, [4] ) )

        while True:
            all_finished = True

            print("\nHave the workers finished?")

            for i in range(0,len(futures)):
                if futures[i].ready():
                    print("Process %d has finished" % i)
                else:
                    all_finished = False
                    print("Process %d is running..." % i)

            if all_finished:
                break

            time.sleep(1)

        print("\nHere are the results.")

        for i in range(0,len(futures)):
            if futures[i].successful():
                print("Process %d was successful. Result is %s" \
                   % (i, futures[i].get()))
            else:
                print("Process %d failed!" % i)

                try:
                    futures[i].get()
                except Exception as e:
                    print("Error = %s : %s" % (type(e), e))
```

Running this script using `python future.py` should give results
similar to

```
Have the workers finished?
Process 0 is running...
Process 1 is running...
Process 2 is running...
Process 3 is running...
Process 4 is running...

Have the workers finished?
Process 0 is running...
Process 1 is running...
Process 2 is running...
Process 3 is running...
Process 4 is running...

Have the workers finished?
Process 0 is running...
Process 1 has finished
Process 2 has finished
Process 3 is running...
Process 4 is running...

Have the workers finished?
Process 0 has finished
Process 1 has finished
Process 2 has finished
Process 3 is running...
Process 4 is running...

Have the workers finished?
Process 0 has finished
Process 1 has finished
Process 2 has finished
Process 3 is running...
Process 4 is running...

Have the workers finished?
Process 0 has finished
Process 1 has finished
Process 2 has finished
Process 3 has finished
Process 4 has finished

Here are the results.
Process 0 was successful. Result is 13
Process 1 was successful. Result is 3
Process 2 was successful. Result is 9
Process 3 was successful. Result is 7
Process 4 failed!
Error = <type 'exceptions.ValueError'> : Called broken function
```

Is this output that you expected? Note that the exception raised
by `broken_function` is held safely in its associated future.
This is indicated by `.successful()` returning `False`, thereby
allowing us to handle the exception in a `try...except` block
that is put around the `.get()` function (if you `.get()` 
a future that contains an exception, then that exception
is raised).

***

## Exercise

Edit the `future.py` script so that you can control the number of 
workers in the pool using a command line argument (e.g. using
`Pool(processes=int(sys.argv[1]))` rather than `Pool()`).

Edit the script to add calls to more asynchronous functions. 

Then experiment with running the script with different numbers of
processes in the pool and with different numbers of asynchronous
function calls.

How are the asynchronous function calls distributed across the
pool of worker processes?

***

# [Previous](mapreduce_part2.md) [Up](part2.md) [Next](queue.md) 
