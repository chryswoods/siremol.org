#C

Copy this code into `fixed_loops.c`.

```c
#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv)
{
    int i, rank, nprocs, count, start, stop, nloops, total_nloops;

    MPI_Init(&argc, &argv);

    // get the number of processes, and the id of this process
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &nprocs);

    // we want to perform 1000 iterations in total. Work out the 
    // number of iterations to perform per process...
    count = 1000 / nprocs;

    // we use the rank of this process to work out which
    // iterations to perform.
    start = rank * count;
    stop = start + count;

    // now perform the loop
    nloops = 0;

    for (i=start; i<stop; ++i)
    {
        ++nloops;
    }

    printf("Process %d performed %d iterations of the loop.\n",
           rank, nloops);

    if (rank != 0)
    {
        // if we are not the master process (rank 0) then we need to
        // tell that process how many iterations we performed
        MPI_Send( &nloops, 1, MPI_INT, 0, 0, MPI_COMM_WORLD );
    }
    else
    {
        // if we are the master process, then we need to wait to be
        // told how many iterations were performed by each other
        // process
        total_nloops = nloops;

        for (i=1; i<nprocs; ++i)
        {
            MPI_Recv( &nloops, 1, MPI_INT, i, 0, MPI_COMM_WORLD, 0 );

            total_nloops += nloops;
        }

        // ok - are there any more loops to run?
        nloops = 0;

        for (i=total_nloops; i<1000; ++i)
        {
            ++nloops;
        }

        printf("Process 0 performed the remaining %d iterations of the loop\n",
               nloops);
    }

    MPI_Finalize();

    return 0;
}
```

This example uses two new functions;

* `MPI_Send(void *message, int size, MPI_INT, int process, 0, MPI_COMM_WORLD)`. This 
function sends the message in the memory pointed to by `message` to the process 
whose rank is given in `process`. The message is an array of integers, where the 
number of integers is given in `size`.
* `MPI_Recv(void *message, int size, MPI_INT, int process, 0, MPI_COMM_WORLD, 0)`. 
This function receives the message from the process whose rank is given in `process`. 
The received message is placed into the memory pointed to by `message`. 
The message is an array of integers, where the number of integers is given in `size`.

It is possible to send messages of other data types, e.g.

* `MPI_INT` - the message is a single integer, or an array of integers
* `MPI_FLOAT` - the message is a single float or an array of floats
* `MPI_DOUBLE` - the message is a single double or an array of doubles

Just replace `MPI_INT` in `MPI_Send` and `MPI_Recv` with the correct data type for the message.

The full list of MPI data types is [given here](http://www.mpi-forum.org/docs/mpi-20-html/node229.htm).

Note that it is also possible for you to define your own data types, although 
this is beyond the scope of this basic introductory course.

In this example, `MPI_Send` is used to send the number of completed loops from 
each worker process (processes with ranks `1` to `N-1`) to the master process 
(process with rank `0`). `MPI_Recv` is called `N-1` times on the master process 
to receive the `N-1` messages sent by the worker processes.

You can compile this example using;

    mpicc fixed_loops.c -o fixed_loops

This will produce the executable `fixed_loops`.

[Return to the previous page](messages.md).
