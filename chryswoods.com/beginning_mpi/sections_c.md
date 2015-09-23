#C

Create the file `mpi_sections.c` and copy in the following;

```c
#include <mpi.h>
#include <stdio.h>
#include <unistd.h>

void times_table(int n)
{
    int i, i_times_n, rank;
    
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    for (i=1; i<=n; ++i)
    {
        i_times_n = i * n;
        printf("Process %d says %d times %d equals %d.\n",
               rank, i, n, i_times_n );

        sleep(1);
    }
}

void countdown()
{
    int i, rank;

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    for (i=10; i>=1; --i)
    {
        printf("Process %d says %d...\n", rank, i);
        sleep(1);
    }

    printf("Process %d says \"Lift off!\"\n", rank);
}

void long_loop()
{
    int i, rank;
    double sum = 0;

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    for (i=1; i<=10; ++i)
    {
        sum += (i*i);
        sleep(1);
    }

    printf("Process %d says the sum of the long loop is %f\n",
            rank, sum);
}

int main(int argc, char **argv)
{
    int rank;

    MPI_Init(&argc, &argv);

    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 0)
    {
        printf("This is the main process.\n");
        times_table(12);
    }
    else if (rank == 1)
    {
        countdown();
    }
    else if (rank == 2)
    {
        long_loop();
    }
    else
    {
        printf("I am not needed...\n");
    }

    MPI_Finalize();

    return 0;
}
```

Note that we have included the header file `unistd.h` to use the function 
`sleep`, to add one second pauses (via `sleep(1)`) within each function.

In this example we use the function `MPI_Comm_rank(MPI_COMM_WORLD, int *rank)`. 
This function puts the rank of the calling process into the variable pointed to by 
`rank`. This allows the `if` block to be used to control which function is called 
by which process in the MPI process team. While it is possible to write the 
code within each block of the `if` statement directly, the code is more readable 
if you write each section as a function (e.g. `countdown`, `long_loop` and `times_table`) 
and just call the function from within each block.

You can compile this program using;

    mpicc mpi_sections.c -o mpi_sections

This will produce the executable, `mpi_sections`.

[Return to the previous page](sections.md).


