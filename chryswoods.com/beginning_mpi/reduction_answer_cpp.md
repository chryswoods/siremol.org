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

    std::cout << "Process " << rank << " n_inside = " << n_inside
              << " n_outside = " << n_outside << "\n";

    int total_n_inside = 0;
    int total_n_outside = 0;

    MPI::COMM_WORLD.Reduce(&n_inside, &total_n_inside, 1, MPI_INT,
                           MPI::SUM, 0);

    MPI::COMM_WORLD.Reduce(&n_outside, &total_n_outside, 1, MPI_INT,
                           MPI::SUM, 0);

    if (rank == 0)
    {
        double pi = (4.0 * total_n_inside) / (total_n_inside + total_n_outside);
        std::cout << "The estimated value of pi is " << pi << "\n";
    }

    MPI::Finalize();

    return 0;
}
```

[Return](reduction.md)

