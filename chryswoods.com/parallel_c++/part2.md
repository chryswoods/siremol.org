# Part 2: Parallel Programming using Intel Threaded Building Blocks

You have now learned how to use functional programming to write
modern C++ programs that are composed of a set of functions that
can be mapped
against or used to reduce vectors of data. You may be wondering
now how this has helped us write efficient parallel C++ code?

To write efficient parallel C++ code you need to think of your algorithm
at a high level, i.e. in terms of mapping or reduction. Such 
higher-level abstractions are inherently easily parallelisable, 
and can be parallelised efficiently across large numbers of cores
of many-core and massively many-core processors (e.g. modern Xeon
or Xeon Phi processors). By structuring your program into algorithms
at this high level, you then make it easier to add efficient parallelism.

One tool to add parallelism is Intel's Threaded Building Blocks (TBB).
There are other tools available. However, TBB is a good choice,
as it implements an efficient task-based scheduler that supports
multi-level parallelism. While it has been written by Intel, TBB is
inherently portable and is a free, and excellent choice for adding
parallelisation to your C++ code.

In this part of the course you will learn the basics of Intel's TBB.
You will then see how TBB can be used to parallelise our `map` and
`reduce` functions, to create a very efficient and highly
scalable parallel `map/reduce`. We will then look at the underlying
technology of TBB, i.e. tasks, and the TBB task scheduler.

* [tbb::parallel_for](parallel_for.md)
* [Parallel map](parallel_map.md)
* [tbb::parallel_reduce](parallel_reduce.md)
* [Parallel map/reduce](mapreduce.md)
* [tbb::task](task.md)
* [Task Scheduler](scheduler.md)

***

# [Previous](lambda.md) [Up](README.md) [Next](parallel_for.md)


 
