#Fortran

Copy this into the file `hello_processes.f`

```f77
      program functions

      include "mpif.h"

      integer nprocs
      integer rank
      integer err

c     Initialise MPI
      call MPI_INIT(err)

c     Get the number of cores in the MPI cluster
      call MPI_Comm_size( MPI_COMM_WORLD, nprocs, err )

c     Get the ID of this core in the MPI cluster
      call MPI_Comm_rank( MPI_COMM_WORLD, rank, err )

      print *,"I am process ",rank,". The number of processes is ",
     .        nprocs

c     Shut down MPI
      call MPI_Finalize(err)

      end 
```

This example calls two MPI functions;

* `MPI_Comm_size(MPI_COMM_WORLD, integer size, integer err)` : Places the number of processes in the team into the variable `size`, with any errors reported in the integer `err`
* `MPI_Comm_rank(MPI_COMM_WORLD, integer rank, integer err)` : Places the rank of the calling process in the team into the variable `rank`, with any errors reported in the integer `err`

Note that using these functions requires you to include the `mpif.h` header file.

Note also that you have to pass `MPI_COMM_WORLD` as the first argument. This is a 
handle to the global communicator that is used to coordinate communication between 
all processes in the MPI process team. It is possible to create and use different 
MPI communicators in a program, e.g. by calling `MPI_Comm_create`, and passing the 
resulting handle to the new communicator in place of `MPI_COMM_WORLD`. Creating and 
managing different communicators is beyond the scope of this simple introduction, 
so all examples in this course will always use `MPI_COMM_WORLD`.

You can compile this program as you did for the `hello_mpi.f` in the last section, e.g.

    mpif77 hello_processes.f -o hello_processes

This will produce the executable, `hello_processes`.

[Return to the previous page](functions.md).
