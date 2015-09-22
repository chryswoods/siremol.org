# Performance

OpenMP is reasonably straightforward to use, and can be added to existing programs. 
However, don't let this simplicity deceive you. While writing OpenMP code is 
straightforward, writing efficient, scalable OpenMP code can be hard, and requires 
you to think deeply about the problem to be solved. As you saw in the map/reduce example, 
the amount of OpenMP was quite small, but the application itself had to be arranged 
in a way that allowed the problem to be solved using a map/reduce approach.

While the techniques used to get good performance using OpenMP are problem specific, 
there are a set of general guidelines that will put you on the right track;

* Avoid working with global variables whenever possible (which in Fortran means 
avoid common blocks!).
* Try to do as much work as you can using thread-private variables. Structure 
your program so that each thread can calculate a thread-local result, and then 
these thread-local results can then be combined together at the end into the final answer.
* Avoid OpenMP critical regions wherever possible. These will cause threads to 
block as only one thread can be in a critical region at a time. However, 
remember that critical regions are necessary whenever you update a global variable.
* Try to leave all global updates to the end of the parallel region.
* Prefer to use OpenMP reduction operations rather than trying to write your own.

However, the most important advice is benchmark, benchmark, benchmark! 
Don't try and guess the performance of your code, or guess that something 
makes it faster. Actually time how fast your code runs (e.g. using the 
time command or using timers within your code), and compare timings for 
different numbers of threads (by changing `OMP_NUM_THREADS`) every time you
make changes to your code. Make benchmarking and performance testing as 
important in your coding workflow as debugging and unit testing.

***

[Compare with MPI](../beginning_mpi/performance.md)

***

# [Previous](mapreduce.md) [Up](README.md) [Next](casestudy.md) 
