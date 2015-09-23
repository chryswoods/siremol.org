# Sections

The MPI function `MPI_Comm_rank` can be used to obtain the identification number 
of a member of an MPI team of processes. This identification number, known as a rank, 
runs from `0` to `N-1`, where `N` is the number of processes in the team. Typically, 
we tend to think of the process with rank `0` as being the master process, 
while processes with ranks `1` to `N-1` are the child or worker processes.

While each MPI process in the team starts with the same main function, it is 
possible to use the rank of a process to get each member of the MPI team to run 
different sections of code. Copy the code from the appropriate link below to create 
the executable `mpi_sections`.

* [C](sections_c.md)
* [C++](sections_cpp.md)
* [Fortran](sections_f77.md)

Try running the executable `mpi_sections` using different numbers of processes 
(via `mpirun -np X`).

In this example, there are three functions, `times_table`, `countdown` and `long_loop`. 
These three functions are called from an `if` block in the main function. The decision 
of which function to run is based on the rank of the MPI process. If the 
processes rank is `0`, then `times_table` is called. If the rank is `1`, then 
`countdown` is called. If the rank is `2`, then `long_loop` is called. If the 
rank is greater than `2`, then the MPI process does nothing, and is ignored.

***

[Compare with OpenMP](../beginning_openmp/sections.md)

***

# [Previous](functions.md) [Up](README.md) [Next](loops.md)
