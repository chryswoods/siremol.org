#C

Copy the code below into `mapreduce.c`.

```c
#include <stdio.h>
#include <malloc.h>
#include <math.h>
#include <mpi.h>

/* Define an Ion type to hold the 
   coordinates of an Ion */
typedef struct Ion
{
    double x;
    double y;
    double z;
} Ion;

/* The reference Ion */
struct Ion reference_ion;

/* Return the square of a number */
double square(double x)
{
    return x*x;
}

/* Energy function to be mapped */
double calc_energy( struct Ion ion )
{
    double r;

    r = sqrt( square( reference_ion.x - ion.x ) +
              square( reference_ion.y - ion.y ) +
              square( reference_ion.z - ion.z ) );

    /* The energy is simply 1 / r */
    return 1.0 / r;
}

/* You will need to fill in this function to read in 
   an array of ions and return the array */
struct Ion* readArrayOfIons(int *num_ions)
{
    int i;
    Ion *ions = (Ion*)malloc(10 * sizeof(Ion));

    *num_ions = 10;

    for (i=0; i<10; ++i)
    {
        ions[i].x = 0.0;
        ions[i].y = 0.0;
        ions[i].z = i;
    }

    return ions;
}

int main(int argc, char **argv)
{
    int i, start, stop, num_ions, num_calc;
    struct Ion *ions_array;
    double total_energy, energy;
    int rank, nprocs;

    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &nprocs);

    if (rank == 0)
    {
        /* Lets put the reference ion at (1,2,3) */
        reference_ion.x = 1.0;
        reference_ion.y = 2.0;
        reference_ion.z = 3.0;

        /* Broadcast this to all processes */
        if (nprocs > 1)
        {
            MPI_Bcast(&reference_ion, 3, MPI_DOUBLE, 0,
                      MPI_COMM_WORLD);
        }

        /* Now read in an array of ions */
        ions_array = readArrayOfIons( &num_ions );

        /** Broadcast the array of ions. Note that it would be
            more efficient to send each process only the ions that
            it needs using MPI_Scatter... */
        if (nprocs > 1)
        {
            MPI_Bcast(&num_ions, 1, MPI_INT, 0, MPI_COMM_WORLD);
            MPI_Bcast(ions_array, 3*num_ions, MPI_DOUBLE, 0,
                      MPI_COMM_WORLD);
        } 
    }
    else
    {
        /** Receive the broadcast reference ion */
        MPI_Bcast(&reference_ion, 3, MPI_DOUBLE, 0, MPI_COMM_WORLD);

        /** Receive the number of ions in the array */
        MPI_Bcast(&num_ions, 1, MPI_INT, 0, MPI_COMM_WORLD);

        /** Create space for the ions */
        ions_array = (Ion*)malloc(num_ions * sizeof(Ion));

        /** Receive the ions array */
        MPI_Bcast(ions_array, 3*num_ions, MPI_DOUBLE, 0, MPI_COMM_WORLD);
    }

    energy = 0.0;
    total_energy = 0.0;

    num_calc = num_ions / nprocs;

    start = rank*num_calc;

    if (rank == nprocs-1)
    {
        stop = num_ions;
    }
    else
    {
        stop = start + num_calc;
    }

    for (i=start; i<stop; ++i)
    {
        energy += calc_energy( ions_array[i] );
    }

    printf("Process %d (%d to %d) Energy = %f\n", 
           rank, start, stop, energy);

    /* Reduce to get the result */
    MPI_Reduce(&energy, &total_energy, 1, MPI_DOUBLE, 
               MPI_SUM, 0, MPI_COMM_WORLD);

    if (rank == 0)
    {
        printf("The total energy is %f\n", total_energy);
    }

    MPI_Finalize();

    return 0;
}
```

The new MPI function here is 
`MPI_Bcast(void *message, int size, MPI_INT, int process, MPI_COMM_WORLD)`. 
This function copies the message held in `message` on the process whose rank 
is in `process` and broadcasts it so that it is received into `message` by 
all of the other processes in the MPI process team. `MPI_Bcast` is very useful 
when you want to send the same message to all processes in a team.

Compile the example using;

    mpicc mapreduce.c -o mapreduce

This will give you an executable called `mapreduce`.

[Return to the previous page](mapreduce.md).


