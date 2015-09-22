#C

Most C compilers support the use of OpenMP. Available compilers include 
gcc (version 4.2 or above), icc and pgc.

The first step is to create a simple OpenMP C program, which we will call 
`hello_openmp`. Open a text editor (e.g. `nano`), create a file called 
`hello_openmp.c` and copy in the following code;

```c
#include <stdio.h>

int main(int argc, char **argv)
{
    #pragma omp parallel
    {
        printf("Hello OpenMP!\n");
    }

    return 0;
}
```

The only new line in this example is `#pragma omp parallel`, which is used 
to specify that all of the code between the curly brackets is part of an 
OpenMP parallel section.

You can compile this program using one of these commands (choose one for 
the compiler you wish to use);

* gcc : `gcc -fopenmp hello_openmp.c -o hello_openmp`
* icc : `icc -openmp hello_openmp.c -o hello_openmp -cxxlib-icc`
* pgc : `pgc -mp hello_openmp.c -o hello_openmp`

This will produce the executable, `hello_openmp`.

Now return to the [previous page](basics.md) to see how to run 
`hello_openmp` in parallel.

