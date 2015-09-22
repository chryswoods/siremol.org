#C

```c
#include <stdio.h>

int main(int argc, char **argv)
{
    int i;
    int private_nloops, nloops;

    nloops = 0;

    #pragma omp parallel private(private_nloops) \
                         reduction(+ : nloops)
    {
        private_nloops = 0;

        #pragma omp for
        for (i=0; i<100000; ++i)
        {
            ++private_nloops;
        }

        /* Reduction step - reduce 'private_nloops' into 'nloops' */
        nloops = nloops + private_nloops;
    }

    printf("The total number of loop iterations is %d\n",
           nloops);

    return 0;
}
```

[Return to the previous page](reduction.md).

