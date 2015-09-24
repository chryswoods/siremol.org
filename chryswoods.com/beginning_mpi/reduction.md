#Reduction

Reduction, which is the process of combining (or reducing) the results of 
several sub-calculations into a single combined (reduced) result, is very 
common, and is the second half of the very powerful map-reduce form of parallel 
programming. In the exercise in the last section you used reduction to form the 
global sum of the total number of points inside and outside the circle, calculated 
as the sum of the number of points inside and outside the circle calculated by each 
process's iterations of the loop. While it may appear easy to write your own 
reduction code, using `MPI_Send` and `MPI_Recv`, it is actually very hard to 
write efficient reduction code. This is because reduction requires communication 
between all processes, where perhaps only one process at a time is allowed to 
update the sum on the master process. Reduction can actually be implemented 
much more efficiently, e.g. perhaps by dividing processes into pairs, and 
getting each pair to sum their results, and then dividing into pairs of pairs, 
and summing the pairs of pairs results, etc. (this method is known as binary 
tree reduction - [see here](http://blogs.rapidmind.com/2009/07/23/parallel-pattern-7-reduce/) 
for a more in-depth discussion of reduction algorithms).

So reduction is actually quite complicated to implement if you want it to be 
efficient and work well. Fortunately, you don't have to implement it, 
as MPI provides a [MPI_Reduce](http://www.mcs.anl.gov/research/projects/mpi/www/www3/MPI_Reduce.html) 
function which has a complete implementation for you! You can use MPI_Reduce 
by providing the input message, which is sent by each process and contains the 
set of data to be reduced, the output message, which will be sent to a 
specified process, and will contain the reduced output, and the operation, 
which refers to the numerical operation that must be applied to reduce the 
variables from each process together. The operators include;

* `MPI_SUM` - adds (sums) all of the variables together
* `MPI_PROD` - forms the product of all of the variables
* `MPI_MAX` - finds the maximum value from the variables
* `MPI_MIN` - finds the minimum value from the variables

A full list can be [found here](http://www.mpi-forum.org/docs/mpi-11-html/node78.html). 
Note that it is also possible for you to define your own functions that can be used 
to reduce variables together, via [MPI_Op_create](http://www.mpi-forum.org/docs/mpi-11-html/node80.html), 
although describing how that works is beyond this introductory course.

To make this clear, the following links provide the code for the fixed loop 
counting examples from the last page which use `MPI_Reduce` rather than 
`MPI_Send` / `MPI_Recv` pairs for summing up the number of iterations performed;

* [C](reduction_c.md)
* [C++](reduction_cpp.md)
* [Fortran](reduction_f77.md)

Note that `MPI_Reduce` will send the reduced result back to only the 
designated process (which should normally be your master process). If you 
want all of the processes to receive the reduced result, then you should 
call [MPI_Allreduce](http://www.mcs.anl.gov/research/projects/mpi/www/www3/MPI_Allreduce.html). 
[MPI_Allreduce] is equivalent to [MPI_Reduce], except that it sends the reduced 
result to every process in the MPI team.

***

##Exercise

Edit your program to estimate pi so that it uses reduction to form the sum of 
the number of points inside and outside the circle.

Here's the answers for checking (no peeking before you've finished!)

* [C](reduction_answer_c.md)
* [C++](reduction_answer_cpp.md)
* [Fortran](reduction_answer_f77.md)

***

[Compare with OpenMP](../beginning_openmp/reduction.md)

***

# [Previous](messages.md) [Up](README.md) [Next](mapreduce.md)

