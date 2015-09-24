#Map/Reduce

Map/reduce is a very powerful method of parallelising an algorithm. The idea is 
that you map the problem to be solved into a loop over a large number of iterations.
The iterations of the loop are then divided equally between a team of processes, 
with each process performing its allocation of iterations, and thus solving its 
own part of the problem, computing the result in process-local variables. Once 
all of the process's iterations are complete, all of the process-local computed 
variables are combined together (reduced) via `MPI_Reduce` to form the final global result.

We have now covered enough that we can use MPI to parallelise a map/reduce 
style calculation. In this case, the problem we will solve will be calculating 
the total interaction energy between each ion in an array of ions with a single 
reference ion. Passed into this function will be the reference ion, and an array 
of ions. The algorithm performed for each ion in the array will be;

* Calculate the distance between the ion in the array and the reference ion.
* Use this distance (r) to calculate the interaction energy ( 1 / r )
* Add this interaction energy onto the total sum.

Map/reduce can be used when you have an array of data, a function you wish to 
apply (to map) to each item in the array, and a single value you want back 
that is the reduction of the results of applying the function to each item in 
the array. In terms of map/reduce, our algorithm would look like this;

* Create a function that calculates and returns the interaction between a passed 
ion and the reference ion, e.g. `calc_energy(ion)`
* Map each ion in the array against the energy function `calc_energy`
* Reduce the result of each mapped function call using a sum (`MPI_SUM`)

Here are incomplete pieces of code that implement this algorithm (note that 
this is to provide an example of how map/reduce can be used - you don't 
need to complete this code);

* [C](mapreduce_c.md)
* [C++](mapreduce_cpp.md)
* [Fortran](mapreduce_f77.md)

Please look at, compile and try to run the code, using different numbers 
of processes in the MPI team.

Note that, in this example, the position of the reference ion and the 
positions of the array of ions must be shared amongst all processes. This 
could have been achieved by having the master process use `MPI_Send` to send the 
data individually to each worker process, and having each worker process use 
`MPI_Recv` to receive the data. While this is easy to program, matching 
`MPI_Send` / `MPI_Recv` pairs has a potential for programmer error. 
To simplify things, and to make the communication more efficient, MPI 
provides the function, [MPI_Bcast](http://www.mcs.anl.gov/research/projects/mpi/www/www3/MPI_Bcast.html). 
`MPI_Bcast` broadcasts a message from one process to all other processes 
in the team. Calling `MPI_Bcast` in the master process is equivalent to 
calling `MPI_Send` sequentially to all of the worker processes. Calling 
`MPI_Bcast` in a worker process is equivalent to calling `MPI_Recv` to 
receive a message from the master process.
 
Note that the amount of MPI in this examples is very low. Essentially, 
`MPI_Bcast` is used to map all of the data across all of the processes in 
the team at the start of the program, and then `MPI_Reduce` is used to reduce 
the computed result back to the master process at the end of the program. 
Ideally, such a simple, limited use of MPI should be the norm for MPI programs. 
Most of the work of parallelisation should be organising your code so that 
it can be parallelised. Once it has been organised, you then only need to 
add calls to a small number of MPI functions that share the data amongst 
the team, and then reduce the results back to the master.

***

[Compare with OpenMP](../beginning_openmp/mapreduce.md)

***

# [Previous](reduction.md) [Up](README.md) [Next](performance.md)
