#C++

```c++
#include <iostream>

int main(int argc, char **argv)
{
    int nloops = 0;

    #pragma omp parallel reduction( + : nloops )
    {
        int private_nloops = 0;

        #pragma omp for
        for (int i=0; i<100000; ++i)
        {
            ++private_nloops;
        }

        nloops = nloops + private_nloops;
    }

    std::cout << "The total number of loop iterations is " << nloops << ".\n";

    return 0;
}
```

[Return to the previous page](reduction.md).

