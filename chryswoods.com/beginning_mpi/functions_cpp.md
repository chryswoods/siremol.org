#C++

Copy this into the file `hello_processes.cpp`

```c++
#include <mpi.h>
#include <iostream>

int main(int argc, char **argv)
{
    // Initialise MPI
    MPI_Init(&argc, &argv);

    // Get the number of cores in the MPI cluster
    int nprocs = MPI::COMM_WORLD.Get_size();

    // Get the ID number of this core in the MPI cluster
    int rank = MPI::COMM_WORLD.Get_rank();

    std::cout << "I am process " << rank
              << ". The number of processes is " << nprocs << ".\n";

    // Shut down MPI
    MPI::Finalize();

    return 0;
}
```

This example calls two MPI functions;

* `MPI::COMM_WORLD.Get_size()` : Returns the number of processes in the MPI processteam
* `MPI::COMM_WORLD.Get_rank()` : Returns the rank of the calling process.

Note that using these functions requires you to include the `mpi.h` header file. 
For some MPI implementations, you may also need to include an extra C++ MPI 
header file, called something like `mpic++.h`. See the documentation of your
MPI library for more details. Also, the C++ wrappers were only standardised 
in MPI 2. Most MPI libraries now support MPI 2, but older MPI libraries may 
be missing the C++ wrappers.

Note that all MPI functions are in the MPI namespace. Also note that the 
functions are called from the object `MPI::COMM_WORLD`. This object represents 
the global communicator that is used to coordinate communication between 
all processes in the MPI process team. It is possible to create and use 
different MPI communicators in a program, and calling the same MPI functions 
using the object representing the new communicator. Creating and managing 
different communicators is beyond the scope of this simple introduction, 
so all examples in this course will always use `MPI::COMM_WORLD`.

You can compile this program as you did for the `hello_mpi.cpp` in the last section, e.g.

    mpicxx hello_processes.cpp -o hello_processes

This will produce the executable, `hello_processes`.

[Return to the previous page](functions.md).
