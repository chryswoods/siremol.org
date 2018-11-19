# Part 2: Asynchronous Mapping

Asynchronous functions allow you to give different tasks to
different members of the `multiprocessing.Pool`. However, giving functions one
by one is not very efficient. It would be good to be able
to combine mapping with asynchronous functions, i.e. be able
to give different mapping tasks simultanously to the pool
of workers. Fortunately, `Pool.map_async` provides exactly that - 
an asynchronous parallel map.

Create a new python script called `asyncmap.py` and copy into it

```python
from functools import reduce
from multiprocessing import Pool, current_process
import time

def add(x, y):
    """Return the sum of the arguments"""
    print("Worker %s is processing add(%s, %s)" % (current_process().pid, x, y))
    time.sleep(1)
    return x + y

def product(x, y):
    """Return the product of the arguments"""
    print("Worker %s is processing product(%s, %s)" % (current_process().pid, x, y))
    time.sleep(1)
    return x * y

if __name__ == "__main__":

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    # Now create a Pool of workers
    with Pool() as pool:
        sum_future = pool.starmap_async(add, zip(a,b))
        product_future = pool.starmap_async(product, zip(a,b))

        sum_future.wait()
        product_future.wait()

    total_sum = reduce(lambda x, y: x + y, sum_future.get())
    total_product = reduce(lambda x, y: x + y, product_future.get())

    print("Sum of sums of 'a' and 'b' is %s" % total_sum)
    print("Sum of products of 'a' and 'b' is %s" % total_product)
```

Running this script, e.g. via `python asyncmap.py` should result
in something like

```
Worker 32722 is processing add(1, 11)
Worker 32723 is processing add(2, 12)
Worker 32724 is processing add(3, 13)
Worker 32725 is processing add(4, 14)
Worker 32722 is processing add(5, 15)
Worker 32724 is processing add(6, 16)
Worker 32725 is processing add(7, 17)
Worker 32723 is processing add(8, 18)
Worker 32722 is processing add(9, 19)
Worker 32724 is processing add(10, 20)
Worker 32725 is processing product(1, 11)
Worker 32723 is processing product(2, 12)
Worker 32722 is processing product(3, 13)
Worker 32723 is processing product(4, 14)
Worker 32724 is processing product(5, 15)
Worker 32725 is processing product(6, 16)
Worker 32722 is processing product(7, 17)
Worker 32725 is processing product(8, 18)
Worker 32723 is processing product(9, 19)
Worker 32724 is processing product(10, 20)
Sum of sums of 'a' and 'b' is 210
Sum of products of 'a' and 'b' is 935
```

This script provides two functions, `add` and `product`, which are
mapped asynchronously using the `Pool.map_async` function. This is
identical to the `Pool.map` function that you used before, except
now the map is performed asynchronously. This means that the
resulting list is returned in a future (in this case, the futures
`sum_future` and `product_future`. The results are waited for
using the `.wait()` functions, remembering to make sure that 
we don't exit the `with` block until all results are available.
Then, the results of mapping are retrieved using the
`.get()` function of the futures.

## Chunking

By default, the `Pool.map` function divides the work over the pool of workers
by assiging pieces of work one by one. In the example above, the work 
to be performed was;

```
add(1, 11)
add(2, 12)
add(3, 13)
etc.
add(10,20)
product(1, 11)
product(2, 12)
product(3, 13)
etc.
product(10, 20)
```

The work was assigned one by one to the four workers on my computer, 
i.e. the first worker process was
given `add(1, 11)`, the second `add(2, 12)`, the third `add(3, 13)`
the then the fourth `add(4, 14)`. The first worker to finish was then
given `add(5, 15)`, then the next given `add(6, 16)` etc. etc.

Giving work one by one can be very inefficient for quick tasks, as the
time needed by a worker process to stop and get new work can be longer
than it takes to actually complete the task. To solve this problem,
you can control how many work items are handed out to each worker
process at a time. This is known as chunking, and the number of work
items is known as the chunk of work to perform.

You can control the number of work items to perform per worker
(the chunk size) by setting the `chunksize` argument, e.g.

```python
sum_future = pool.starmap_async(add, zip(a, b), chunksize=5)
```

would suggest to `pool` that each worker be given a chunk of five pieces of work.
Note that this is just a suggestion, and `pool` may decide to use
a slightly smaller or larger chunk size depending on the amount of work
and the number of workers available.

Modify your `asyncmap.py` script and set the `chunksize`
to 5 for both of the asynchronous maps for `add` and 
`product`. Re-run your script. You 
should see something like;

```
Worker 658 is processing add(1, 11)
Worker 659 is processing add(6, 16)
Worker 660 is processing product(1, 11)
Worker 661 is processing product(6, 16)
Worker 659 is processing add(7, 17)
Worker 660 is processing product(2, 12)
Worker 661 is processing product(7, 17)
Worker 658 is processing add(2, 12)
Worker 660 is processing product(3, 13)
Worker 659 is processing add(8, 18)
Worker 661 is processing product(8, 18)
Worker 658 is processing add(3, 13)
Worker 660 is processing product(4, 14)
Worker 659 is processing add(9, 19)
Worker 661 is processing product(9, 19)
Worker 658 is processing add(4, 14)
Worker 659 is processing add(10, 20)
Worker 660 is processing product(5, 15)
Worker 661 is processing product(10, 20)
Worker 658 is processing add(5, 15)
Sum of sums of 'a' and 'b' is 210
Sum of products of 'a' and 'b' is 935
```

My laptop has four workers. The first worker is assigned the first
five items of work, i.e. `add(1, 11)` to `add(5, 15)`, and it starts
by running `add(1, 11)`, hence why `add(1, 11)` is printed first. 

The next worker is given the next five items
of work, i.e. `add(6, 16)` to `add(10,20)`, and starts by running
`add(6, 16)`, hence why `add(6, 16)` is printed second.

The next worker is given the next five items
of work, i.e. `product(1, 11)` to `product(5, 15)`, and it starts
by running `product(1, 11)`, hence why this is printed third.

The last worker is given the next five items of
work, i.e. `product(6, 16)` to `product(10, 20)`, and it starts
by running `product(6, 16)`, hence why this is printed fourth.

Once each worker has finished its first item of work, it moves
onto its second. This is why `add(2, 12)`, `add(7, 17)`, 
`product(2, 12)` and `product(7, 17)` are printed next. Then, 
each worker moves onto its third piece of work etc. etc.

If you don't specify the `chunksize` then it is equal to `1`. 
When writing a new script you should experiment with different
values of `chunksize` to find the value that gives best 
performance.

***

## Exercise

Edit your script written in answer to 
[exercise 2 of Parallel Map/Reduce](mapreduce_part2.md),
in which you count all of the words used in all
Shakespeare plays (e.g. an example answer 
[is here](mapreduce2_answer2.md)).

Edit the script so that you use an asynchronous map
to distribute the work over the pool. This will free
up the master process to give feedback to the user
of the script, e.g. to print a progress or status
message while the work is running to reassure
the user that the script has not frozen. For example

```python
while not future.ready():
    print("Work is in progress...")
    time.sleep(0.1)
```

Add a status message to your script to reassure the
user that your script hasn't frozen while it is processing.

(note that you can call your script using `python -u countwords.py shakespeare/*`
to use the `-u` argument to stop Python from buffering text written to standard output)

If you get stuck or want inspiration, a possible
answer is given [here](async_map_answer1.md).

***

# [Previous](futures_part2.md) [Up](part2.md) [Next](part3.md) 
