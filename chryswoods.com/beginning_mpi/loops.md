#Loops

MPI makes it easy to start a team of processes where different functions are run 
by different processes. While this is easy to do, it does not scale well. You 
can only run as many processes in parallel as there are different functions 
to be run. If you have more processes than functions, then the extra processes
will be idle. Also, if different functions take different amounts of time, then 
some processes may finish earlier than other processes, and they will be left 
idle waiting for the remaining processes to finish.

One way of achieving better performance is to use MPI to parallelise loops 
within your code. Lets imagine you have a loop that requires 1000 iterations. 
If you have two processes in the MPI team, then it would make sense for one 
process to perform 500 of the 1000 iterations while the other process performs 
the other 500 of 1000 iterations. This will scale as as more processes are added, 
the iterations of the loop can be shared evenly between them, e.g.

* 2 processes : 500 iterations each
* 4 processes : 250 iterations each
* 100 processes : 10 iterations each
* 1000 processes : 1 iteration each

Of course, this only scales up to the number of iterations in the loop, e.g. if 
there are 1500 processes, then 1000 processes will have 1 iteration each, 
while 500 processes will sit idle.

Also, and this is quite important, this will only work if each iteration of 
the loop is independent. This means that it should be possible to run each 
iteration in the loop in any order, and that each iteration does not affect any 
other iteration. This is necessary as running loop iterations in parallel means 
that we cannot guarantee that loop iteration 99 will be performed before loop iteration 100.

To see how to use MPI to parallelise a loop, copy out the appropriate code from the 
links below to create the executable loops;

* [C](loops_c.md)
* [C++](loops_cpp.md)
* [Fortran](loops_f77.md)

Again, run this executable with different numbers of processes (`mpirun -np X`) 
to get an idea of how it performs.

Key to this example, is that each process must know how many processes are in the 
team. A process finds out how many processes are running in the team using the 
function `MPI_Comm_size`. If a loop requires 100 iterations, and there are 
4 processes in the team, then the process with rank 0 should run the first 
25 iterations, the process with rank 1 should run the next 25 iterations, 
the process with rank 2 should run the third set of 25 iterations, 
while the process with rank 3 should run the last 25 iterations. 
It is up to you to work out the range of iterations to run in a process 
based on its rank, and based on the number of processes in the team.

***

[Compare with OpenMP](../beginning_openmp/loops.md)

***

# [Previous](sections.md) [Up](README.md) [Next](messages.md)
