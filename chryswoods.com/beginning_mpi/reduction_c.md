#C

Copy this code into `reduced_loops.c`.

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

    total_nloops = 0;
    MPI_Reduce( &nloops, &total_nloops, 1, MPI_INT, MPI_SUM,
                0, MPI_COMM_WORLD );

    if (rank == 0)
    {
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

In this code, `MPI_Send` and `MPI_Recv` have been replaced by a call to 
`MPI_Reduce(void *send, void *receive, int size, MPI_INT, MPI_SUM, int process, MPI_COMM_WORLD)`. 
This function reduces the data in the message pointed to by `send` using the 
MPI operation `MPI_SUM` and places the resulting message into `receive`. 
The messages are of size `size`, and you specify the data type as you do 
for `MPI_Recv` and `MPI_Send`, e.g. in this case we use `MPI_INT`. 
The resulting message is placed only into `receive` on the process whose 
rank is given in `process`. Note that all processes in the MPI process 
team must call this function with the same arguments, or else the result 
is undefined. Note also that other reduction operations are possible, 
e.g. by replacing `MPI_SUM` with `MPI_PROD`.

Compile the code using;

    mpicc reduced_loops.c -o reduced_loops

This will give you an executable called `reduced_loops`.

[Return to the previous page](reduction.md).
