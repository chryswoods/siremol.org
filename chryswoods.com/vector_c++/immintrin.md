# Part 2: AVX Intrinsics

The AVX intrinsics are very similar to the SSE2 intrinsics, and follow
a similar naming convention. The intrinsics for AVX are defined in the
header file `immintrin.h`, which is available if your compiler supports
writing AVX code, as indicated by the `__AVX__` macro.

```c++
#ifdef __AVX__
  #include <immintrin.h>
#else
  #warning AVX is not available. Code will not compile!
#endif
```

You will need to pass a flag to your compiler to switch on AVX support.
For GCC and clang the flag is `-mavx`. This is needed as code compiled with
AVX support with not run on processors that don't support AVX (the program
will just crash with an "unsupported" or "invalid instruction" error).

The `immintrin.h` header file defines a set of data types that represent
different types of vectors. These are;

* `__m256` : This is a vector of eight floating point numbers (8x32 = 256 bits)
* `__m256d` : This is a vector of four double precistion numbers (4x64 = 256 bits)

Several functions are defined that operate on `__m256` vectors, e.g.

* `_mm256_set1_ps(float a)` : This returns a `__m256` vector, where all eight elements of the 
vector are set equal to `a`, i.e. the vector is `[a,a,a,a,a,a,a,a]`.
* `_mm256_set_ps(float h, float g, float f, float e, float d, float c, float b, float a)` : 
This returns a `__m256` vector
where the eight elements are set equal to the eight passed floats, i.e. `[a,b,c,d,e,f,g,h]`. Note
that the load is backwards, i.e. the first element of the vector is the last variable
passed to the function. 
* `_mm256_add_ps(__m256 a, __m256 b)` : This returns a `__mm256` vector where each of the 
elements are set equal to the sum of `a` and `b`, i.e. 
`[ a[0]+b[0], a[1]+b[1], a[2]+b[2], a[3]+b[3], a[4]+b[4], a[5]+b[5], a[6]+b[6], a[7]+b[7] ]`.
* `_mm256_sub_ps(__m256 a, __m256 b)` : This returns a `__m256` vector where each of the
elements are set equal to the difference of `a` and `b`.
* `_mm256_mul_ps(__m256 a, __m256 b)` : This returns a `__m256` vector where each of the
elements are set equal to the product of `a` and `b`.
* `_mm256_div_ps(__m256 a, __m256 b)` : This returns a `__m256` vector where each of the 
elements are set equal to the ratio of `a` and `b`. 
* `_mm256_sqrt_ps(__m256 a)` : This returns a `__m256` vector where each of the
elements are set equal to the square root of `a`.
* `float b[8]; _mm256_storeu_ps(__m256 a)` : This will copy the data from the `__m256` vector
`a` into a float array `b`, where `b[0]` will equal `a[0]`, `b[1]` will equal `a[1]` etc.

In addition to functions that operate on `__m256` float vectors, there are equivalent
functions that operate on `__m256d` double vectors. The functions are named similarly
to the float vector functions, except `_ps` (which stands for "packed single") is replaced
by `_pd` (which stands for "packed double"). For example;

* `_mm256_set1_pd(double a)` : This returns a `__m256d` vector, where the elements of the 
vector are set equal to `a`, i.e. the vector is `[a,a,a,a]`.
* `_mm256_set_pd(double d, double c, double b, double a)` : This returns a `__m256d` vector
where the elements are set equal to the passed floats, i.e. `[a,b,c,d]`. Note
that the load is backwards, i.e. the first element of the vector is the last variable
passed to the function. 
* `_mm256_add_pd(__m256d a, __m256d b)` : This returns a `__m256d` vector where each of the 
elements are set equal to the sum of `a` and `b`, 
i.e. `[ a[0]+b[0], a[1]+b[1], a[2]+b[2], a[3]+b[3] ]`.
* `_mm256_sub_pd(__m256d a, __m256d b)` : This returns a `__m256d` vector where each of the
elements are set equal to the difference of `a` and `b`.
* `_mm256_mul_pd(__m256d a, __m256d b)` : This returns a `__m256d` vector where each of the
elements are set equal to the product of `a` and `b`.
* `_mm256_div_pd(__m256d a, __m256d b)` : This returns a `__m256d` vector where each of the 
elements are set equal to the ratio of `a` and `b`.
* `_mm256_sqrt_pd(__m256d a)` : This returns a `__m256d` vector where each of the
elements are set equal to the square root of `a`.
* `double b[4]; _mm256_storeu_pd(__m256d a)` : This will copy the data from the `__m256d` vector
`a` into a double array `b`, where `b[0]` will equal `a[0]`, `b[1]` will equal `a[1]` etc.

The above is a lot of information. Let's now try a simple program that creates two
`__m256` vectors and calculates their sum. Create a new file called `avx.cpp` and 
copy into it;

```c++
#include <iostream>

#ifdef __AVX__
  #include <immintrin.h>
#else
  #warning No AVX support - will not compile
#endif

int main(int argc, char **argv)
{
    __m256 a = _mm256_set_ps(8.0, 7.0, 6.0, 5.0, 
                             4.0, 3.0, 2.0, 1.0);
    __m256 b = _mm256_set_ps(18.0, 17.0, 16.0, 15.0, 
                             14.0, 13.0, 12.0, 11.0);

    __m256 c = _mm256_add_ps(a, b);

    float d[8];
    _mm256_storeu_ps(d, c);

    std::cout << "result equals " << d[0] << "," << d[1]
              << "," << d[2] << "," << d[3] << ","
              << d[4] << "," << d[5] << "," << d[6] << ","
              << d[7] << std::endl;

    return 0;
}
```

Compile and run using

```
g++ --std=c++14 -O2 -mavx avx.cpp -o avx
./avx
```

(note the addition of `-mavx` to switch on AVX support)

You should see output

```
result equals 12,14,16,18,20,22,24,26
```

This is because we have loaded `[1,2,3,4,5,6,7,8]` into `a` and 
`[11,12,13,14,15,16,17,18]` into `b`. We calculated the sum, which is 
`[12,14,16,18,20,22,24,26]`, which was then printed out.

Try editing `avx.cpp` to use the other arithmetic functions (i.e. `_mm256_mul_ps`).
Is the result what you expect?

## Manually vectorising a loop

Now you know how to create and use AVX intrinsics, the next step is to use
them to vectorise code. We will look here at vectorising the `loop.cpp` file
that we first met in [part 1](part1.md).

Create a new file called `avxloop.cpp` and copy into it the below;

```c++
#include "workshop.h"

#ifdef __AVX__
  #include <immintrin.h>
#else
  #warning AVX not supported. Code will not compile
#endif

int main(int argc, char **argv)
{
    const int size = 512;

    auto a = workshop::Array<float>(size);
    auto b = workshop::Array<float>(size);
    auto c = workshop::Array<float>(size);

    auto avx_a = workshop::AlignedArray<__m256>(size/8);
    auto avx_b = workshop::AlignedArray<__m256>(size/8);
    auto avx_c = workshop::AlignedArray<__m256>(size/8);


    for (int i=0; i<size; ++i)
    {
        a[i] = 1.0*(i+1);
        b[i] = 2.5*(i+1);
        c[i] = 0.0;
    }

    for (int i=0; i<size; i+=8)
    {
        avx_a[i/8] = _mm256_set_ps(1.0*(i+7+1),
                                   1.0*(i+6+1),
                                   1.0*(i+5+1),
                                   1.0*(i+4+1),
                                   1.0*(i+3+1),
                                   1.0*(i+2+1),
                                   1.0*(i+1+1),
                                   1.0*(i+0+1));

        avx_b[i/8] = _mm256_set_ps(2.5*(i+7+1),
                                   2.5*(i+6+1),
                                   2.5*(i+5+1),
                                   2.5*(i+4+1),
                                   2.5*(i+3+1),
                                   2.5*(i+2+1),
                                   2.5*(i+1+1),
                                   2.5*(i+0+1));

        avx_c[i/8] = _mm256_set1_ps(0.0);
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
        for (int i=0; i<size/8; ++i)
        {
            avx_c[i] = _mm256_add_ps(avx_a[i], avx_b[i]);
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
g++ -mavx -O2 --std=c++14 -Iinclude avxloop.cpp -o avxloop
./avxloop
```

You should see that the manually vectorised loop is nearly eight times faster than
the scalar loop. On my computer, the vector loop is about 7.9 times faster than the 
scalar loop, taking 6.2 ms versus 49.1 ms.

To manually vectorise the loop, we have had to make some changes to the code;

* We had to create AVX versions of `a`, `b` and `c`, which we called `avx_a`, `avx_b` and `avx_c`.
These were declared as aligned arrays of `__m256` vectors, with the array containing
`size/8` elements (as each vector holds eight floats).
* We had to populate `avx_a` and `avx_b` using the `_mm256_set_ps` function.
* We had to initialise `avx_c` to zero using the `_mm256_set1_ps` function.
* The vectorised loop performs `size/8` iterations, as each iteration performs eight additions.
* We had to use `_mm256_add_ps` to add `avx_a` and `avx_b` together.

Note that the number of iterations of our loop (512) was evenly divisable by 8. If this
was not the case, we would have had to manually add additional scalar iterations of the loop to
make up any shortfall. For example, if our loop used 514 iterations, then 512 could be
performed using the vector loop, and then code would need to be added to perform 
the remaining 2 iterations using a scalar loop.


# Exercises

* Edit `avxloop.cpp` so that you can compare scalar multiplication against manually
vectorised multiplication (e.g. change `c[i] = a[i] + b[i]` to `c[i] = a[i] * b[i]`, and
change `avx_c[i] = _mm256_add_ps(avx_a[i],avx_b[i])` to `avx_c[i] = _mm256_mul_ps(avx_a[i],avx_b[i])`.
Recompile and rerun. Do you see a similar eight-times speed up as for addition?

* Edit `avxloop.cpp` and now compare scalar division against manually vectorised division.
Do you see a similar eight-times speed-up as for addition, and what is the total speed of the loop
compared to addition?

* Finally, edit `avxloop.cpp` to compare scalar square root versus manually vectorised
square root. Do this by changing `c[i] = a[i] + b[i]` to `c[i] = std::sqrt(a[i] + b[i])`, and
changing `avx_c[i] = _mm256_add_ps(avx_a[i],avx_b[i])` to 
`avx_c[i] = _mm256_sqrt_ps(_mm256_add_ps(avx_a[i],avx_b[i]))`. 
If you need help making this
change, the please [look here](immintrin_answer.md).
Recompile and rerun. What is the
speed up for vectorised square root versus scalar square root?

Hopefully, you should see the (perhaps surprising) result that vector square root is 
significantly faster than scalar square root. On my computer, scalar square root takes
about 211 ms, while vector square root takes 11 ms. This is about a 19 times speed up,
which goes beyond the normal eight times speed up associated with vectorisation. The reason
is that, like SSE2, AVX has an implementation of square root that is built directly into the processor.
This hardware square root is exceptionally fast, and much faster than the scalar square root
that is implemented in software. In addition, this hardware square root is an actual processor
instruction rather than a function call, meaning that there are no overheads. However, 
unlike SSE2, the AVX square root does increase the cost of the loop compared to simple
addition (11 ms for square root plus addition, while 6 ms for addition only). Despite
this, AVX square root is still faster than SSE2 square root (11 ms versus 13.5 ms).

This shows that if your code uses a lot of square roots, you can get a big performance
boost by using manual vectorisation with AVX intrinsics.

***

# [Previous](emmintrin.md) [Up](part2.md) [Next](portable.md)
