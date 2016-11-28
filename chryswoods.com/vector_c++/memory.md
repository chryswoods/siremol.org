# Part 1: Memory Layout

The way you put data in memory is crucial to achieve a speed-up
when vectorising your code. It is much more efficient to load
the vector register with variables that are contiguous in memory.

For example, in the diagram below you can see the a vector
register being loading with contiguous memory (`a[0] a[1] a[2] a[3]`),
compared to being loaded with non-contiguous memory (`a[0] a[10] a[20] a[30]`).

![Comparing a packed load versus an unpacked load](images/packed.jpg)

We can compare the speed of using contiguous and non-contiguous memory
using the code below. Create a new file called `loop2.cpp` and copy
into it;

```c++
#include "workshop.h"

int main(int argc, char **argv)
{
    const int size = 512;

    auto a = workshop::Array<float>(10*size);
    auto b = workshop::Array<float>(10*size);
    auto c = workshop::Array<float>(size);

    for (int i=0; i<size; ++i)
    {
        a[i*10] = 1.0*(i+1);
        b[i*10] = 2.5*(i+1);
        c[i] = 0.0;
    }

    auto timer = workshop::start_timer();

    for (int j=0; j<100000; ++j)
    {
        for (int i=0; i<size; ++i)
        {
            c[i] = a[i*10] + b[i*10];
        }
    }

    auto duration = workshop::get_duration(timer);

    timer = workshop::start_timer();

    for (int j=0; j<100000; ++j)
    {    
        #pragma omp simd
        for (int i=0; i<size; ++i)
        {
            c[i] = a[i*10] + b[i*10];
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
g++ -O2 --std=c++14 -fopenmp-simd -Iinclude loop2.cpp -o loop2
./loop2
```

This program is almost identical to the `loop.cpp` that you used at the
[start of this workshop](part1.md). The only difference is that 
the loop sums every 10th element of the array rather than every element.
This means that the vector registers are being filled by data that 
is not contiguous in memory (e.g. `a[10]` is separated from `a[20]` by
ten floats, which is separated from `a[30]` by ten floats, which is 
separated from `a[40]` by ten floats. In comparison `a[0]` is next
to `a[1]`, which is next to `a[2]` which is next to `a[3]`).

Do you still see the same speed-up for the vectorised loop over the scalar
loop as you did for the original `loop.cpp`.

On an older Intel processor, I see that the speed up of the vectorised loop
compared to the scalar loop of `loop2` is only ~1.7x. The speed up for 
the vectorised loop in `loop`, which loads from contiguous memory is
is ~4x. This shows that loading non-contiguous data into a vector register reduces 
performance. However, on a new Intel processor (2016) I don't see any difference in speed-up
between `loop2` and `loop`. This suggests that newer processors are less sensitive.

The reason for this is that the processor has to do more work to load
data from non-contiguous memory, compared to loading from contiguous memory.
Newer processors have features that aim to hide or minimise this extra work.

To maintain performance portability, and make sure that your vector code
runs efficiently on both old and new processors, you should make sure you 
load vectors from contiguous memory whenever possible.

## Array of structs versus structs of arrays

It is easy to load vectors from contiguous memory when you are working
with simple data types (i.e. floats or doubles). However, the main benefit 
of using C++ is that you create more complex data types. For example, create
a new file called `a_of_s.cpp` and copy into it the below code;

```c++
a_of_s.cpp
```

Compile and run using

```
g++ -O2 -fopenmp-simd --std=c++14 -Iinclude a_of_s.cpp -o a_of_s
./a_of_s
```

This program uses a `Point` class that is defined in `include/workshop.h`.
This is a simple class with floats to hold the `x`, `y` and `z` coordinates,
as seen here;

```c++
class Point
```

The program creates two arrays of `Point` objects, `a` and `b`. The square
of the distance between pairs of points is calculated and stored in `c`,
using the code

```c++
float dx = a[i].x - b[i].x;
float dy = a[i].y - b[i].y;
float dz = a[i].z - b[i].z;

c[i] = dx*dx + dy*dy + dz*dz;
```

As with the previous examples, this is performed as part of a scalar loop,
and a loop vectorised using `#pragma omp simd`.

On most computers, you should see vectorisation has made the calculation
faster, but this speed-up is limited (i.e. on my older computer the
vector loop is only ~1.25x faster than the scalar loop). Why is this the case?

The reason is that the array of Point objects...

![Array of structs layout in memory](images/aofs.jpg)

Array of structs is slow. Need to convert into a struct of arrays. Points
object. This is a class that holds three arrays (struct of arrays).

Containers need to be struct of arrays, rather than array of structs.

On my older Intel processor, the vectorisation speed-up for an 
array of structs is only ~1.25x. The speed-up for a struct of arrays
is ~3.4x. On my new Intel processor (2016), there is almost 
no difference in speed-up. This suggests that newer processors 
are less sensitive to memory layout, and are better able to load
vectors from non-contiguous memory.

However, to maintain performance portability, and ensure that your
code runs efficiently on both old and new processors, you should
lay out your data using structs of arrays, rather than arrays
of structs.

***

# [Previous](features.md) [Up](README.md) [Next](limitations.md)

