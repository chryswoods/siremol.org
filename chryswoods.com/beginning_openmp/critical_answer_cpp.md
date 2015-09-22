#Answer to Exercise (C++)

```c++
#include <cmath>
#include <cstdlib>
#include <iostream>

double rand_one()
{
    return std::rand() / (RAND_MAX + 1.0);
}

int main(int argc, const char **argv)
{
    int n_inside = 0;
    int n_outside = 0;

    #pragma omp parallel
    {
        int pvt_n_inside = 0;
        int pvt_n_outside = 0;

        #pragma omp for
        for (int i=0; i<1000000; ++i)
        {
            double x = (2*rand_one()) - 1;
            double y = (2*rand_one()) - 1;

            double r = sqrt( x*x + y*y );

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

    double pi = (4.0 * n_inside) / (n_inside + n_outside);

    std::cout << "The estimated value of pi is " << pi << std::endl;

    return 0;
}
```

[Back](critical.md)
