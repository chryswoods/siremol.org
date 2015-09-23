#Messages

Up to this point, the examples have shown how to just run different parts of the 
program in parallel, either by the process rank to control running different 
functions in different processes, or using loops, and sharing the different 
iterations of the loop amongst the processes in the MPI team. While this is good, 
it isn't yet useful. This is because we have not yet seen how to make the processes 
work together on a problem. At the moment, each process works on its own, using 
its own internal memory and variables. For example, we've seen how each process 
can count the number of iterations it performed itself in a loop, but no mechanism 
has been presented yet that would allow the team of processes to count up the total 
number of iterations performed by all of them.

What we need is a way to allow the processes to talk to each other and to share 
the data held in each processes' memory. MPI has been designed specifically for this 
purpose. MPI stands for "Message Passing Library", and its main purpose is to 
allow processes in a team to share data by sending message to one another.

An MPI message is a piece of data, such as a single integer, which can be sent 
from one process to another. For example, this allows each of the "worker" 
processes to send a message to the "master" process, so that the "master" process 
can accumulate a single variable that holds the result combined from those 
calculated by each member of the process team. To make this clear, consider 
the loops example from the previous page. In that example, each process counted 
up the number of loops that it performed, with the aim being that the team of 
processes completed 1000 iterations of the loop between them. However, the logic 
used to work out how to divide the loops amongst the team was quite basic, 
with the total number of iterations (1000) divided equally between the members 
of the team. While this worked if there were four processes in the team 
(each running 250 iterations each), it doesn't work with three members. 
This is because each member only performs 333 iterations. There was no mechanism 
to tell the master process (process with rank 0) that one of the iterations 
had been left out.

We can fix this by having each of the worker processes (processes with ranks `1` to `N-1`) 
tell the master process how many iterations they have performed. The master process 
can then work out if any iterations have been left out, and then process those 
iterations itself. This is performed in the next example, which you should call `fixed_loops`;

* [C](messages_c.md)
* [C++](messages_cpp.md)
* [Fortran](messages_f77.md)

Try running both `loops` and `fixed_loops` using different numbers of processes 
in the MPI team. You should find `fixed_loops` correctly identifies times when 
the team miss iterations, and so the master process is able to run those iterations itself.

Messages in MPI are sent using the `MPI_Send` function, while they are received 
by the `MPI_Recv` function. A message is sent from one process to the other, 
using the processes rank to specify who to send the message to (in `MPI_Send`), 
or who to receive the message from (in `MPI_Recv`). An `MPI_Send` must be 
matched with an `MPI_Recv`, or else the program will block, with either one 
process waiting for a message that is never sent, or another process waiting 
for the delivery of a message that is not being waited for.

MPI messages must specify the type of message, and the size of message. The type 
specifies which type of variable is being sent, e.g. integer, floating point number etc. 
The size of the message specifies the number of variables being sent. 
For example, `MPI_INT, 1` refers to a single C or C++ integer. `MPI_INTEGER, 1` 
would refer to a single Fortran integer. To specify an array of 10 integers you would 
use `MPI_INT, 10`, or `MPI_INTEGER, 10` depending on whether you are using C/C++ or Fortran. 
To specify a message of 5 double precision floating point numbers, 
you would use `MPI_DOUBLE, 5` in C/C++, and `MPI_DOUBLE_PRECISION, 5` in Fortran.

Note that the memory for the variable in which the message will be sent or received 
must be valid, and that the type and size of the message must be the same for an 
`MPI_Send` / `MPI_Recv` pair. It is very easy to introduce bugs by not matching 
`MPI_Send` with a corresponding `MPI_Recv`, and so debugging MPI programs can be 
a lengthy and complex process. You should always strive to document use of 
`MPI_Send` and `MPI_Recv` in your code, and to make sure that communication between 
processes is kept as simple as possible. One strategy, employed here, is to designate 
one process as the master, and the rest as worker, and then set it so that the worker 
processes only send messages to the master.

***

##Exercise

Write an MPI parallel program to calculate pi using a Monte Carlo algorithm.

Pi can be calculated using Monte Carlo by imagining a circle with radius 1 sitting 
at the origin within a square that just contains this circle 
(so with corners [-1,-1], [-1,1], [1,-1] and [1,1]). The area of the circle 
is pi, (from pi r squared), while the area of the square is 4. If we imagine 
throwing darts randomly at the square, than the proportion that lie within the 
circle compared to the proportion that lie outside the circle will be directly 
related to the ratio of the area of the circle against the area of the square.

In a parallel loop, you must thus generate a large number of random points 
in the square, and count up the number that lie within the circle and those 
that lie outside. Reduce these numbers into a global count of the number inside 
and outside the circle, and then finally take the ratio of these numbers to get 
the value of pi. This algorithm to calculate pi is [described in more 
detail here](http://www.chem.unl.edu/zeng/joy/mclab/mcintro.html).

Note that you will need to use the following random number functions and square root functions;

* C : `rand` `srand` and `sqrt`, contained in `math.h` and `stdlib.h`
* C++ : `std::rand` `std::srand` and `std::sqrt`, contained in `cmath` and `cstdlib`
* Fortran : `rand` `srand` and `sqrt`

The Fortran `rand` function already generates a random number between 0 and 1. 
To achieve this in C or C++ you need to write the following function;

```c
double rand_one()
{
    return rand() / (RAND_MAX + 1.0);
}
```

To get a random number from -1 to 1 you need to use;

    (2 * rand()) - 1 or (2 * rand_one()) - 1

Here are the possible answers - take a look if you get stuck or you want to check your work;

* [C](messages_answer_c.md)
* [C++](messages_answer_cpp.md)
* [Fortran](messages_answer_f77.md)

***

[Compare with OpenMP](../beginning_openmp/critical.md)

***

# [Previous](loops.md) [Up](README.md) [Next](reduction.md)
