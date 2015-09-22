#C

Copy this into the file `hello_threads.c`.

```c
#include <stdio.h>

#ifdef _OPENMP
    #include <omp.h>
#else
    #define omp_get_num_threads() 0
    #define omp_get_thread_num() 0
#endif

int main(int argc, char **argv)
{
    int nthreads, thread_id;

    printf("I am the main thread.\n");

    #pragma omp parallel private(nthreads, thread_id)
    {
        nthreads = omp_get_num_threads();
        thread_id = omp_get_thread_num();

        printf("Hello. I am thread %d out of a team of %d\n", 
                 thread_id, nthreads);
    }

    printf("Here I am, back to the main thread.\n");

    return 0;
}
```

This example uses two OpenMP functions;

* `omp_get_num_threads()` : Returns the number of threads in the OpenMP thread team.
* `omp_get_thread_num()` : Returns the identifying number of the thread in the team.

Note that using these functions requires you to include the `omp.h` header file. 
To ensure portability (if OpenMP is not supported) we hide this header file 
behind an `#ifdef _OPENMP` guard, and add stubs for the two OpenMP functions to set them to 0.

This example uses a slightly modified omp parallel line. In this case, 
`private(nthreads, thread_id)` is added to specify that each thread should have its 
own copy of the `nthreads` and `thread_id` variables.

You can compile this program using one of these commands (choose one for the 
compiler you wish to use);

* gcc : `gcc -fopenmp hello_threads.c -o hello_threads`
* icc : `icc -openmp hello_threads.c -o hello_threads -cxxlib-icc`
* pgc : `pgc -mp hello_threads.c -o hello_threads`

This will produce the executable, `hello_threads`.

Now [return to the previous page](directives.md).


