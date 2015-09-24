#Performance

Done right, MPI is reasonably straightforward to use, and can be added to 
existing programs. However, don't let this simplicity deceive you. While 
writing MPI code can be straightforward, writing efficient, scalable MPI code 
that doesn't become a spaghetti mess of mismatched messages can be hard, 
and requires you to think deeply about the problem to be solved. As you saw 
in the map/reduce example, in a cleanly structured parallel algorithm the 
amount of MPI was quite small. However, the application itself had to be 
arranged in a way that allowed the problem to be solved using a map/reduce approach.

While the techniques used to get good performance using MPI are problem specific, 
there are a set of general guidelines that will put you on the right track;

* Avoid sending messages whenever possible (which means work as much as possible using 
variables already present in the process. Only update variables using 
`MPI_Bcast` or `MPI_Reduce` when you have to).
* Try to do as much work as you can using process-local variables. Structure your 
program so that each process can calculate a process-local result, and then these 
process-local results can then be combined (reduced) together at the end into the final answer.
* Avoid `MPI_Send` and `MPI_Recv` wherever possible. These are point-to-point 
communication operations, which can involve only two processes at a time. Whenever 
possible, try to broadcast data, or scatter data (using [MPI_Scatter](http://www.mcs.anl.gov/research/projects/mpi/www/www3/MPI_Scatter.html) - 
not covered here in this basic course) to the processes, and collect the 
results using `MPI_Reduce`.
* If possible, try to group communication together as much as possible, e.g. instead of 
broadcasting five integers separately using five calls to `MPI_Bcast`, copy 
the integers into an array, and then broadcast the array in a single call.

Prefer to use high-level MPI functions, such as `MPI_Bcast`, `MPI_Reduce` 
and `MPI_Scatter`, rather than trying to write your own using `MPI_Send` and `MPI_Recv`. 
While writing your own can be fun, it will be difficult to make them efficient, 
and you are more likely to introduce difficult-to-find bugs.

However, the most important advice is benchmark, benchmark, benchmark! Don't try 
and guess the performance of your code, or guess that something makes it faster. 
Actually time how fast your code runs (e.g. using the time command or using 
timers within your code), and compare timings for different numbers of processes 
(e.g. by running with different numbers of `N` in `mpirun -np N`) every time you 
make changes to your code. Make benchmarking and performance testing as important 
in your coding workflow as debugging and unit testing.

***

[Compare with OpenMP](../beginning_openmp/performance.md)

***

# [Previous](mapreduce.md) [Up](README.md) [Next](whatnext.md)

