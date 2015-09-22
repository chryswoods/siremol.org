#Directives (Pragmas)

So what was going on in the last example?

A standard program works by executing one line of code at a time, 
starting from the main function (or "program" function in Fortran) 
and working down line by line. This single thread of execution is 
known as the `main` thread. All programs have a single `main` thread, 
and in most programs, this is the only thread of execution, hence 
why the program can only do one thing at a time.

The `hello_openmp` program also has a single `main` thread of execution. 
However, this `main` thread is split into a team of threads within the 
OpenMP parallel section. Each parallel thread in the team executes all 
of the code in the parallel section, hence each thread executes the 
line of code that prints `Hello OpenMP!`.

We can see this more clearly by getting each thread to identify itself. 
Please copy the code from one of these examples to create the executable hello_threads.

* [C](directives_c.md)
* [C++](directives_cpp.md)
* [Fortran](directives_f77.md)

Try running this executable using different values of `OMP_NUM_THREADS`.

The OpenMP parallel section is specified by using compiler directives. 
These directives (also called compiler pragmas) are instructions to the 
compiler to tell it how to create the team of threads, and to help 
tell the compiler how to assign threads to tasks. These OpenMP directives 
are only followed if the program is compiled with OpenMP support. If 
the program is compiled without OpenMP support, then they are ignored.

There are several OpenMP directives. This course will cover the basic usage of just a selection;

* `parallel` : Used to create a parallel block of code which will be executed by a team of threads
* `sections` : Used to specify different sections of the code that can be run in parallel by different threads.
* `for` (C/C++), `do` (Fortran) : Used to specify loops where different iterations of the loop are performed by different threads.
* `critical` : Used to specify a block of code that can only be run by one thread at a time.
* `reduction` : Used to combine (reduce) the results of several local calculations into a single result

Pragmas are added to the code using either;

    #pragma omp name_of_directive

in C or C++, or using;

    C$OMP name_of_directive

at the start of the line in fixed-format Fortran, or using;

    !$OMP name_of_directive

anywhere in the line using free-format Fortran.

***

[Compare with MPI](../beginning_mpi/functions.md)

***

# [Previous](basics.md) [Up](README.md) [Next](sections.md)
