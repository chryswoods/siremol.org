#Fortran

Copy this code into `broken_loopcount.F`

```f77
      program main
      use omp_lib
      implicit none

      integer i, thread_id
      integer private_nloops, global_nloops

      global_nloops = 0

C$OMP PARALLEL PRIVATE(thread_id, private_nloops)
      thread_id = omp_get_thread_num()
      private_nloops = 0

C$OMP DO
      do 100 i=1,100000
          private_nloops = private_nloops + 1
100   continue

      print *,"Thread ",thread_id," adding its iterations (",
     .        private_nloops,") to the sum (",global_nloops,
     .        ")..."

      global_nloops = global_nloops + private_nloops

      print *,"...total nloops now equals ",global_nloops

C$OMP END PARALLEL

      print *,"The total number of loop iterations is ",
     .        global_nloops

      end
```

and copy this code into fixed_loopcount.F

```f77
      program main
      use omp_lib
      implicit none

      integer i, thread_id
      integer private_nloops, global_nloops

      global_nloops = 0

C$OMP PARALLEL PRIVATE(thread_id, private_nloops)
      thread_id = omp_get_thread_num()
      private_nloops = 0

C$OMP DO
      do 100 i=1,100000
          private_nloops = private_nloops + 1
100   continue

C$OMP CRITICAL
      print *,"Thread ",thread_id," adding its iterations (",
     .        private_nloops,") to the sum (",global_nloops,
     .        ")..."

      global_nloops = global_nloops + private_nloops

      print *,"...total nloops now equals ",global_nloops
C$OMP END CRITICAL

C$OMP END PARALLEL

      print *,"The total number of loop iterations is ",
     .        global_nloops

      end
```

The only new code here is the `$OMP CRITICAL` to `$OMP END CRITICAL` section 
in `fixed_loopcount.c`. The critical section is performed by each thread, 
but can only be performed by one thread at a time. This ensures that while 
one thread is updating the `global nloops` variable (`global_nloops`) with 
the thread local value of `nloops` (`private_nloops`), that the value of 
`global_nloops` is not changed by any other thread.

You can compile these programs using one of these sets of commands (choose 
one for the compiler you wish to use);

* gfortran : `gfortran -fopenmp broken_loopcount.F -o broken_loopcount ; gfortran -fopenmp fixed_loopcount.F -o fixed_loopcount`
* ifort : `ifort -openmp broken_loopcount.F -o broken_loopcount -cxxlib-icc ; ifort -openmp fixed_loopcount.F -o fixed_loopcount -cxxlib-icc`
* pgf77 : `pgf77 -mp broken_loopcount.F -o broken_loopcount ; pgf77 -mp fixed_loopcount.F -o fixed_loopcount`

This will produce the executables, `broken_loopcount` and `fixed_loopcount`.

Now [return to the previous page](critical.md).

