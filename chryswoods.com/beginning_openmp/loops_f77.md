#Fortran

Copy this into `loops.F`

```f77
      program main
      use omp_lib
      implicit none

      integer i, thread_id, nloops

C$OMP PARALLEL PRIVATE(thread_id, nloops)

      thread_id = omp_get_thread_num()
      nloops = 0

C$OMP DO
      do 100 i=1,1000
          nloops = nloops + 1
100   continue

      print *,"Thread ",thread_id," performed ",
     .        nloops," iterations."

C$OMP END PARALLEL

      end
```

The new directive in this code is `$OMP DO`. This tells the compiler that 
the `do` loop directly below this pragma can be run in parallel by the team 
of threads. In this case, the only work performed in each iteration is 
increasing the `thread private` counter of the number of times that the 
loop has been performed (each thread in the team has its own copy of `nloops` 
because it is specified as `PRIVATE` as part of the `!OMP PARALLEL` directive). 
By doing this, each thread in the team counts up the number of times 
that it has performed the loop.

You can compile this program using one of these commands (choose one for 
the compiler you wish to use);

* gfortran : `gfortran -fopenmp loops.f -o loops`
* ifort : `ifort -openmp loops.f -o loops -cxxlib-icc`
* pgf77 : `pgf77 -mp loops.f -o loops`

This will produce the executable, `loops`.

Now [return to the previous page](loops.md).

