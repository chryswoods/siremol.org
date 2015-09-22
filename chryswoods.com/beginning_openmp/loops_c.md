#C

Copy this into `loops.c`

```c
#include <stdio.h>

#ifdef _OPENMP
    #include <omp.h>
#else
    #define omp_get_thread_num() 0
#endif

int main(int argc, char **argv)
{
    int i, thread_id, nloops;

    #pragma omp parallel private(thread_id, nloops)
    {
        nloops = 0;

        #pragma omp for
        for (i=0; i<1000; ++i)
        {
            ++nloops;
        }

        thread_id = omp_get_thread_num();

        printf("Thread %d performed %d iterations of the loop.\n",
                thread_id, nloops );
    }

    return 0;
}
```

The new directive in this code is `omp for`. This tells the compiler 
that the `for` loop directly below this pragma can be run in parallel 
by the team of threads. In this case, the only work performed in 
each iteration is increasing the thread private counter of the number of 
times that the loop has been performed (each thread in the team has 
its own copy of `nloops` because it is specified as `private` as part of the 
OpenMP `parallel` pragma). By doing this, each thread in the team counts 
up the number of times that it has performed the loop.

You can compile this program using one of these commands (choose one 
for the compiler you wish to use);

* gcc : `gcc -fopenmp loops.c -o loops`
* icc : `icc -openmp loops.c -o loops -cxxlib-icc`
* pgc : `pgc -mp loops.c -o loops`

This will produce the executable, `loops`.

Now [return to the previous page](loops.md).

