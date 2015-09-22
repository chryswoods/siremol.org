#Beginning MPI

MPI provides a straight-forward interface to write software that can use 
multiple cores of a computer, and multiple computers in a cluster or nodes 
in a supercomputer. Using MPI you can write code that uses all of the cores 
and all of the nodes in a multicore computer cluster, and that will run 
faster as more cores and more compute nodes become available.

MPI is a well-established, standard method of writing parallel programs. 
It was first released in 1992, and is currently on version 2. MPI is 
implemented as a library, which is available for nearly all computer platforms 
(e.g. Linux, Windows, OS X), and with interfaces for many popular languages 
(e.g. C, C++, Fortran, Python).

MPI stands for "Message Passing Interface", and it parallelises computational 
work by providing tools that let you use a team of processes to solve the problem, 
and for the team to then share the solution by passing messages amongst one 
another. MPI can be used to parallelise programs that run locally, by having 
all processes in the team run locally, or it can be used to parallelise programs 
across a compute cluster, by running one or more processes per node. MPI can 
be combined with other parallel programming technologies, e.g. OpenMP. This 
course is presented as a companion to my [OpenMP course](../beginning_openmp/README.md), 
with both this and the OpenMP course following a similar structure and presenting 
similar examples. If you want to compare MPI and OpenMP, then please click on the 
[Compare with OpenMP](../beginning_openmp/README.md) links on each page.

You can read about the history of MPI at its 
[Wikipedia page](http://en.wikipedia.org/wiki/Message_Passing_Interface), 
or by going to one of the
[many](http://www.mpi-forum.org/) 
[MPI](https://computing.llnl.gov/tutorials/mpi/) 
[websites](http://www.mcs.anl.gov/research/projects/mpi/tutorial/). 
The best book to learn MPI in my opinion is 
[Using MPI: Portable Parallel Programming with the Message-Passing Interface](http://www.amazon.co.uk/Using-MPI-Programming-Message-Passing-Engineering/dp/0262571323/ref=sr_1_3?ie=UTF8&qid=1329953725&sr=8-3) 
(I used it to learn MPI).

This is a short course that will provide a taster of MPI. MPI is a large 
library, and this course presents just a taster. The course is arranged with 
examples in C, C++ and Fortran. Feel free to look at just the language you
are familiar with, or, if you are interested, feel free to compare MPI use 
in each of the languages. Please also feel free to work through this course 
at your own pace. MPI is best learned by using it, so please copy out and 
play with the examples provided, and also have a go at the exercises.

***

* [Basics](basics.md)
* [MPI Functions](functions.md)
* [Sections](sections.md)
* [Loops](loops.md)
* [Messages](messages.md)
* [Reduction](reduction.md)
* [Map/Reduce](mapreduce.md)
* [Maximising Performance](performance.md)
* [What Next?](whatnext.md)

***

# [Previous](../main/courses.md) [Up](../main/courses.md) [Next](basics.md) 
