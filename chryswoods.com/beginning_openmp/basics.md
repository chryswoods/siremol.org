#Hello OpenMP!

The first stage is to write a small OpenMP program. Choose from 
[C](basics_c.md), [C++](basics_cpp.md) or [Fortran](basics_f77.md) 
to write the program `hello_openmp`. Once you have written and compiled 
`hello_openmp` return to this page.

Now that you have the compiled the `hello_openmp` executable, the next 
step is to run it. The way to run the executable is the same regardless 
of the programming language used to produce it. The first step is to 
set the number of threads of execution that you want to run in parallel. 
This is achieved by setting the environmental variable `OMP_NUM_THREADS` 
to the desired number of threads, e.g. in the bash shell;

    export OMP_NUM_THREADS=4

or in the tcsh shell;

    setenv OMP_NUM_THREADS 4

Now that you have set the number of threads, run the executable by typing;

    ./hello_openmp

You should see the following output.

```
Hello OpenMP!
Hello OpenMP!
Hello OpenMP!
Hello OpenMP!
```

The line `Hello OpenMP!` is output four times, as the program split 
into four threads, and each thread printed `Hello OpenMP!`. Play 
with the number of threads (by changing `OMP_NUM_THREADS`) and see 
how that affects the output.

***

[Compare with MPI](../beginning_mpi/basics.md)

***

# [Previous](README.md) [Up](README.md) [Next](directives.md) 
