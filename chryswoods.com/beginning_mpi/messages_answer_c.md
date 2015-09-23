#Answer to exercise (C)

```c
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <mpi.h>

double rand_one()
{
    return rand() / (RAND_MAX + 1.0);
}

int main(int argc, char **argv)
{
    int n_inside, n_outside;
    int total_n_inside, total_n_outside;
    int rank, nprocs, niters;
    int i;

    double x, y, r, pi;

    n_inside = 0;
    n_outside = 0;

    MPI_Init(&argc, &argv);

    // get the number of processors in the cluster
    MPI_Comm_size(MPI_COMM_WORLD, &nprocs);

    // make sure that each process has a different random
    // number seed
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    srand( rank * 473879 );

    // calculate the number of iterations - we want 1000000 in total
    niters = 1000000 / nprocs;

    // perform this processes batch of iterations
    for (i=0; i<niters; ++i)
    {
        x = (2*rand_one()) - 1;
        y = (2*rand_one()) - 1;

        r = sqrt( x*x + y*y );

        if (r < 1.0)
        {
            ++n_inside;
        }
        else
        {
            ++n_outside;
        }
    }

    if (rank == 0)
    {
        total_n_inside = n_inside;
        total_n_outside = n_outside;

        printf("Process %d: n_inside = %d, n_outside = %d\n",
               rank, n_inside, n_outside);

        //collect every other processes result
        for (i=1; i<procs; ++i)
        {
            MPI_Recv( &n_inside, 1, MPI_INT, i, 0, MPI_COMM_WORLD, 0 );
            MPI_Recv( &n_outside, 1, MPI_INT, i, 0, MPI_COMM_WORLD, 0 );

            total_n_inside += n_inside;
            total_n_outside += n_outside;
        }

        pi = (4.0 * total_n_inside) / (total_n_inside + total_n_outside);
        printf("The estimated value of pi is %f\n", pi);
    }
    else
    {
        //send the results to the master process
        MPI_Send( &n_inside, 1, MPI_INT, 0, 0, MPI_COMM_WORLD );
        MPI_Send( &n_outside, 1, MPI_INT, 0, 0, MPI_COMM_WORLD );

        printf("Process %d: n_inside = %d, n_outside = %d\n",
               rank, n_inside, n_outside);
    }

    MPI_Finalize();

    return 0;
}
```

[Return](messages.md)

