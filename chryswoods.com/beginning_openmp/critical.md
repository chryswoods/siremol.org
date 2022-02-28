#Critical Code

Up to this point, the examples have shown how to just run different parts 
of the program in parallel, either by using sections, and running 
different sections using different threads, or using loops, and 
running different iterations of the loop using different threads. 
While this is good, it isn't yet useful. This is because we have not 
yet seen how to make the threads work together on a problem. At the moment, 
each thread works on its own, using its own private variables. 
For example, we've seen how each thread can count the number of iterations 
it performed itself in a loop, but no mechanism has been presented yet that
would allow the team of threads to count up the total number of iterations 
performed by all of them.

What we need is a way to allow the threads to combine their thread private 
copies of variables into a global copy. One method of doing this is to use 
an OpenMP `critical` section. A `critical` section is a part of code that 
is performed by all of the threads in the team, but that is only performed 
by one thread at a time. This allows each thread to update a global variable 
with the local result calculated by that thread, without having to worry 
about another thread trying to update that global variable at the same time. 
To make this clear, use the appropriate link below to create the two executables, 
`broken_loopcount` and `fixed_loopcount`;

* [C](critical_c.md)
* [C++](critical_cpp.md)
* [Fortran](critical_f77.md)

Try running both executables using different values of `OMP_NUM_THREADS`. 
Depending on the compiler, programming language and number of threads, 
`broken_loopcount` may print out a wide range of different outputs. 
Sometimes it will work, and will correctly add the number of iterations 
onto the global sum, and will correctly print out the intermediate 
steps without problem. However, sometimes, completely randomly, it will 
break, and either it will print out nonsense (e.g. it will add 1000 iterations 
to a total of 4000, but the insist that the total is 10000) or it will get 
the total number of iterations completely wrong. The reason for this is that 
while one thread is updating or printing the global total, another thread may be changing it.

The `fixed_loopcount` in contrast will always work, regardless of compiler, 
programming language or number of threads. This is because we've protected 
the update and printing of the global total within an OpenMP `critical` section. 
The `critical` section ensures that only one thread at a time is printing and 
updating the global sum of loops, and so ensures that two threads don't try 
to access `global_nloops` simultaneously.

OpenMP `critical` sections are extremely important if you want to guarantee that 
your program will work reproducibly. Without `critical` sections, random bugs 
can sneak through, and the result of your program may be different if different 
numbers of threads are used.

OpenMP loops plus OpenMP critical sections provide the basis for one of the 
most efficient models of parallel programming, namely map and reduce. The 
idea is that you map the problem to be solved into a loop over a large number 
of iterations. Each iteration solves its own part of the problem and computes 
the result into a local thread-private variable. Once the iteration is 
complete, all of the thread-private variables are combined together (reduced) 
via critical sections to form the final global result.

***

##Exercise

Write an OpenMP parallel program to calculate pi using a Monte Carlo algorithm.

Pi can be calculated using Monte Carlo by imagining a circle with radius 1 sitting 
at the origin within a square that just contains this circle (so with 
corners [-1,-1], [-1,1], [1,-1] and [1,1]). The area of the circle is pi, 
(from pi r squared), while the area of the square is 4. If we imagine throwing 
darts randomly at the square, than the proportion that lie within the circle 
compared to the proportion that lie outside the circle will be directly related 
to the ratio of the area of the circle against the area of the square. In a 
parallel loop, you must thus generate a large number of random points in the square, 
and count up the number that lie within the circle and those that lie outside. 
Reduce these numbers into a global count of the number inside and outside the 
circle, and then finally take the ratio of these numbers to get the value of pi. 
This algorithm to calculate pi is [described in more detail here](https://academo.org/demos/estimating-pi-monte-carlo/).

Note that you will need to use the following random number functions and square root functions;

* C : `rand` and `sqrt`, contained in `math.h` and `stdlib.h`
* C++ : `std::sqrt`, contained in `cmath`
* Fortran : `rand` and `sqrt`

The Fortran `rand` function already generates a random number between 0 and 1. 
To achieve this in C you need to write the following function;

```c
double rand_one()
{
    return rand() / (RAND_MAX + 1.0);
}
```

To get a random number from -1 to 1 you need to use;

    (2 * rand()) - 1 or (2 * rand_one()) - 1

In C++, you can use the standard library random number generators provied by the [`<random>` header](https://en.cppreference.com/w/cpp/header/random).
This provides a `std::random_device` which is used to safely seed the random number generation, `std::default_random_engine` which is used to generate the random numbers, and `std::uniform_real_distribution` which provides those random numbers in a particular range. You can use it by putting, before the `#pragma omp parallel` part:

```c++
std::random_device rd;
```

then, inside the parallel section (so each thread gets their own):

```c++
std::default_random_engine generator(rd());
std::uniform_real_distribution random(-1.0, 1.0);
```

and then extract random numbers using `random(generator)` which will be in the range -1.0 to 1.0.

Here are the possible answers - take a look if you get stuck or you want to check your work;

* [C](critical_answer_c.md)
* [C++](critical_answer_cpp.md)
* [Fortran](critical_answer_f77.md)

***

[Compare with MPI](../beginning_mpi/messages.md)

***

# [Previous](loops.md) [Up](README.md) [Next](reduction.md) 
