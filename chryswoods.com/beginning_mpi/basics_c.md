#C

The MPI standard is provided in a C library, which can be linked to your 
program by using the MPI C compiler, `mpicc`.

The first step is to create a simple C program, which we will call `hello_mpi`. 
Open a text editor (e.g. `nano`), create a file called `hello_mpi.c` 
and copy in the following code;

```c
#include <stdio.h>

int main(int argc, char **argv)
{
    printf("Hello MPI!\n");

    return 0;
}
```

You can compile this program using;

    mpicc hello_mpi.c -o hello_mpi

Note that the MPI C compiler `mpicc` must be in your path. The compiler will be 
provided by the MPI library that you have installed. There are many different 
implementations of the MPI library, e.g. OpenMPI and mpich2. While you could 
compile an MPI program using your normal C compiler, the specifics of 
linking the program to the correct MPI library can be tricky. Each MPI 
library therefore provides `mpicc` as a thin wrapper around your C compiler, 
which automates finding and linking to the right MPI library, and 
handling any MPI-specific command-line flags and additional dependencies.

If you cannot find `mpicc` then you should either try to install an MPI 
library, or see if the library has been installed for you by your 
cluster administrator, e.g. it may have been installed as a module. 
At Bristol, we have OpenMPI installed as a module that can be loaded using the command;

    module add openmpi/gcc

[Return to the previous page](basics.md).
