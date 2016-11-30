# Part 2 : AVX Intrinsics - Example answer

```c++
#include "workshop.h"

#ifdef __AVX__
  #include <immintrin.h>
#else
  #warning AVX not supported. Code will not compile.
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
            c[i] = std::sqrt( a[i] + b[i] );
        }
    }

    auto duration = workshop::get_duration(timer);

    timer = workshop::start_timer();

    for (int j=0; j<100000; ++j)
    {    
        for (int i=0; i<size/8; ++i)
        {
            avx_c[i] = _mm256_sqrt_ps( _mm256_add_ps(avx_a[i], avx_b[i]) );
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

***

# [Previous](immintrin.md) [Up](immintrin.md) [Next](immintrin.md)
