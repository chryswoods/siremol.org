#Reduction

Reduction, which is the process of combining (or reducing) the results of 
several sub-calculations into a single combined (reduced) result, is very 
common, and is the second half of the very powerful map-reduce form of 
parallel programming. In the exercise in the last section you used reduction 
to form the global sum of the total number of points inside and outside the circle, 
calculated as the sum of the number of points inside and outside the circle 
calculated by each thread's iterations of the loop. While it may appear easy to
write your own reduction code, it is actually very hard to write efficient 
reduction code. This is because reduction requires the use of a critical section, 
where only one thread is allowed to update the global sum at a time. Reduction 
can actually be implemented much more efficiently, e.g. perhaps by dividing 
threads into pairs, and getting each pair to sum their results, and then dividing 
into pairs of pairs, and summing the pairs of pairs results, etc. (this method 
is known as binary tree reduction - [see here](http://blogs.rapidmind.com/2009/07/23/parallel-pattern-7-reduce/) 
for a more in-depth discussion of reduction algorithms).

So reduction is actually quite complicated to implement if you want it to be 
efficient and work well. Fortunately, you don't have to implement it, 
as OpenMP provides a reduction directive which has implemented it for you! 
The reduction directive is added to the end of the OpenMP parallel directive 
and has the following form;

    reduction( operator : variable list )

where `operator` can be any binary operator (e.g. `+`, `-`, `*`), and `variable list` 
is a single variable or list of variables that will be used for the reduction, e.g.

    reduction( + : sum )

will tell the compiler that `sum` will hold the global result of a reduction 
which will be formed by adding together the results of thread-private calculations, while,

    reduction( - : balance, diff )

will tell the compiler that both `balance` and `diff` will hold the global results 
of reductions which are formed by subtracting the results of thread-private calculations.

To make this clear, the following links provide the code for the fixed loop counting 
examples from the last section which use reduction rather than thread-private 
variables with an OpenMP critical section;

* [C](reduction_c.md)
* [C++](reduction_cpp.md)
* [Fortran](reduction_f77.md)

***

##Exercise

Edit your program to estimate pi so that it uses reduction to form the sum of the 
number of points inside and outside the circle.

Here's the answers for checking (no peeking before you've finished!)

* [C](reduction_answer_c.md)
* [C++](reduction_answer_cpp.md)
* [Fortran](reduction_answer_f77.md)

***

[Compare with MPI](../beginning_mpi/reduction.md)

***

# [Previous](critical.md) [Up](README.md) [Next](mapreduce.md) 
