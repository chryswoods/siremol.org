
# Part 2: SSE Intrinsics

The intrinsics for SSE (specifically SSE2) are provided in the header
file `emmintrin.h`, which your compiler will automatically provide
if it supports compiling code with SSE2. If your compiler supports
SSE2, then the macro `__SSE2__` will be set, meaning that you can
include this header file using;

```c++
#ifdef __SSE2__
  #include <emmintrin.h>
#else
  #warning SSE2 is not available. Code will not compile!
#endif
```

For some compilers, you may need to pass a complier flag to switch on
the use of SSE2. For example, gcc and clang use the flag `-msse2`

Different header files are used for the other versions of SSE. However,
for most numerical work, SSE2 is the version you want to use, and it
is now widely supported on pretty much any X86- or X86-64-compatible 
processor that you will use.

The `emmintrin.h` header file defines a set of data types that represent
different types of vectors. These are;

* `__m128` : This is a vector of four floating point numbers (4x32 = 128 bits)
* `__m128d` : This is a vector of two double precistion numbers (2x64 = 128 bits)

Several functions are defined that operate on `__m128` vectors, e.g.

* `_mm_set1_ps(float a)` : This returns a `__m128` vector, where all four elements of the 
vector are set equal to `a`, i.e. the vector is `[a,a,a,a]`.
* `_mm_set_ps(float d, float c, float b, float a)` : This returns a `__m128` vector
where the four elements are set equal to the four passed floats, i.e. `[a,b,c,d]`. Note
that the load is backwards, i.e. the first element of the vector is the last variable
passed to the function. 
* `_mm_add_ps(__m128 a, __m128 b)` : This returns a `__m128` vector where each of the 
four elements are set equal to the sum of `a` and `b`, i.e. `[ a[0]+b[0], a[1]+b[1], a[2]+b[2], a[3]+b[3] ]`.
* `_mm_sub_ps(__m128 a, __m128 b)` : This returns a `__m128` vector where each of the
four elements are set equal to the difference of `a` and `b`, i.e.
`[ a[0]-b[0], a[1]-b[1], a[2]-b[2], a[3]-b[3] ]`.
* `_mm_mul_ps(__m128 a, __m128 b)` : This returns a `__m128` vector where each of the
four elements are set equal to the product of `a` and `b`, i.e.
`[ a[0]*b[0], a[1]*b[1], a[2]*b[2], a[3]*b[3] ]`.
* `_mm_div_ps(__m128 a, __m128 b)` : This returns a `__m128` vector where each of the 
four elements are set equal to the ratio of `a` and `b`, i.e. 
`[ a[0]/b[0], a[1]/b[1], a[2]/b[2], a[3]/b[3] ]`.
* `_mm_sqrt_ps(__m128 a)` : This returns a `__m128` vector where each of the four
elements are set equal to the square root of `a`, i.e.
`[ sqrt(a[0]), sqrt(a[1]), sqrt(a[2]), sqrt(a[3]) ]`.
* `float b[4]; _mm_storeu_ps(__m128 a)` : This will copy the data from the `__m128` vector
`a` into a float array `b`, where `b[0]` will equal `a[0]`, `b[1]` will equal `a[1]` etc.

In addition to functions that operate on `__m128` float vectors, there are equivalent
functions that operate on `__m128d` double vectors. The functions are named similarly
to the float vector functions, except `_ps` (which stands for "packed single") is replaced
by `_pd` (which stands for "packed double"). For example;

* `_mm_set1_pd(double a)` : This returns a `__m128d` vector, where both elements of the 
vector are set equal to `a`, i.e. the vector is `[a,a]`.
* `_mm_set_pd(double b, double a)` : This returns a `__m128d` vector
where both elements are set equal to the two passed floats, i.e. `[a,b]`. Note
that the load is backwards, i.e. the first element of the vector is the last variable
passed to the function. 
* `_mm_add_pd(__m128d a, __m128d b)` : This returns a `__m128d` vector where each of the 
elements are set equal to the sum of `a` and `b`, i.e. `[ a[0]+b[0], a[1]+b[1] ]`.
* `_mm_sub_pd(__m128d a, __m128d b)` : This returns a `__m128d` vector where each of the
elements are set equal to the difference of `a` and `b`, i.e.
`[ a[0]-b[0], a[1]-b[1] ]`.
* `_mm_mul_pd(__m128d a, __m128d b)` : This returns a `__m128d` vector where each of the
elements are set equal to the product of `a` and `b`, i.e.
`[ a[0]*b[0], a[1]*b[1] ]`.
* `_mm_div_pd(__m128d a, __m128d b)` : This returns a `__m128d` vector where each of the 
elements are set equal to the ratio of `a` and `b`, i.e. 
`[ a[0]/b[0], a[1]/b[1] ]`.
* `_mm_sqrt_pd(__m128d a)` : This returns a `__m128d` vector where each of the
elements are set equal to the square root of `a`, i.e.
`[ sqrt(a[0]), sqrt(a[1]) ]`.
* `double b[2]; _mm_storeu_pd(__m128d a)` : This will copy the data from the `__m128d` vector
`a` into a double array `b`, where `b[0]` will equal `a[0]` and `b[1]` will equal `a[1]`.

The above is a lot of information. Let's now try a simple program that creates two
`__m128` vectors and calculates their sum. Create a new file called `sse.cpp` and 
copy into it;

```c++
#include <iostream>

#ifdef __SSE2__
  #include <emmintrin.h>
#else
  #warning SSE2 support is not available. Code will not compile
#endif

int main(int argc, char **argv)
{
    __m128 a = _mm_set_ps(4.0, 3.0, 2.0, 1.0);
    __m128 b = _mm_set_ps(8.0, 7.0, 6.0, 5.0);

    __m128 c = _mm_add_ps(a, b);

    float d[4];
    _mm_storeu_ps(d, c);

    std::cout << "result equals " << d[0] << "," << d[1]
              << "," << d[2] << "," << d[3] << std::endl;

    return 0;
}
```

Compile and run using

```
g++ -O2 -msse2 --std=c++14 sse.cpp -o sse
./sse
```

(note the addition of `-msse2` to switch on SSE2 support. Some compilers
now do this automatically, but it is still worth adding).

You should see output

```
result equals 6,8,10,12
```

This is because we have loaded `[1,2,3,4]` into `a` and `[5,6,7,8]` into `b`. 
We calculated the sum, which is `[6,8,10,12]`, which was then printed out.

Try editing `sse.cpp` to use the other arithmetic functions (i.e. `_mm_mul_ps`).
Is the result what you expect?

## Manually vectorising a loop

Now you know how to create and use SSE2 intrinsics, the next step is to use
them to vectorise code. We will look here at vectorising the `loop.cpp` file
that we first met in [part 1](part1.md).

Create a new file called `sseloop.cpp` and copy into it the below;

```c++
#include "workshop.h"

#ifdef __SSE2__
  #include <emmintrin.h>
#else
  #warning SSE2 support is not available. Code will not compile.
#endif

int main(int argc, char **argv)
{
    const int size = 512;

    auto a = workshop::Array<float>(size);
    auto b = workshop::Array<float>(size);
    auto c = workshop::Array<float>(size);

    auto sse_a = workshop::AlignedArray<__m128>(size/4);
    auto sse_b = workshop::AlignedArray<__m128>(size/4);
    auto sse_c = workshop::AlignedArray<__m128>(size/4);


    for (int i=0; i<size; ++i)
    {
        a[i] = 1.0*(i+1);
        b[i] = 2.5*(i+1);
        c[i] = 0.0;
    }

    for (int i=0; i<size; i+=4)
    {
        sse_a[i/4] = _mm_set_ps(1.0*(i+3+1),
                                1.0*(i+2+1),
                                1.0*(i+1+1),
                                1.0*(i+0+1));

        sse_b[i/4] = _mm_set_ps(2.5*(i+3+1),
                                2.5*(i+2+1),
                                2.5*(i+1+1),
                                2.5*(i+0+1));

        sse_c[i/4] = _mm_set1_ps(0.0);
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
        for (int i=0; i<size/4; ++i)
        {
            sse_c[i] = _mm_add_ps(sse_a[i], sse_b[i]);
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

Compile and run using

```
g++ -msse2 -O2 --std=c++14 -Iinclude sseloop.cpp -o sseloop
./sseloop
```

You should see that the manually vectorised loop is nearly four times faster than
the scalar loop. On my computer, the vector loop is about 3.8 times faster than the 
scalar loop, taking 12.4 ms versus 47.6 ms.

To manually vectorise the loop, we have had to make some changes to the code;

* We had to create SSE versions of `a`, `b` and `c`, which we called `sse_a`, `sse_b` and `sse_c`.
These were declared as aligned arrays of `__m128` vectors, with the array containing
`size/4` elements (as each vector holds four floats).
* We had to populate `sse_a` and `sse_b` using the `_mm_set_ps` function.
* We had to initialise `sse_c` to zero using the `_mm_set1_ps` function.
* The vectorised loop performs `size/4` iterations, as each iteration performs four additions.
* We had to use `_mm_add_ps` to add `sse_a` and `sse_b` together.

Note that the number of iterations of our loop (512) was evenly divisable by 4. If this
was not the case, we would have had to manually add additional scalar iterations of the loop to
make up any shortfall. For example, if our loop used 514 iterations, then 512 could be
performed using the vector loop, and then code would need to be added to perform 
the remaining 2 iterations using a scalar loop.

# Exercises

* Edit `sseloop.cpp` so that you can compare scalar multiplication against manually
vectorised multiplication (e.g. change `c[i] = a[i] + b[i]` to `c[i] = a[i] * b[i]`, and
change `sse_c[i] = _mm_add_ps(sse_a[i],sse_b[i])` to `sse_c[i] = _mm_mul_ps(sse_a[i],sse_b[i])`.
Recompile and rerun. Do you see a similar four-times speed up as for addition?

* Edit `sseloop.cpp` and now compare scalar division against manually vectorised division.
Do you see a similar four-times speed-up as for addition, and what is the total speed of the loop
compared to addition?

* Finally, edit `sseloop.cpp` to compare scalar square root versus manually vectorised
square root. Do this by changing `c[i] = a[i] + b[i]` to `c[i] = std::sqrt(a[i] + b[i])`, and
changing `sse_c[i] = _mm_add_ps(sse_a[i],sse_b[i])` to 
`sse_c[i] = _mm_sqrt_ps(_mm_add_ps(sse_a[i],sse_b[i]))`. If you need help making this
change, the please [look here](emmintrin_answer.md).
Recompile and rerun. What is the
speed up for vectorised square root versus scalar square root?

Hopefully, you should see the (perhaps surprising) result that vector square root is 
significantly faster than scalar square root. On my computer, scalar square root takes
about 211 ms, while vector square root takes 13.5 ms. This is about a 15 times speed up,
which goes beyond the normal four times speed up associated with vectorisation. The reason
is that SSE2 has an implementation of square root that is built directly into the processor.
This hardware square root is exceptionally fast, and much faster than the scalar square root
that is implemented in software. In addition, this hardware square root is an actual processor
instruction rather than a function call, meaning that there are no overheads. Indeed,
it is that fast that adding in the square root has barely increased the cost of the loop
compared to the simple addition.

This shows that if your code uses a lot of square roots, you can get a big performance
boost by using manual vectorisation with SSE2 intrinsics.

***

# [Previous](part2.md) [Up](part2.md) [Next](immintrin.md)
