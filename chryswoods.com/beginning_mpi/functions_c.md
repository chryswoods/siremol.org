#C

Copy this into the file `hello_processes.c`

```c
#include <mpi.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    int nprocs;    //holder for the number of cores
    int rank;   //holder for the ID number of this core

    // Initialise MPI
    MPI_Init(&argc, &argv);

    // Get the number of cores in the MPI cluster
    MPI_Comm_size( MPI_COMM_WORLD, &nprocs );

    // Get the ID number of this core in the MPI cluster
    MPI_Comm_rank( MPI_COMM_WORLD, &rank );

    printf("I am process %d. The number of processes is %d.\n", rank, nprocs);

    // Shut down MPI
    MPI_Finalize();

    return 0;
} 
```

This example calls two MPI functions;

* `MPI_Comm_size(MPI_COMM_WORLD, int *size)` : Places the number of processes in the team into the variable pointed to by `size`
* `MPI_Comm_rank(MPI_COMM_WORLD, int *rank)` : Places the rank of the calling process in the team into the variable pointed to by `rank`.

Note that using these functions requires you to include the `mpi.h` header file.

Note also that you have to pass `MPI_COMM_WORLD` as the first argument. This is a 
pointer to the global communicator that is used to coordinate communication between 
all processes in the MPI process team. It is possible to create and use different 
MPI communicators in a program, e.g. by calling `MPI_Comm_create`, and 
passing the pointer to the new communicator in place of `MPI_COMM_WORLD`. 
Creating and managing different communicators is beyond the scope of this simple 
introduction, so all examples in this course will always use `MPI_COMM_WORLD`.

You can compile this program as you did for the `hello_mpi.c` in the last section, e.g.

    mpicc hello_processes.c -o hello_processes

This will produce the executable, `hello_processes`.

[Return to the previous page](functions.md).
