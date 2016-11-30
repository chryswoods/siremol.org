# Part 2: Portable Intrinsics

Using intrinsics while retaining code portability can be challenging. The way
I prefer to do it is to create a C++ class that represents a vector, and that
provides a thin wrapper around the intrinsic data and functions.

For example, `include/floatvec.h` contains a simple `FloatVec` class that 
defines a single vector of floats. The interface to the `FloatVec` class
is the same regardless of whether SSE2, AVX or another vectorisation scheme
is used. It is only the implementation that changes. For example, the start
of the class is as follows;

```c++
/** A simple class that provides a portable, optimised
    vector of floats
*/
class FloatVec
{
private:
    #ifdef __AVX__
        // if we have AVX, then we have a 8xfloat vector
        __m256 v;
        #define FLOATVEC_SIZE 8
    #else
    #ifdef __SSE2__
        // if we have SSE2, then we have a 4xfloat vector
        __m128 v;
        #define FLOATVEC_SIZE 4
    #else
        // in the general case, we will create a float array of 
        // size 8 (we can choose whatever size we want)
        float v[8];
        #define FLOATVEC_SIZE 8
    #endif
    #endif
```

If AVX is available, then the `#ifdef __AVX__` is true, and so the `FloatVec`
class has a single member variable called `v`, which is of type `__m256`.

If AVX isn't available, but SSE2 is, then `#ifdef __SSE2__` is true. This means
that now `FloatVec` contains a single member variable valled `v`, which is of
type `__m128`. 

If neither AVX nor SSE2 are available, then `FloatVec` contains a single
member varable called `v`, which is an array of eight floats.

The interface to `FloatVec` provides some useful functions;

* `FloatVec::Array FloatVec::fromArray( workshop::Array<float> x )` : This function 
automatically converts from an array of floating point numbers to an
array of `FloatVec` vectors. This simplifies loading data into the vector.

* `workshop::Array<float> FloatVec::toArray( FloatVec::Array x )` : This function
automatically converts back from an array of `FloatVec` vectors to an array
of floats. This simplifies reading data back from the vector.

* `FloatVec FloatVec::operator+(FloatVec v) const` : This function is used to 
add one vector to another.

The last function is worth looking at deeper, as it shows how `#ifdef` guards
are used to provide a different implementation depending on whether AVX, SSE2
or something else is available.

```c++
/** Add two vectors together */
inline FloatVec FloatVec::operator+(const FloatVec &other) const
{
    #ifdef __AVX__
        return FloatVec( _mm256_add_ps(v, other.v) );
    #else
    #ifdef __SSE2__
        return FloatVec( _mm_add_ps(v, other.v) );
    #else
        FloatVec result;

        #pragma omp simd
        for (int i=0; i<size(); ++i)
        {
            result.v[i] = v[i] + other.v[i];
        }

        return result;
    #endif
    #endif
}
```

The first thing to note is that this function is declared `inline`, meaning that 
it is automatically expanded by the compiler, with the function call replaced
by the code within the function at compile time. This is to ensure that
we don't suffer any penalties from calling a function.

Next, we have three implementations;

* If AVX is available, we simply return a `FloatVec` which is constructed
from the result of `_mm256_add_ps(v, other.v)`.
* Otherwise, if SSE2 is available, we simple return a `FloatVec` which is constructed
from the result of `_mm_add_ps(v, other.v)`.
* Otherwise, we manually perform the addition in a short loop. We've added
`#pragma omp simd` to this loop in case the compiler is able to vectorise this
loop (which should be doable, as this is a very simple loop!)

## Using `FloatVec` to abstract vector instrinsics

Now we will use `FloatVec` to vectorise the `loop.cpp` example that
we have been using throughout the workshop. Create a new file called `portable.cpp`
and copy into it;

```c++
#include "workshop.h"
#include "floatvec.h"

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

    auto vec_a = FloatVec::fromArray(a);
    auto vec_b = FloatVec::fromArray(b);
    auto vec_c = FloatVec::fromArray(c);

    const int vec_size = vec_a.size();

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
        for (int i=0; i<vec_size; ++i)
        {
            vec_c[i] = vec_a[i] + vec_b[i];
        }
    }

    std::cout << "c = ";

    for (int i=0; i<c.size(); ++i)
    {
        std::cout << c[i] << " ";
    }

    std::cout << std::endl;

    c = FloatVec::toArray(vec_c);

    std::cout << "vec_c = ";

    for (int i=0; i<c.size(); ++i)
    {
        std::cout << c[i] << " ";
    }

    std::cout << std::endl;

    auto vector_duration = workshop::get_duration(timer);

    std::cout << "The standard loop took " << duration
              << " microseconds to complete." << std::endl;

    std::cout << "The vectorised loop took " << vector_duration
              << " microseconds to complete." << std::endl;

    return 0;
}
```

We will compile this for AVX, SSE and omp simd using;

```
g++ -O2 -msse2 --std=c++14 -Iinclude portable.cpp -o sse_portable
g++ -O2 -mavx --std=c++14 -Iinclude portable.cpp -o avx_portable
g++ -O2 -fopenmp-simd --std=c++14 -Iinclude portable.cpp -o omp_portable
```

Run the three executables and compare their speed, using;

```
./sse_portable
./avx_portable
./omp_portable
```

Note that, in this example, we have printed out the value of `c` and `vec_c`
so that you can see that the results are all the same.

On my computer I find that the standard loop takes about 32 ms to run.

* The vectorised loop for the AVX code takes about 4.5 ms to run (7.1 times faster)
* The vectorised loop for the SSE2 code takes about 8.0 ms to run (4.0 times faster)
* The vectorised loop using omp simd takes about 8.0 ms to run (4.0 times faster)

# Exercises

* Edit `include/floatvec.h` to add in equivalent functions for `operator-`, 
`operator*` and `operator/`. Change `portable.cpp` so that you can compare
the speed of scalar and vector loops using addition, subtraction, multiplication
and division.

* Take a look at the `sqrt` function that is defined in `include/floatvec.h`. 
Edit `portable.cpp` so that you can compare scalar square root versus vector
square root, i.e. `std::sqrt(a[i] + b[i])` versus `sqrt(vec_a[i] + vec_b[i])`.

* The current version of `toArray` and `fromArray` assume that the size of the
array is an exact multiple of the size of the vector. What do you think you should
do if the array is not an exact multiple? Could you edit `fromArray` and `toArray`
to implement your chosen solution.

***

# [Previous](immintrin.md) [Up](part2.md) [Next](whatnext.md)
