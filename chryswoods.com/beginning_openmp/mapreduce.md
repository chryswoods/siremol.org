#Map/Reduce

We have now covered enough that we can use OpenMP to parallelise a map/reduce style 
calculation. In this case, the problem we will solve will be calculating the 
total interaction energy between each ion in an array of ions with a single 
reference ion. Passed into this function will be the reference ion, and an 
array of ions. The algorithm performed for each ion in the array will be;

* Calculate the distance between the ion in the array and the reference ion.
* Use this distance (r) to calculate the interaction energy ( 1 / r )
* Add this interaction energy onto the total sum.
* Map/reduce can be used when you have an array of data, a function you wish to apply (to map) to each item in the array, and a single value you want back that is the reduction of the results of applying the function to each item in the array. 

In terms of map/reduce, our algorithm would look like this;

* Create a function that calculates and returns the interaction between a passed ion and the reference ion, e.g. `calc_energy(ion)`
* Map each ion in the array against the energy function `calc_energy`
* Reduce the result of each mapped function call using a `sum (+)`

Here are incomplete pieces of code that implement this algorithm (note that this is to provide an example of how map/reduce 
can be used - you don't need to complete this code);

* [C](mapreduce_c.md)
* [C++](mapreduce_cpp.md)
* [Fortran](mapreduce_f77.md)

Note that the amount of OpenMP in these examples is very low (just 2-3 lines). 
This is quite common for OpenMP programs - most of the work of parallelisation 
is organising your code so that it can be parallelised. Once it has been 
organised, you then only need to add a small number of OpenMP directives.

Compile the above programs, and try running them using different numbers of threads.

***

[Compare with MPI](../beginning_mpi/mapreduce.md)

***

# [Previous](reduction.md) [Up](README.md) [Next](performance.md) 
