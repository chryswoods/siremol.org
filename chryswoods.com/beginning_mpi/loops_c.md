#C

Copy this into `loops.c`

```c
#include <stdio.h>
#include <mpi.h>

int main(int argc, char **argv)
{
    int i, rank, nprocs, count, start, stop, nloops;

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

    MPI_Finalize();

    return 0;
}
```

In this example we use `MPI_Comm_size(MPI_COMM_WORLD, int *size)` to put the 
number of processes in the MPI process team into the variable pointed to by 
`size`. This allows each process to work out how many interations of the loop 
to perform, e.g. if there are four processes in the team, then each only needs 
run 250 of the 1000 iterations to be performed. In this example, the only work 
performed in each iteration is increasing the process-local counter of the 
number of times that the loop has been performed (each process in the team 
has its own copy of `nloops`). By doing this, each process in the team counts 
up the number of times that it has performed the loop.

You can compile this program using;

    mpicc loops.c -o loops

This will produce the executable, `loops`.

[Return to the previous page](loops.md).

