# Part 1: How to vectorise? (omp simd)

So, how can you vectorise your code? In order of difficulty, your 
options are;

1. Easiest is to use numerical libraries, such as BLAS or Intel's math kernel library (mkl),
   as these are already fully vectorised. It is significantly easier to use
   other people's hard work than to reinvent and revectorise the wheel yourself...

2. Ask the compiler to vectorise your code for you. Compilers can automatically
   vectorise simple code, and top of the range compilers can automatically 
   vectorise simple code. For example, recompile `loop.cpp` using 
   `-O3` rather than `-O2`. You should see that the standard loop now runs 
   as quickly as the vectorised loop. This is because GCC is sufficiently
   clever that it can see that the simple standard loop can be vectorised,
   and it has automatically done this for you. Some compilers, e.g. the Intel compiler,
   can even print out a report to tell you when it auto-vectorises a loop,
   or how you can help it to auto-vectorise loops. However, like auto-parallelisation,
   auto-vectorisation has limits, and the compiler can't do it all for you,
   especially if your code is very object-orientated (you use lots of 
   your own classes and objects).

3. Use OpenMP 4.0 SIMD instructions to advise the compiler how to vectorise
   your code. This is the subject of the rest of the first part of this
   workshop, and you will learn how to do this below.

4. Use vector intrinsics to work directly with vectors in C++ in the same way that
   you work with floats or doubles. You will learn how to do this in the
   second part of this workshop.

## OpenMP SIMD

If the compiler won't auto-vectorise, and you can't use a vectorised library,
then the next best way to vectorise your code is to use OpenMP. 
OpenMP provides a set of compiler directives that are used to provide extra information
to a compiler to allow it to automatically parallelise and/or vectorise code (typically loops).
These are built into the compiler and accessed by using pragmas (via `#pragma`).
Pragmas are hints that the compiler can choose to use or ignore, depending on
whether it has built-in support for that capability. For example, `#pragma omp parallel`
accesses the set of OpenMP parallel directives, with `#pragma omp parallel for` 
instructing the compiler to consider parallelising the attached loop. If you want,
you can learn more about OpenMP in my [../beginning_openmp](OpenMP course).

Recently, it was recognised that the ideas behind OpenMP are just as useful
to help compilers automatically vectorise code (again, typically loops).
OpenMP 4.0 introduced `omp simd`, accessed via `#pragma omp simd` 
as a standard set of hints that can be
given to a compiler to encourage it to autovectorise code. You have already
seen `omp simd` in use. The addition of `#pragma omp simd` above a loop
is an OpenMP SIMD directive that tells the compiler that it should consider 
vectorising that loop.

* Note that `omp parallel` and `omp simd` are completely separate. You don't need to
use both in your program. It is completely acceptable to vectorise using
`omp simd`, and parallelise using, e.g. [Intel threading building blocks](../parallel_c++).
It is also acceptable to parallelise using `omp parallel` and vectorise using vector intrinsics.

* Note also that you do not need to know `omp parallel` to use `omp simd`. Also
note that, like `omp parallel`, `omp simd` is usable in C and Fortran, as well
as C++. This workshop will only look at `omp simd` in C++.

* Finally, note that `omp simd` is relatively new, and so you need to use
later versions of GCC, CLANG or the Intel C++ compiler to use it. Older compilers
will still compile your code with `omp simd`, but they will ignore the
directives as they don't have `omp simd` support.

***

# Exercise

Edit `loop.cpp` and use `omp simd` to vectorise the standard loop. Check that
the newly-vectorised standard loop now runs at the same speed as the vectorised
loop.

For GCC, `omp simd` vectorisation is supported via the `-fopenmp-simd` compiler flag.
For CLANG, `omp simd` vectorisation is supported via the `-openmp-simd` compiler flag.
Try recompiling `loop.cpp` without this flag, i.e.

```
g++ -O2 --std=c++14 -Iinclude loop.cpp -o loop
```

How fast do the two loops run now? Does this mean that `#pragma omp simd` has been ignored?

***

# [Previous](vectorisation.md) [Up](README.md) [Next](features.md)
