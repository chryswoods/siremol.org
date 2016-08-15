# Part 1: Functional Programming

To understand how best to write efficient parallel programs in modern C++,
we first need to gain an understanding of "Functional Programming".
This is a style of programming in which functions are treated and
manipulated as objects, i.e. functions can be assigned to variables,
they can be passed as arguments, and they can be stored in containers
along with other data.

Using the idea of functional programming, we can write parallel code
that works by running lots of functions in parallel on large amounts
of data. Your job, as a parallel functional programmer, is to design
these functions. You then connect them together, with their dependencies,
to create a team that can be distributed across the cores
of a processor.

Functional programming is not the only way of writing an efficient
parallel program. Other examples are shared memory parallelism
(e.g. check out my [OpenMP course](../beginning_openmp/README.md)) or
message passing (e.g. check out my [MPI course](../beginning_mpi/README.md)).
However, functional programming is, in my opinion, the easiest and most efficient
way of extracting good performance from a parallel C++ program
when you have a large number of available cores (e.g. >8).

Functional programming is useful also in its own right, and adopting
it as a programming style can improve the readability and efficiency
of even single-threaded C++ code. It can make your intention as 
a programmer clearer to other developers, it can limit the amount
of code duplication or retyping, and can also reduce the number of
lines of code needed to represent your algorithm.

 * [Functions as Objects](functions.md)
 * [Mapping Functions](map.md)
 * [Reduction](reduce.md)
 * [Anonymous Functions (lambda)](lambda.md)
 * [Map/Reduce](mapreduce.md)

***

# [Previous](README.md) [Up](README.md) [Next](functions.md)
