
# Parallel Programming with Python

Welcome to a short course that will teach you how to write Python scripts
that can take advantage of the processing power of multicore processors
and large compute clusters. While this course is based on Python, the
core ideas of functional programming and parallel functional programming
are applicable to a wide range of languages.

To follow this course you should already have a good basic understanding
of Python, e.g. loops, functions, containers and classes. This course
will rely on you understanding the material presented in 
my [Beginning Python](../beginning_python/README.md) and 
[Intermediate Python](../intermediate_python/README.md) courses.

This is a short course that will give you a taste of functional programming
and how it can be used to write efficient parallel code. Please work
through the course at your own pace. Python is best learned by
using it, so please copy out and play with the examples provided,
and also have a go at the exercises.

NOTE - this course will present parallel python as implemented
in Python 2. There are some small differences between Python 2 and 3
for parallel Python that are [described here](python2to3.md). 
Presenting these differences during the course itself would be distracting. Please
use a Python 2 interpreter to complete this course, and then, 
if you are interested,
take a look at the [list of small changes in Python 3](python2to3.md) to 
see how things have changed (and got a little more complex).

***

* [Part 1: Functional Programming](part1.md)
    * [Functions as Objects](functions.md)
    * [Mapping Functions](map.md)
    * [Reduction](reduce.md)
    * [Anonymous Functions (lambda)](lambda.md)
* [Part 2: Multicore (local) Parallel Programming](part2.md)
    * [Multiprocessing](multiprocessing.md)
    * [Pool](pool_part2.md)
    * [Parallel map/reduce](mapreduce_part2.md)
    * [Asynchronous Functions and Futures](futures_part2.md)
    * [Asynchronous Mapping](async_map.md)
* [Part 3: Multinode (distributed/cluster) Parallel Programming](part3.md)
    * [Scoop](scoop.md)
    * [Distributed map/reduce](mapreduce_part3.md)
    * [Running Scoop on a Cluster](cluster.md)
    * [What Next?](whatnext.md)
* [Epilogue](epilogue.md)
    * [Changes from Python 2 to 3](python2to3.md)
    * [Global Interpreter Lock (GIL)](gil.md)

***

# [Previous](../main/courses.md) [Up](../main/courses.md) [Next](part1.md)  
