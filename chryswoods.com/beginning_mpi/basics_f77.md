#Fortran

The MPI standard is provided in a Fortran library, which can be linked to you program 
by using the MPI Fortran compiler, `mpif77` or `mpif90`.

The first step is to create a simple Fortran program, which we will call `hello_mpi`. 
Open a text editor (e.g. `nano`), create a file called `hello_mpi.f` and copy in 
the following code;

```f77
      program hello_mpi

      print *,"Hello MPI!" 

      end
```
 
(note that this course uses Fortran 77 fixed format, although Fortran 90 could instead be used)

You can compile this program using;

    mpif77 hello_mpi.f -o hello_mpi

Note that the MPI Fortran compiler `mpif77` must be in your path. The compiler 
will be provided by the MPI library that you have installed. There are many 
different implementations of the MPI library, e.g. OpenMPI and mpich2. While you 
could compile an MPI program using your normal Fortran compiler, the specifics of 
linking the program to the correct MPI library can be tricky. Each MPI library 
therefore provides `mpif77` as a thin wrapper around your Fortran compiler, 
that automates finding and linking to the right MPI library, and handling 
any MPI-specific command-line flags and additional dependencies.

If you cannot find `mpif77` then you should either try to install an MPI 
library, or see if the library has been installed for you by your cluster 
administrator, e.g. it may have been installed as a module. At Bristol, 
we have OpenMPI installed as a module that can be loaded using the command;

    module add openmpi/gcc

[Return to the previous page](basics.md).

