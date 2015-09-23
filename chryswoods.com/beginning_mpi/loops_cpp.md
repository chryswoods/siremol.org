#C++

Copy this into `loops.cpp`

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

    MPI::Finalize();

    return 0;
}
```

In this example we use `MPI::COMM_WORLD.Get_size()` to return the number of processes 
in the MPI process team. This allows each process to work out how many interations 
of the loop to perform, e.g. if there are four processes in the team, then each 
only needs run 250 of the 1000 iterations to be performed. In this example, 
the only work performed in each iteration is increasing the process-local 
counter of the number of times that the loop has been performed (each process 
in the team has its own copy of `nloops`). By doing this, each process in the 
team counts up the number of times that it has performed the loop.

You can compile this program using;

    mpicxx loops.cpp -o loops

This will produce the executable, `loops`.

[Return to the previous page](loops.md).


