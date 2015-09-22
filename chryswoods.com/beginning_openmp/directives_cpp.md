#C++

Copy this into the file `hello_threads.cpp`.

```c++
#include <iostream>

#ifdef _OPENMP
    #include <omp.h>
#else
    #define omp_get_num_threads() 0
    #define omp_get_thread_num() 0
#endif

int main(int argc, const char **argv)
{
    std::cout << "I am the main thread.\n";

    #pragma omp parallel
    {
        int nthreads = omp_get_num_threads();
        int thread_id = omp_get_thread_num();

        std::cout << "Hello. I am thread " << thread_id
                  << " out of a team of " << nthreads 
                  << std::endl;
    }

    std::cout << "Here I am, back to the main thread.\n";

    return 0;
}
```

This example uses two OpenMP functions;

* `omp_get_num_threads()` : Returns the number of threads in the OpenMP thread team.
* `omp_get_thread_num()` : Returns the identifying number of the thread in the team.

Note that using these functions requires you to include the `omp.h` header file. 
To ensure portability (if OpenMP is not supported) we hide this header file 
behind an `#ifdef _OPENMP` guard, and add stubs for the two OpenMP functions to set them to 0.

Note also that because the `nthreads` and `thread_id` variables exist only in the 
scope of the `omp parallel` section, each thread will have its own private copy of these variables.

You can compile this program using one of these commands (choose one for the compiler 
you wish to use);

* g++ : `g++ -fopenmp hello_threads.cpp -o hello_threads`
* icpc : `icpc -openmp hello_threads.cpp -o hello_threads -cxxlib-icc`
* pgCC : `pgCC -mp hello_threads.cpp -o hello_threads`

This will produce the executable, `hello_threads`.

Now [return to the previous page](directives.md).
