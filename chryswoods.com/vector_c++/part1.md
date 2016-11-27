# Part 1: Introduction to Vectorisation

So, what is vectorisation? (or vectorization for everyone outside the UK?) 
To answer this, let's look at a simple example. Open a text editor (i.e. nano) to create
a C++ source file called `loop.cpp` and copy in the code below;

```c++
#include "workshop.h"

int main(int argc, char **argv)
{
    const int size = 512;

    auto a = workshop::Array<float>(size);
    auto b = workshop::Array<float>(size);
    auto c = workshop::Array<float>(size);

    for (int i=0; i<size; ++i)
    {
        a[i] = 1.0*(i+1);
        b[i] = 2.5*(i+1);
        c[i] = 0.0;
    }

    auto timer = workshop::start_timer();

    for (int j=0; j<100000; ++j)
    {
        for (int i=0; i<size; ++i)
        {
            c[i] = a[i] + b[i];
        }
    }

    auto duration = workshop::get_duration(timer);

    timer = workshop::start_timer();

    for (int j=0; j<100000; ++j)
    {    
        #pragma omp simd
        for (int i=0; i<size; ++i)
        {
            c[i] = a[i] + b[i];
        }
    }

    auto vector_duration = workshop::get_duration(timer);

    std::cout << "The standard loop took " << duration
              << " microseconds to complete." << std::endl;

    std::cout << "The vectorised loop took " << vector_duration
              << " microseconds to complete." << std::endl;

    return 0;
}
```

Compile and run the program using

```
g++ -O2 --std=c++14 -fopenmp-simd loop.cpp -Iinclude -o loop
./loop
```

(note that you need to use `-openmp-simd` instead of `-fopenmp-simd` if
you are using clang or are using a Mac)

You should see output similar to this

```
The standard loop took 31884.2 microseconds to complete.
The vectorised loop took 7937.6 microseconds to complete.
```

(note that your computer will take a different amount of time to run both loops,
but you should see that the vectorised loop completes much more quickly
than the standard loop)

This was a very simple program that compared a standard loop with
a vectorised loop. The program has three main parts;

## (1) Initialising the data for the calculation

```c++
#include "workshop.h"

int main(int argc, char **argv)
{
    const int size = 512;

    auto a = workshop::Array<float>(size);
    auto b = workshop::Array<float>(size);
    auto c = workshop::Array<float>(size);

    for (int i=0; i<size; ++i)
    {
        a[i] = 1.0*(i+1);
        b[i] = 2.5*(i+1);
        c[i] = 0.0;
    }
```

This first part sets up the program. It includes `workshop.h`, which is a header provided with
this workshop that is in the directory `include`. This header file includes a variety of headers,
such as `<chrono>` and `<iostream>`, and adds some basic functions that make it easier to write these examples.

After this, three `workshop::Array` arrays are created, `a`, `b` and `c`. These are initialised
with some starting values.

## (2) Performing the standard loop

```c++
    auto timer = workshop::start_timer();

    for (int j=0; j<100000; ++j)
    {
        for (int i=0; i<size; ++i)
        {
            c[i] = a[i] + b[i];
        }
    }

    auto duration = workshop::get_duration(timer);
```

This part of the program performs a simple loop, which just adds `a` and `b` together, 
setting `c[i]` equal to the sum of `a[i]` and `b[i]`.

This is timed using a timer that is started using the function
`workshop::start_timer()`, and measured using `workshop::get_duration(timer)`.

Note that because computers are *really* fast, we have repeated the 
calculation 100,000 times, so that it is possible to measure accurately.

On my computer, 100,000 repeats of this calculation took 32,000 microseconds
(32 milliseconds), meaning that each calculation of `a` plus `b` took
only 0.3 microseconds (300 nanoseconds). As `a` and `b` are both arrays with
512 values, this means that 512 additions were performed in 300 nanoseconds.
Each addition therefore took 0.6 nanoseconds, meaning the program was performing
the calculation at a rate of 1.7 billion floating point additions per second. An addition
is an example of a FLoating Point OPeration (a FLOP), so this means that this
calculation ran at a speed of 1.7 gigaflops (GFLOPs).

## (3) Performing the vectorised loop

```c++
    timer = workshop::start_timer();

    for (int j=0; j<100000; ++j)
    {
        #pragma omp simd
        for (int i=0; i<size; ++i)
        {
            c[i] = a[i] + b[i];
        }
    }

    auto vector_duration = workshop::get_duration(timer);
```

This part of the program performs the vectorised loop. This is identical to 
the last part (the standard loop), except now we have added

```c++
#pragma omp simd
```

above the loop that calculates `a` plus `b`. This line is a command that
is given to the compiler that tells it to vectorise the loop. What this means,
and how it works, will be explained later.

With this `pragma omp simd`, the loop is vectorised, and the calculation
runs much more quickly. On my computer, 100,000 repeats of the vectorised
loop took about 8,000 microseconds (8 milliseconds), meaning that each
calculation of `a` plus `b` took 0.08 microseconds (80 nanoseconds). This
means that each of the 512 additions needed to calculate `a` plus `b` took
0.15 nanoseconds, so the calculation ran at a speed of 6.7 GFLOPs.
This is approximately four times faster than the standard, non-vectorised
loop.

***

# Exercise

* Work out the speed of the standard loop and vectorised loop in GFLOPs for
your computer. How much faster is the vectorised loop compared to the standard loop?

* Edit `loop.cpp` and change it so that it compares a standard multiplication
with a vectorised multiplication (i.e. change `c[i] = a[i] + b[i];` to
`c[i] = a[i] * b[i];`. Work out the speed in GFLOPs for both loops. Is this
similar to the speed for addition? Is the vector speed up for multiplication 
similar to that for addition?

* Next, edit `loop.cpp` to compare standard division versus vectorised division
(`c[i] = a[i] / b[i];`). Work out the speed in GFLOPs for both loops. 
Is this similar to the speed for addition? How does the speed and vector speed-up
of division compare to addition or multiplication?

* Finally, edit `loop.cpp` to change the size of the arrays (edit the 
`size` variable). Does changing the size affect the speed of the two 
loops in GFLOPs? Does changing the size affect the speedup of the vectorised
loop versus the unvectorised loop? Good sizes to try are 1, 2, 4, 128, 256
and 4096.

***

# [Previous](README.md) [Up](README.md) [Next](vectorisation.md)
