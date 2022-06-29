
# Efficient Vectorisation with C++

Welcome to a short course that will teach you what vectorisation is, 
and how you can use it to speed up your C++ programs. Learning how
to efficiently vectorise your code is important to allow you to 
make good use of the increasingly large vector units found
on modern multicore and massively multicore processors.

This course will teach you what vectorisation means, and how
it can be achieved at a variety of levels. This will also
discuss why processor manufacturers are increasingly turning
to vectorisation to improve processor speed, and you will
also learn how to lay out the data in your program in memory
to ensure optimal performance. By combinging efficient vectorisation
with parallel programming (i.e. as described in my
[Parallel Programming in C++](../parallel_c++/README.md) course),
you will ensure that your program makes optimal use of modern 
processors such as Xeon and Xeon Phi.

To follow this course you should already have a good basic understanding
of C++, e.g. loops, functions, containers and classes. In addition, this
course will use modern C++ (C++ 2014).

NOTE - this course will assume that you are compiling using the
g++ command, via gcc version 5 or above, or clang version 3.7 or above.
This is available for Windows (e.g. via MSYS2), Linux or OS X. The
course will also assume that you are comfortable using the command
line, and a text editor, such as `nano` or `vim`. 

***

To start, you will need to download all of the course material. This
is available by [clicking here](https://github.com/chryswoods/siremol.org/blob/5208716a0f826ff567748a714d48c193ec98d322/chryswoods.com/vector_c++/workshop.tgz?raw=true). 
This will download a file called
`workshop.tgz`. Unpack this file using the command

```
tar -zxvf workshop.tgz
```

(if you are on windows, type this into an `MSYS2` command shell)

This will unpack a directory called `workshop`. Change into this directory
by typing

```
cd workshop
```

Typing `ls` should show you the following files;

```
include     test.cpp
```

You can test that your compiler is installed and working
by typing on Linux or Windows (MSYS2) with GCC;

```
g++ -O2 --std=c++14 -fopenmp-simd test.cpp -Iinclude -o test
./test
```

or by typing on OS X (or on Linux with clang);

```
g++ -O2 --std=c++14 -openmp-simd test.cpp -Iinclude -o test
./test
```

(GCC uses `-fopenmp-simd` while clang uses `-openmp-simd`)

If this works, you should see output

```
Everything is ok :-)
```

If not, then something went wrong. Double-check your installation of GCC or clang.

***

* [Part 1: Introduction to Vectorisation](part1.md)
    * [What is vectorisation?](vectorisation.md)
    * [How to vectorise? (omp simd)](simd.md)
    * [omp simd features](features.md)
    * [Memory layout](memory.md)
    * [omp simd limitations](limitations.md)
* [Part 2: Vectorisation using intrinsics](part2.md)
    * [SSE intrinsics](emmintrin.md)
    * [AVX intrinsics](immintrin.md)
    * [Portable vectorisation](portable.md)
    * [What next?](whatnext.md)

***

# [Previous](../main/courses.md) [Up](../main/courses.md) [Next](part1.md)  
