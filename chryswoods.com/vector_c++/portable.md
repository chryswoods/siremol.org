
# Part 2: Portable Intrinsics

For portability, you should hide use of intrinsics behind `#ifdef` guards, and
provide a scalar fallback if, e.g. SSE or AVX are not available. There are some
libraries that can help, e.g. Intel's math kernel library etc. etc.

Also, look at `MultiFloat` and `MultiDouble` from the Sire package, as
this creates a `MultiFloat` class that holds a vector of floats, and 
manipulates them in a C++-friendly way.

Create a new file called `portable.cpp` and copy into it;

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
            c[i] = std::sqrt(a[i] + b[i]);
        }
    }

    auto duration = workshop::get_duration(timer);

    timer = workshop::start_timer();

    for (int j=0; j<100000; ++j)
    {   
        for (int i=0; i<vec_size; ++i)
        {
            vec_c[i] = sqrt(vec_a[i] + vec_b[i]);
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


==
[chzcjw@bluegem1 workshop]$ g++ -O2 -msse2 --std=c++14 -Iinclude portable.cpp -o portable[chzcjw@bluegem1 workshop]$ ./portable 
The standard loop took 31888.6 microseconds to complete.
The vectorised loop took 8025.98 microseconds to complete.
[chzcjw@bluegem1 workshop]$ g++ -O2 -mavx --std=c++14 -Iinclude portable.cpp -o portable
[chzcjw@bluegem1 workshop]$ ./portable 
The standard loop took 33470.8 microseconds to complete.
The vectorised loop took 4576.96 microseconds to complete.
[chzcjw@bluegem1 workshop]$ g++ -O2 -fopenmp-simd --std=c++14 -Iinclude portable.cpp -o portable
[chzcjw@bluegem1 workshop]$ ./portable 
The standard loop took 31608.1 microseconds to complete.
The vectorised loop took 8009.71 microseconds to complete.
[chzcjw@bluegem1 workshop]$ g++ -O2 -fopenmp-simd -mavx --std=c++14 -Iinclude portable.cpp -o portable
[chzcjw@bluegem1 workshop]$ ./portable The standard loop took 33317.8 microseconds to complete.
The vectorised loop took 4574 microseconds to complete.

***

# [Previous](immintrin.md) [Up](part2.md) [Next](whatnext.md)
