#C++

Copy this code into `broken_loopcount.cpp`

```c++
#include <iostream>

#ifdef _OPENMP
    #include <omp.h>
#else
    #define omp_get_thread_num() 0
#endif

int main(int argc, char **argv)
{
    int global_nloops = 0;

    #pragma omp parallel
    {
        int private_nloops = 0;

        int thread_id = omp_get_thread_num();

        #pragma omp for
        for (int i=0; i<100000; ++i)
        {
            ++private_nloops;
        }

        std::cout << "Thread " << thread_id << " adding its iterations ("
                  << private_nloops << ") to the sum (" << global_nloops 
                  << ")...\n";

        global_nloops += private_nloops;

        std::cout << "...total nloops now equals " << global_nloops << ".\n";
    }

    std::cout << "The total number of loop iterations is " << global_nloops 
              << ".\n";

    return 0;
}
```

and copy this code into `fixed_loopcount.cpp`

```c++
#include <iostream>

#ifdef _OPENMP
    #include <omp.h>
#else
    #define omp_get_thread_num() 0
#endif

int main(int argc, char **argv)
{
    int global_nloops = 0;

    #pragma omp parallel
    {
        int private_nloops = 0;

        int thread_id = omp_get_thread_num();

        #pragma omp for
        for (int i=0; i<100000; ++i)
        {
            ++private_nloops;
        }

        #pragma omp critical
        {
            std::cout << "Thread " << thread_id << " adding its iterations ("
                      << private_nloops << ") to the sum (" << global_nloops 
                      << ")...\n";

            global_nloops += private_nloops;

            std::cout << "...total nloops now equals " << global_nloops 
                      << ".\n";
        }
    }

    std::cout << "The total number of loop iterations is " << global_nloops 
              << ".\n";

    return 0;
}
```

The only new code here is the `omp critical` section in `fixed_loopcount.cpp`. 
The critical section is performed by each thread, but can only be performed 
by one thread at a time. This ensures that while one thread is updating the 
global `nloops` variable (`global_nloops`) with the thread local value of 
`nloops` (`private_nloops`), that the value of `global_nloops` is not 
changed by any other thread.

You can compile these programs using one of these sets of commands 
(choose one for the compiler you wish to use);

* g++ : `g++ -fopenmp broken_loopcount.cpp -o broken_loopcount ; g++ -fopenmp fixed_loopcount.cpp -o fixed_loopcount`
* icpc : `icpc -openmp broken_loopcount.cpp -o broken_loopcount -cxxlib-icc ; icpc -openmp fixed_loopcount.cpp -o fixed_loopcount -cxxlib-icc`
* pgCC : `pgCC -mp broken_loopcount.cpp -o broken_loopcount ; pgCC -mp fixed_loopcount.cpp -o fixed_loopcount`

This will produce the executables, `broken_loopcount` and `fixed_loopcount`.

Now [return to the previous page](critical.md).


