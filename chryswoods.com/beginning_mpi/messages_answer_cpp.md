#Answer to exercise (C++)

```c++
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <mpi.h>

double rand_one()
{
    return std::rand() / (RAND_MAX + 1.0);
}

int main(int argc, char **argv)
{
    int n_inside = 0;
    int n_outside = 0;

    MPI::Init(argc, argv);

    // get the number of processors in the cluster
    int nprocs = MPI::COMM_WORLD.Get_size();

    // make sure that each process has a different random
    // number seed
    int rank = MPI::COMM_WORLD.Get_rank();

    std::srand( rank * 473879 );

    // calculate the number of iterations - we want 1000000 in total
    int niters = 1000000 / nprocs;

    // perform this processes batch of iterations
    for (int i=0; i<niters; ++i)
    {
        double x = (2*rand_one()) - 1;
        double y = (2*rand_one()) - 1;

        double r = std::sqrt( x*x + y*y );

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
        int total_n_inside = n_inside;
        int total_n_outside = n_outside;

        std::cout << "Process " << rank << " n_inside = " << n_inside
                  << " n_outside = " << n_outside << "\n";

        //collect every other processes result
        for (int i=1; i<nprocs; ++i)
        {
            MPI::COMM_WORLD.Recv( &n_inside, 1, MPI_INT, i, 0 );
            MPI::COMM_WORLD.Recv( &n_outside, 1, MPI_INT, i, 0 );

            total_n_inside += n_inside;
            total_n_outside += n_outside;
        }

        double pi = (4.0 * total_n_inside) / (total_n_inside + total_n_outside);
        std::cout << "The estimated value of pi is " << pi << "\n";
    }
    else
    {
        //send the results to the master process
        MPI::COMM_WORLD.Send( &n_inside, 1, MPI_INT, 0, 0 );
        MPI::COMM_WORLD.Send( &n_outside, 1, MPI_INT, 0, 0 );

        std::cout << "Process " << rank << " n_inside = " << n_inside
                  << " n_outside = " << n_outside << "\n";
    }

    MPI::Finalize();

    return 0;
}
```

[Return](messages.md)
