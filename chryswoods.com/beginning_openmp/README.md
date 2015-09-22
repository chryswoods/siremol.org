#Beginning OpenMP

OpenMP provides a straight-forward interface to write software that can use 
multiple cores of a computer. Using OpenMP you can write code that uses all 
of the cores in a multicore computer, and that will run faster as more cores 
become available.

OpenMP is a well-established, standard method of writing parallel programs. 
It was first released in 1997, and is currently on version 3.0. It is provided 
by default in nearly all compilers, e.g. the gnu compiler suite (gcc, g++, gfortran), 
the Intel compilers (icc, icpc, ifort) and the Portland Group compilers 
(pgc, pgCC, pgf77) and works on nearly all operating systems (e.g. Linux, Windows and OS X).

You can read about the history of OpenMP at its 
[Wikipedia page](http://en.wikipedia.org/wiki/OpenMP), 
or by going to one of the 
[many](http://www.openmp.org/)
[OpenMP](http://www.nersc.gov/nusers/help/tutorials/openmp/)
[websites](http://www.compunity.org/). 
The best book to learn OpenMP in my opinion is 
[Using OpenMP: Portable Shared Memory Parallel Programming](http://www.amazon.co.uk/Using-OpenMP-Programming-Computation-Engineering/dp/0262533022/ref=sr_1_1?ie=UTF8&s=books&qid=1256806054&sr=8-1)
(I used it to learn OpenMP).

OpenMP can be combined with other parallel programming technologies, e.g. MPI. 
This course is presented as a companion to my [MPI course](../beginning_mpi/README.md), 
with both this and the MPI course following a similar structure and 
presenting similar examples. If you want to compare OpenMP and MPI, 
then please click on the [Compare with MPI](../beginning_mpi/README.md) links on each page.

This is a short course that will provide a taster of OpenMP. The course is arranged 
with examples in C, C++ and Fortran. Feel free to look at just the language you 
are familiar with, or, if you are interested, feel free to compare OpenMP use 
in each of the languages. Please also feel free to work through this course at 
your own pace. OpenMP is best learned by using it, so please copy out and play 
with the examples provided, and also have a go at the exercises.

***

* [Basics](basics.md)
* [Compiler Directives / Pragmas](directives.md)
* [Sections](sections.md)
* [Loops](loops.md)
* [Critical Code](critical.md)
* [Reduction](reduction.md)
* [Map/Reduce](mapreduce.md)
* [Maximising Performance](performance.md)
* [Case Study](casestudy.md)
* [What Next?](whatnext.md)

***

# [Previous](../main/courses.md) [Up](../main/courses.md) [Next](basics.md) 
