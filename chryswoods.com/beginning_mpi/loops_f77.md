#Fortran

Copy this into `loops.f`

```f77
      program main

      include 'mpif.h'

      integer i, rank, nprocs, count, start, stop, nloops
      integer err

      call MPI_Init(err)

c     get the number of processes, and the id of this process
      call MPI_Comm_rank(MPI_COMM_WORLD, rank, err)
      call MPI_Comm_size(MPI_COMM_WORLD, nprocs, err)

c     we want to perform 1000 iterations in total. Work out the 
c     number of iterations to perform per process...
      count = 1000 / nprocs

c     we use the rank of this process to work out which
c     iterations to perform.
      start = rank * count
      stop = start + count - 1

c     now perform the loop
      nloops = 0

      do i=start,stop
        nloops = nloops + 1
      enddo

      print *,"Process ",rank," performed ",nloops,
     .        " iterations of the loop."

      call MPI_Finalize();

      end
```

In this example we use `MPI_Comm_size(MPI_COMM_WORLD, integer size, integer err)` 
to put the number of processes in the MPI process team into the variable `size`. 
This allows each process to work out how many interations of the loop to perform, 
e.g. if there are four processes in the team, then each only needs run 250 of 
the 1000 iterations to be performed. In this example, the only work performed 
in each iteration is increasing the process-local counter of the number of 
times that the loop has been performed (each process in the team has its own 
copy of `nloops`). By doing this, each process in the team counts up the number 
of times that it has performed the loop.

You can compile this program using;

    mpif77 loops.f -o loops

This will produce the executable, `loops`.

[Return to the previous page](loops.md).


