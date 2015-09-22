#C++

Copy this into `loops.cpp`

```c++
#include <iostream>

#ifdef _OPENMP
    #include <omp.h>
#else
    #define omp_get_thread_num() 0
#endif

int main(int argc, const char **argv)
{
    #pragma omp parallel
    {
        int nloops = 0;

        #pragma omp for
        for (int i=0; i<1000; ++i)
        {
            ++nloops;
        }

        int thread_id = omp_get_thread_num();

        std::cout << "Thread " << thread_id << " performed "
                  << nloops << " iterations of the loop.\n";
    }

    return 0;
}
```

The new directive in this code is `omp for`. This tells the compiler 
that the for loop directly below this pragma can be run in parallel 
by the team of threads. In this case, the only work performed in each 
iteration is increasing the thread private counter of the number of 
times that the loop has been performed (each thread in the team has 
its own copy of `nloops` because this variable was declared only within 
the scope of the `omp parallel` block). By doing this, each thread in 
the team counts up the number of times that it has performed the loop.

You can compile this program using one of these commands (choose one for the 
compiler you wish to use);

* g++ : `g++ -fopenmp loops.cpp -o loops`
* icpc : `icpc -openmp loops.cpp -o loops -cxxlib-icc`
* pgCC : `pgCC -mp loops.cpp -o loops`

This will produce the executable, `loops`.

Now [return to the previous page](loops.md).
