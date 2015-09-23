#C++

Copy this code into `fixed_loops.cpp`.

```c++
#include <iostream>
#include <mpi.h>

int main(int argc, char **argv)
{
    MPI::Init(argc, argv);

    // get the number of processes, and the id of this process
    int rank = MPI::COMM_WORLD.Get_rank();
    int nprocs = MPI::COMM_WORLD.Get_size();

    // we want to perform 1000 iterations in total. Work out the 
    // number of iterations to perform per process...
    int count = 1000 / nprocs;

    // we use the rank of this process to work out which
    // iterations to perform.
    int start = rank * count;
    int stop = start + count;

    // now perform the loop
    int nloops = 0;

    for (int i=start; i<stop; ++i)
    {
        ++nloops;
    }

    std::cout << "Process " << rank << " performed " << nloops 
              << " iterations of the loop.\n";

    if (rank != 0)
    {
        // if we are not the master process (rank 0) then we need to
        // tell that process how many iterations we performed
        MPI::COMM_WORLD.Send( &nloops, 1, MPI_INT, 0, 0 );
    }
    else
    {
        // if we are the master process, then we need to wait to be
        // told how many iterations were performed by each other
        // process
        int total_nloops = nloops;

        for (int i=1; i<nprocs; ++i)
        {
            MPI::COMM_WORLD.Recv( &nloops, 1, MPI_INT, i, 0 );

            total_nloops += nloops;
        }

        // ok - are there any more loops to run?
        nloops = 0;

        for (int i=total_nloops; i<1000; ++i)
        {
            ++nloops;
        }

        std::cout << "Process 0 performed the remaining " << nloops
                  << " iterations of the loop\n";
    }

    MPI::Finalize();

    return 0;
}
```

This example uses two new functions;

* `MPI::COMM_WORLD.Send(void *message, int size, MPI_INT, int process, 0)`. 
This function sends the message in the memory pointed to by `message` to 
the process whose rank is given in `process`. The message is an array of 
integers, where the number of integers is given in `size`.
* `MPI::COMM_WORLD.Recv(void *message, int size, MPI_INT, int process, 0)`. 
This function receives the message from the process whose rank is given in 
`process`. The received message is placed into the memory pointed to by 
`message`. The message is an array of integers, where the number of integers 
is given in `size`.

It is possible to send messages of other data types, e.g.

* `MPI_INT` - the message is a single integer, or an array of integers
* `MPI_FLOAT` - the message is a single float or an array of floats
* `MPI_DOUBLE` - the message is a single double or an array of doubles

Just replace `MPI_INT` in `MPI::COMM_WORLD.Send` and `MPI::COMM_WORLD.Recv` 
with the correct data type for the message.

The full list of MPI data types is [given here](http://www.mpi-forum.org/docs/mpi-20-html/node229.htm).

Note that it is also possible for you to define your own data types, although 
this is beyond the scope of this basic introductory course.

In this example, `MPI::COMM_WORLD.Send` is used to send the number of 
completed loops from each worker process (processes with ranks `1` to `N-1`) 
to the master process (process with rank `0`). `MPI::COMM_WORLD.Recv` is 
called `N-1` times on the master process to receive the `N-1` messages sent by 
the worker processes.

You can compile this example using;

    mpicxx fixed_loops.cpp -o fixed_loops

This will produce the executable `fixed_loops`.

[Return to the previous page](messages.md).

