#Sections

The OpenMP `sections` directive provides a means by which different 
threads can run different parts of the program in parallel. Copy 
the code from the appropriate link below to create the executable `omp_sections`.

* [C](sections_c.md)
* [C++](sections_cpp.md)
* [Fortran](sections_f77.md)

Try running the executable `omp_sections` using different values of `OMP_NUM_THREADS`.

In this example, there are three functions, `times_table`, `countdown` and 
`long_loop`. These three functions are called from within an OpenMP sections 
directive, where each function is placed into a separate OpenMP section. 
This tells the compiler that these three functions can be called in parallel, 
and a thread from the team can be assigned to each section. Note that if 
there are more sections than threads, then each section is queued until a 
thread is available to run it, while if there are more threads than sections, 
then the extra threads will have nothing to do. Note that there is no 
guarantee as to the order in which sections are executed.

***

[Compare with MPI](../beginning_mpi/sections.md)

***

# [Previous](directives.md) [Up](README.md) [Next](loops.md) 
