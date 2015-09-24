#C++

Copy the code below into `mapreduce.cpp`.

```c++
#include <cmath>
#include <vector>
#include <iostream>
#include <mpi.h>

// Define an ion type to hold the
// coordinates of the ion
struct Ion
{
    Ion()
    {
        x = 0;
        y = 0;
        z = 0;
    }

    Ion(double _x, double _y, double _z)
    {
        x = _x;
        y = _y;
        z = _z;
    }

    double x;
    double y;
    double z;
};

// The reference ion
Ion reference_ion;

// Return the square of a number
inline double square(const double x)
{
    return x*x;
}

// Energy function to be mapped
double calc_energy(const Ion &ion)
{
    double r = std::sqrt( square( reference_ion.x - ion.x ) + 
                          square( reference_ion.y - ion.y ) +
                          square( reference_ion.z - ion.z ) );

    // The energy is simply 1 / r
    return 1.0 / r;
}

// You would need to fill in this function to read
// in an array of ions and return the array
std::vector<Ion> readArrayOfIons()
{
    std::vector<Ion> ions;

    for (int i=0; i<10; ++i)
    {
        ions.push_back( Ion(0,0,i) );
    }

    return ions;
}

int main(int argc, char **argv)
{
    MPI::Init(argc, argv);

    int rank = MPI::COMM_WORLD.Get_rank();
    int nprocs = MPI::COMM_WORLD.Get_size();

    std::vector<Ion> ions_array;

    if (rank == 0)
    {
        //put the reference ion at (1,2,3)
        reference_ion.x = 1.0;
        reference_ion.y = 2.0;
        reference_ion.z = 3.0;

        if (nprocs > 1)
        { 
            //broadcast the reference ion to all processes
            MPI::COMM_WORLD.Bcast(&reference_ion, 3, MPI_DOUBLE, 0);
        }

        //read in the array of ions
        ions_array = readArrayOfIons();

        if (nprocs > 1)
        {
            //broadcast the array of ions to all processes
            //(note that it would be more efficient to send each process
            //just the ions that it needs using MPI_Scatter...)
            int num_ions = ions_array.size();
            MPI::COMM_WORLD.Bcast(&num_ions, 1, MPI_INT, 0);
            MPI::COMM_WORLD.Bcast(ions_array.data(), 3*num_ions, MPI_DOUBLE, 0);
        }
    }
    else
    {
        //receive the broadcast of the reference ion
        MPI::COMM_WORLD.Bcast(&reference_ion, 3, MPI_DOUBLE, 0);

        //get the number of ions in the array
        int num_ions;
        MPI::COMM_WORLD.Bcast(&num_ions, 1, MPI_INT, 0);

        //make space for the ions
        ions_array = std::vector<Ion>(num_ions);

        //receive the array of ions
        MPI::COMM_WORLD.Bcast(ions_array.data(), 3*num_ions, MPI_DOUBLE, 0);
    }

    double energy = 0.0;
    double total_energy = 0.0;

    int num_calc = ions_array.size() / nprocs;

    int start = rank*num_calc;
    int stop = start + num_calc;

    if (rank == nprocs-1)
    {
        stop = ions_array.size();
    }

    for (int i=start; i<stop; ++i)
    {
        energy += calc_energy( ions_array[i] );
    }

    std::cout << "Process " << rank << " (" << start << " to " << stop
              << ") Energy = " << energy << "\n"; 

    // Reduce to get the result
    MPI::COMM_WORLD.Reduce(&energy, &total_energy, 1, MPI_DOUBLE, 
                           MPI_SUM, 0);

    if (rank == 0)
    {
        std::cout << "The total energy is " << total_energy << std::endl;
    }

    MPI::Finalize();

    return 0;
}
```

The new MPI function here is 
`MPI::COMM_WORLD.Bcast(void *message, int size, MPI_INT, int process)`. 
This function copies the message held in `message` on the process whose 
rank is in `process` and broadcasts it so that it is received into `message` 
by all of the other processes in the MPI process team. 
`MPI::COMM_WORLD.Bcast` is very useful when you want to send the same 
message to all processes in a team.

Compile the example using;

    mpicxx mapreduce.cpp -o mapreduce

This will give you an executable called `mapreduce`.

[Return to the previous page](mapreduce.md).

