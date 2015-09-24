#C++

Copy this code into `reduced_loops.cpp`.

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

    int total_nloops = 0;
    MPI::COMM_WORLD.Reduce( &nloops, &total_nloops, 1, MPI_INT,
                               MPI_SUM, 0);

    if (rank == 0)
    {
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

In this code, `MPI::COMM_WORLD.Send` and `MPI::COMM_WORLD.Recv` have been 
replaced by a call to `MPI::COMM_WORLD.Reduce(void *send, void *receive, int size, MPI_INT, MPI_SUM, int process)`. 
This function reduces the data in the message pointed to by `send` using the 
MPI operation `MPI_SUM` and places the resulting message into `receive`. 
The messages are of size `size`, and you specify the data type as you do 
for `MPI::COMM_WORLD.Recv` and `MPI::COMM_WORLD.Send`, e.g. in this case 
we use `MPI_INT`. The resulting message is placed only into `receive` on the 
process whose rank is given in `process`. Note that all processes in the MPI 
process team must call this function with the same arguments, or else 
the result is undefined. Note also that other reduction operations are 
possible, e.g. by replacing `MPI_SUM` with `MPI_PROD`.

Compile the code using;

    mpicxx reduced_loops.cpp -o reduced_loops

This will give you an executable called `reduced_loops`.

[Return to the previous page](reduction.md).
