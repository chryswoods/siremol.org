
# Part 2: SSE Intrinsics

Then look at intrinsics for SSE.

Create a new file called `sseloop.cpp` and copy into it the below;

```c++
#include "workshop.h"

#ifdef __SSE2__
  #include <emmintrin.h>
#else
  #fatal You need to have SSE2 support!
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

On my machine, the vector loop is about 3.8 times faster than the scalar loop (12.4 ms versus 47.6 ms).

# Exercises

* Compare to multiplication and division

* Intrinsics also for sqrt. Convert to sqrt using XXX. 

[chris@localhost examples]$ ./ssesqrt 
The standard loop took 211477 microseconds to complete.
The vectorised loop took 13537 microseconds to complete.


***

# [Previous](part2.md) [Up](part2.md) [Next](immintrin.md)
