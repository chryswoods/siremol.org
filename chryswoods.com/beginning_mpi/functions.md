#Functions

So what was going on in the last example?

A standard program works by executing one line of code at a time, starting 
from the `main` function (or `program` function in Fortran) and working 
down line by line. This single thread of execution is known as the `main` thread. 
All programs have a single `main` thread, and in most programs, this is the 
only thread of execution, hence why the program can only do one thing at a time.

The `hello_mpi` example on the last page also has a single `main` thread of 
execution. However, `mpirun` now runs a team of copies of the program, all 
running in parallel at the same time together. The team of `hello_mpi` processes 
are coordinated together via MPI. Each parallel process in the team executes 
all of the code in the `main` function (or `program` function in Fortran), 
each working down line by line. Hence each process executes the line of 
code that prints `Hello MPI!`.

We can see this more clearly by getting each process to identify itself. 
Please copy the code from one of these examples to create the executable hello_processes.

* [C](functions_c.md)
* [C++](functions_cpp.md)
* [Fortran](functions_f77.md)

Try running this executable using `mpirun` specifying different numbers of processes, e.g.

    mpirun -np 2 hello_processes

or

    mpirun -np 4 hello_processes

If you run the example above as 4 processes, then you should get something like the output below;

````
I am process 1. The number of processes is 4.
I am process 3. The number of processes is 4.
I am process 0. The number of processes is 4.
I am process 2. The number of processes is 4.
````

Each process executed every line on code in the main function of the program. 
The four processes in the team ran in parallel together. However, note that 
there is no guarantee that the processes will print in order.

The MPI library provides a series of functions (subroutines) that allow each 
process in the MPI team to get information about the team, and to 
communicate (send messages) to other process members of the team. For example, 
the `hello_processes` example above uses MPI functions to initialise and 
shutdown MPI, and to get the total number of processes in the MPI team, 
and to get the identification number of each process in the team. 
The functions used in `hello_processes` are;

* `MPI_Init` / `MPI::Init` - Used to initialise MPI.
* `MPI_Finalize` - Used to close down MPI.
* `MPI_Comm_size` / `MPI::COMM_WORLD.Get_size()` - used to get the number of processes in the team
* `MPI_Comm_rank` / `MPI::COMM_WORLD.Get_rank()` - used to get the ID number (rank) of a process in the team.

The original MPI standard was developed for Fortran and C, and has a very similar 
structure and syntax for both of these languages. C++ programs are able to use the 
C functions directly (as C++ is almost a superset of C). A dedicated standard 
C++ interface for MPI was provided by MPI 2. This interface exposed the MPI interfaces 
as C++ objects, and has a different syntax and structure to the C and Fortran interfaces. 
If, as a C++ programmer, you don't like the C++ interface, remember that you are 
free to use the C interface. It is safe for a single C++ program to mix and match 
between the C++ and C interfaces.

In this course, the specifics of the differences between the C, C++ and Fortran 
interfaces is given with the code samples, while in the main text, 
the C / Fortran names of the functions will be used.

The standard MPI library is large, with many different functions. This course will 
cover the basic usage of just a selection;

* `MPI_Init` / `MPI_Finalize` : Used to initialise and shut down MPI, so that mpirun can create a team of processes.
* `MPI_Comm_rank` : Used to get the ID of a process in the team, e.g. so that different team members can perform different functions.
* `MPI_Comm_size` : Used to find the number of processes in the team, e.g. so single loops can be divided over team members.
* `MPI_Send` / `MPI_Recv` : Used to send and receive messages between team members, so that information calculated by one process can be sent to another.
* `MPI_Reduce` : Used to combine (reduce) the results of calculations performed in individual processes into a single result.
* `MPI_Bcast` : Used to broadcast a single value in one process in the team to all processes in the team.

***

[Compare with OpenMP](../beginning_openmp/directives.md)

***

# [Previous](basics.md) [Up](README.md) [Next](sections.md)

