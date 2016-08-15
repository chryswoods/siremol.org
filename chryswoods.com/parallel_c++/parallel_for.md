# Part 2: tbb::parallel_for

The simplest construct in TBB is `tbb::parallel_for`. This is used to 
parallelise a `for` loop.

Open a new C++ file called `parallel_for.cpp` and copy into it the
below text;

```c++
#include <tbb/parallel_for.h>

#include <iostream>

int main(int argc, char **argv)
{
    tbb::init();

    
}
