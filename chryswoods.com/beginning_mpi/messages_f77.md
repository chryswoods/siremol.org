#Fortran

Copy this code into `fixed_loops.f`.

```f77
      program main
      implicit none
      include 'mpif.h'

      integer i, rank, nprocs, count, start, stop, nloops
      integer total_nloops,err
      integer status(MPI_STATUS_SIZE)

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

      if (rank .ne. 0) then
c        if we are not the master process (rank 0) then we need to
c        tell that process how many iterations we performed
         call MPI_Send( nloops, 1, MPI_INTEGER, 0, 0, MPI_COMM_WORLD, 
     .                  err )
      else
c        if we are the master process, then we need to wait to be
c        told how many iterations were performed by each other
c        process
         total_nloops = nloops;

         do i=1,nprocs-1
            call MPI_Recv( nloops, 1, MPI_INTEGER, i, 0, MPI_COMM_WORLD,
     .                     status, err )

            total_nloops = total_nloops + nloops
         enddo

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

This example uses two new functions;

* `MPI_Send(void message, integer size, MPI_INTEGER, integer process, 0, MPI_COMM_WORLD, err)`. 
This function sends the message in the memory pointed to by `message` to the process 
whose rank is given in `process`. The message is an array of integers, where the 
number of integers is given in `size`.
* `MPI_Recv(void message, integer size, MPI_INTEGER, integer process, 0, MPI_COMM_WORLD, status, err)`. 
This function receives the message from the process whose rank is given in `process`. 
The received message is placed into the memory pointed to by `message`. The message is 
an array of integers, where the number of integers is given in `size`. 
`status` is an array of integers that gives the status of the transfer. This must be 
an array declared as `integer status(MPI_STATUS_SIZE)`.

It is possible to send messages of other data types, e.g.

* `MPI_INTEGER` - the message is a single integer, or an array of integers
* `MPI_REAL` - the message is a single real number or an array of real numbers
* `MPI_DOUBLE_PRECISION` - the message is a single double precision number or an array of double precision numbers

Just replace `MPI_INTEGER` in `MPI_Send` and `MPI_Recv` with the correct data 
type for the message.

The full list of MPI data types is [given here](http://www.mpi-forum.org/docs/mpi-20-html/node229.htm).

Note that it is also possible for you to define your own data types, although 
this is beyond the scope of this basic introductory course.

In this example, `MPI_Send` is used to send the number of completed loops
from each worker process (processes with ranks `1` to `N-1`) to the master 
process (process with rank `0`). `MPI_Recv` is called `N-1` times on the master 
process to receive the `N-1` messages sent by the worker processes.

You can compile this example using;

    mpif77 fixed_loops.f -o fixed_loops

This will produce the executable `fixed_loops`.

[Return to the previous page](messages.md).
