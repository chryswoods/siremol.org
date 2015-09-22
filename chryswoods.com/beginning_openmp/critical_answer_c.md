#Answer to Exercise (C)

```c
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

double rand_one()
{
    return rand() / (RAND_MAX + 1.0);
}

int main(int argc, char **argv)
{
    int n_inside, n_outside;
    int pvt_n_inside, pvt_n_outside;
    int i;

    double x, y, r, pi;

    n_inside = 0;
    n_outside = 0;

    #pragma omp parallel private(x, y, r, pvt_n_inside, pvt_n_outside)
    {
        pvt_n_inside = 0;
        pvt_n_outside = 0;

        #pragma omp for
        for (i=0; i<1000000; ++i)
        {
            x = (2*rand_one()) - 1;
            y = (2*rand_one()) - 1;

            r = sqrt( x*x + y*y );

            if (r < 1.0)
            {
                ++pvt_n_inside;
            }
            else
            {
                ++pvt_n_outside;
            }
        }

        #pragma omp critical
        {
            n_inside += pvt_n_inside;
            n_outside += pvt_n_outside;
        }
    }

    pi = (4.0 * n_inside) / (n_inside + n_outside);

    printf("The estimated value of pi is %f\n", pi);

    return 0;
}
```

[Back](critical.md)

