#Fortran

Copy this code into `reduced_loops.f`.

```f77
      program main
      implicit none
      include 'mpif.h'

      integer i, rank, nprocs, count, start, stop, nloops
      integer total_nloops,err

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

      total_nloops = 0
      call MPI_Reduce( nloops, total_nloops, 1, MPI_INTEGER,
     .                 MPI_SUM, 0, MPI_COMM_WORLD, err )

      if (rank .eq. 0) then
c        ok - are there any more loops to run?
         nloops = 0

         if (total_nloops .lt. 1000) then
           do i=total_nloops,1000-1
              nloops = nloops + 1
           enddo
         endif

         print *,"Process 0 performed the remaining ",nloops,
     .           " iterations of the loop"
      endif

      call MPI_Finalize()

      end
```

In this code, `MPI_Send` and `MPI_Recv` have been replaced by a call to 
`MPI_Reduce(void send, void receive, integer size, MPI_INTEGER, MPI_SUM, integer process, MPI_COMM_WORLD, integer err)`. 
This function reduces the data in the message in `send` using the MPI operation 
`MPI_SUM` and places the resulting message into `receive`. The messages are of 
size `size`, and you specify the data type as you do for `MPI_Recv` and `MPI_Send`, 
e.g. in this case we use `MPI_INTEGER`. The resulting message is placed only 
into `receive` on the process whose rank is given in `process`. Note that all 
processes in the MPI process team must call this function with the same 
arguments, or else the result is undefined. Note also that other reduction 
operations are possible, e.g. by replacing `MPI_SUM` with `MPI_PROD`.

Compile the code using;

    mpif77 reduced_loops.f -o reduced_loops

This will give you an executable called `reduced_loops`.

[Return to the previous page](reduction.md).

