#Loops

OpenMP sections provide a method by which you can assign different functions 
to be run by different threads. While this is easy to do, it does not scale well. 
You can only run as many threads in parallel as there are different functions 
to be run. If you have more threads than functions, then the extra threads 
will be idle. Also, if different functions take different amounts of time, 
then some threads may finish earlier than other threads, and they will be left 
idle waiting for the remaining threads to finish.

One way of achieving better performance is to use OpenMP to parallelise loops 
within your code. Lets imagine you have a loop that requires 1000 iterations. 
If you have two threads in the OpenMP team, then it would make sense for one thread 
to perform 500 of the 1000 iterations while the other thread performs the 
other 500 of 1000 iterations. This will scale as as more threads are added, 
the iterations of the loop can be shared evenly between them, e.g.

* 2 threads : 500 iterations each
* 4 threads : 250 iterations each
* 100 threads : 10 iterations each
* 1000 threads : 1 iteration each

Of course, this only scales up to the number of iterations in the loop, e.g. 
if there are 1500 threads, then 1000 threads will have 1 iteration each, 
while 500 threads will sit idle.

Also, and this is quite important, this will only work if each iteration of 
the loop is independent. This means that it should be possible to run each 
iteration in the loop in any order, and that each iteration does not affect 
any other iteration. This is necessary as running loop iterations in 
parallel means that we cannot guarantee that loop iteration 99 will be 
performed before loop iteration 100.

To see how to run an OpenMP parallel loop, copy out the appropriate code 
from the links below to create the executable loops;

* [C](loops_c.md)
* [C++](loops_cpp.md)
* [Fortran](loops_f77.md)

Again, run this executable with different values of `OMP_NUM_THREADS` to 
get an idea of how it performs.

***

[Compare with MPI](../beginning_mpi/loops.md)

***

# [Previous](sections.md) [Up](README.md) [Next](critical.md) 
