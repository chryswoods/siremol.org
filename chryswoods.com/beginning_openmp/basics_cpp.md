#C++

Most C++ compilers support the use of OpenMP. Available compilers include 
g++ (version 4.2 or above), icpc and pgCC.

The first step is to create a simple OpenMP C++ program, which we will 
call `hello_openmp`. Open a text editor (e.g. `nano`), create a file called 
`hello_openmp.cpp` and copy in the following code;

```c++
#include <iostream>

int main(int argc, const char **argv)
{
    #pragma omp parallel
    {
        std::cout << "Hello OpenMP!\n";
    }

    return 0;
}
```

The only new line in this example is `#pragma omp parallel`, which is 
used to specify that all of the code between the curly brackets is 
part of an OpenMP parallel section.

You can compile this program using one of these commands (choose one 
for the compiler you wish to use);

* g++ : `g++ -fopenmp hello_openmp.cpp -o hello_openmp`
* icpc : `icpc -openmp hello_openmp.cpp -o hello_openmp -cxxlib-icc`
* pgCC : `pgCC -mp hello_openmp.cpp -o hello_openmp`

This will produce the executable, `hello_openmp`.

Now return to the [previous page](basics.md) to see how to run 
`hello_openmp` in parallel.
