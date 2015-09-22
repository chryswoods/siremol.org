#Fortran

Copy this into the file `hello_threads.F` (make sure you use a capital `.F`).

```f77
      program main

#ifdef _OPENMP
      use omp_lib
#endif

      implicit none

      integer thread_id
      integer num_threads

      print *,"I am the main thread."

C$OMP PARALLEL PRIVATE(thread_id, num_threads)

#ifdef _OPENMP
      thread_id = omp_get_thread_num()
      num_threads = omp_get_num_threads()
#else
      thread_id = 0
      num_threads = 1
#endif

      print *,"Hello. I am thread ",thread_id," out of a team of ",
     .        num_threads
C$OMP END PARALLEL

      print *,"Here I am, back to the main thread."

      end
```

This example uses two OpenMP functions;

* `omp_get_num_threads()` : Returns the number of threads in the OpenMP thread team.
* `omp_get_thread_num()` : Returns the identifying number of the thread in the team.

Note that using these functions requires you to use the `omp_lib` Fortran library. 
To ensure portability (if OpenMP is not supported) we hide this header file 
behind an `#ifdef _OPENMP` guard, and manually set the values of `num_threads`
and `thread_id` if `_OPENMP` is not set.

This example uses a slightly modified `omp parallel` line. In this case, 
`private(nthreads, thread_id)` is added to specify that each thread should 
have its own copy of the `nthreads` and `thread_id` variables.

You can compile this program using one of these commands (choose one for the 
compiler you wish to use);

* gfortran : `gfortran -fopenmp hello_threads.F -o hello_threads`
* ifort : `ifort -openmp hello_threads.F -o hello_threads -cxxlib-icc`
* pgf77 : `pgf77 -mp hello_threads.F -o hello_threads`

This will produce the executable, `hello_threads`.

Now [return to the previous page](directives.md).
