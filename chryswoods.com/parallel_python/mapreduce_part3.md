
# Part 3: Distributed map/reduce

Scoop supplies a `futures` module that provides complete support 
for parallel mapping, futures and asynchronous functions. To
use this module you must import it, e.g. via

```python
from scoop import futures
```

## scoop.futures.map

Create a new script called `mapreduce.py` and type into it

```python
from scoop import futures

def product(x, y):
    """Return the product of the arguments"""
    return x*y

def sum(x, y):
    """Return the sum of the arguments"""
    return x+y

if __name__ == "__main__":

    a = range(1,101)
    b = range(101, 201)

    results = futures.map(product, a, b)

    total = reduce(sum, results)

    print("Sum of the products equals %d" % total)
```

Run this script using the command

```
python -m scoop mapreduce.py
```

You need to use `-m scoop` so that Scoop has time to set up
the distributed cluster before running your script. When you
run your script you should see something similar to

```
[2015-11-29 11:03:38,600] launcher  INFO    SCOOP 0.7 1.1 on darwin using Python 2.7.10 (default, Aug 22 2015, 20:33:39) [GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.1)], API: 1013
[2015-11-29 11:03:38,600] launcher  INFO    Deploying 4 worker(s) over 1 host(s).
[2015-11-29 11:03:38,601] launcher  INFO    Worker distribution: 
[2015-11-29 11:03:38,601] launcher  INFO       127.0.0.1:	3 + origin
Sum of the products equals 20100
[2015-11-29 11:03:39,375] launcher  (127.0.0.1:50551) INFO    Root process is done.
[2015-11-29 11:03:39,375] launcher  (127.0.0.1:50551) INFO    Finished cleaning spawned subprocesses.
```

(the exact output will depend on your computer and your version of Scoop)

By default Scoop will run on your local computer, starting one process
for every available processor core. In my case, I have four workers.

Scoop provides a very similar interface as `multiprocessing`, with the same caveats,
requirements and restrictions. For example

* You must ensure that all use of Scoop is protected within an `if __name__ == "__main__"`
block.

* You must import all modules and declare all functions at the top of your script,
before the `if __name__ == "__main__"` block.

* Scoop does not yet support anonymous (lambda) functions, again because of
Python's poor support for pickling those functions. Hopefully this will change soon.

In the above script we used the Scoop `futures.map` function. 
This is the Scoop mapping function, that is identical to the 
standard Python `map`, except that the map is performed in parallel across the 
distributed cluster. Note that Scoop's map supports passing multiple arguments
to the mapping function.

## scoop.futures.mapReduce

Performance of distributed parallel scripts is strongly related to the speed of the
network and amount of communication between nodes. In the above example, we used
`scoop.futures.map` to map the `sum` function. All of the results were then
transmitted back to the master process to complete the reduction (sum). This
is inefficient, as it means that a lot of data needs to be transmitted back to 
the master. A better approach is to allow all of the workers in the cluster to
perform the reduction as a group, thereby minimising communication.

This can be achieved by using the `scoop.futures.mapReduce` function. This
combines the map and reduce into a single function call. The function call
looks like this;

```python
result = scoop.futures.mapReduce( mapping_func, reduction_func, args... )
```

where `mapping_func` is the function used for mapping, `reduction_func`
is the function used for the reduction, `args` are the set of arguments
that are passed to `mapping_func` and `result` is the returned result.

Edit your `mapreduce.py` script so that it uses the `scoop.futures.mapReduce`
function e.g.

```python
from scoop import futures

def product(x, y):
    """Return the product of the arguments"""
    return x*y

def sum(x, y):
    """Return the sum of the arguments"""
    return x+y

if __name__ == "__main__":

    a = range(1,101)
    b = range(101, 201)

    total = futures.mapReduce(product, sum, a, b)

    print("Sum of the products equals %d" % total)
```

Run the script using `python -m scoop mapreduce.py`, and you should 
see a similar result as before.

***

## Exercise

Edit your script written in answer to 
[exercise 2 of Parallel Map/Reduce](mapreduce_part2.md),
in which you count all of the words used in all
Shakespeare plays (e.g. an example answer 
[is here](mapreduce2_answer2.md)).

Edit the script so that it uses `scoop.futures.mapReduce`
to perform the work. Note that `scoop.futures.mapReduce`
is not asynchronous, so you cannot (yet) add a status
message to your script while it is processing.

If you get stuck or want inspiration, a possible
answer is given [here](mapreduce3_answer1.md).

***

# [Previous](scoop.md) [Up](part3.md) [Next](cluster.md) 
