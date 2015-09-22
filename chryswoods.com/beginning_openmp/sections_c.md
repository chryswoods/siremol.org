#C

Create the file `omp_sections.c` and copy in the following;

```c
#include <stdio.h>
#include <unistd.h>

#ifdef _OPENMP
    #include <omp.h>
#else
    #define omp_get_thread_num() 0
#endif

void times_table(int n)
{
    int i, i_times_n, thread_id;
    
    thread_id = omp_get_thread_num();

    for (i=1; i<=n; ++i)
    {
        i_times_n = i * n;
        printf("Thread %d says %d times %d equals %d.\n",
               thread_id, i, n, i_times_n );

        sleep(1);
    }
}

void countdown()
{
    int i, thread_id;

    thread_id = omp_get_thread_num();

    for (i=10; i>=1; --i)
    {
        printf("Thread %d says %d...\n", thread_id, i);
        sleep(1);
    }

    printf("Thread %d says \"Lift off!\"\n", thread_id);
}

void long_loop()
{
    int i, thread_id;
    double sum = 0;

    thread_id = omp_get_thread_num();

    for (i=1; i<=10; ++i)
    {
        sum += (i*i);
        sleep(1);
    }

    printf("Thread %d says the sum of the long loop is %f\n",
            thread_id, sum);
}

int main(int argc, char **argv)
{
    printf("This is the main thread.\n");

    #pragma omp parallel
    {
        #pragma omp sections
        {
            #pragma omp section
            {
                times_table(12);
            }
            #pragma omp section
            {
                countdown();
            }
            #pragma omp section
            {
                long_loop();
            }
        }
    }

    printf("Back to the main thread. Goodbye!\n");

    return 0;
}
```

Note that we have included the header file `unistd.h` to use the function `sleep`, 
to add one second pauses (via `sleep(1)`) within each function.

In this example, the `omp sections` specifies a block of sections that may 
be run in parallel, with each individual section specified within each `omp section` 
block. While it is possible to write the code within each `omp section` block 
directly, the code is more readable if you write each section as a 
function (e.g. `countdown`, `long_loop` and `times_table`) and just call 
the function from within each section.

You can compile this program using one of these commands (choose one 
for the compiler you wish to use);

* gcc : `gcc -fopenmp sections.c -o sections`
* icc : `icc -openmp sections.c -o sections -cxxlib-icc`
* pgc : `pgc -mp sections.c -o sections`

This will produce the executable, `sections`.

Now [return to the previous page](sections.md).

