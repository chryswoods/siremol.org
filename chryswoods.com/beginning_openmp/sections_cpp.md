#C++

Create the file `omp_sections.cpp` and copy in the following;

```c++
#include <iostream>
#include <unistd.h>

#ifdef _OPENMP
    #include <omp.h>
#else
    #define omp_get_thread_num() 0
#endif

void times_table(int n)
{
    int thread_id = omp_get_thread_num();

    for (int i=1; i<=n; ++i)
    {
        int i_times_n = i * n;
        std::cout << "Thread " << thread_id << " says " << i
                  << " times " << n << " equals " << i_times_n << std::endl;
        sleep(1);
    }
}

void countdown()
{
    int thread_id = omp_get_thread_num();

    for (int i=10; i>=1; --i)
    {
        std::cout << "Thread " << thread_id << " says " << i << "...\n";
        sleep(1);
    }

    std::cout << "Thread " << thread_id << " says \"Lift off!\"\n";
}

void long_loop()
{
    double sum = 0;

    int thread_id = omp_get_thread_num();

    for (int i=1; i<=10; ++i)
    {
        sum += (i*i);
        sleep(1);
    }

    std::cout << "Thread " << thread_id << " says the sum of the long loop is "
              << sum << std::endl;
}

int main(int argc, const char **argv)
{
    std::cout << "This is the main thread.\n";

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

    std::cout << "Back to the main thread. Goodbye!\n";

    return 0;
}
```

Note that we have included the header file `unistd.h` to use the function `sleep`, 
to add one second pauses (via `sleep(1)`) within each function.

In this example, the `omp sections` specifies a block of sections that may be 
run in parallel, with each individual section specified within each `omp section` 
block. While it is possible to write the code within each `omp section` block 
directly, the code is more readable if you write each section as a function 
(e.g. `countdown`, `long_loop` and `times_table`) and just call the function 
from within each section.

You can compile this program using one of these commands (choose one for the 
compiler you wish to use);

* g++ : `g++ -fopenmp omp_sections.cpp -o omp_sections`
* icpc : `icpc -openmp omp_sections.cpp -o omp_sections -cxxlib-icc`
* pgCC : `pgCC -mp omp_sections.cpp -o omp_sections`

This will produce the executable, `omp_sections`.

Now [return to the previous page](sections.md).


