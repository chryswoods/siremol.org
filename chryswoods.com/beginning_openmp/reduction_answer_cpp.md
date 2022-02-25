#Answer to Exercise (C++)

```c++
#include <cmath>
#include <random>
#include <iostream>

int main()
{
    int n_inside = 0;
    int n_outside = 0;
    
    std::random_device rd;
    
    #pragma omp parallel reduction(+ : n_inside, n_outside)
    {
        int pvt_n_inside = 0;
        int pvt_n_outside = 0;
        
        std::minstd_rand generator(rd());
        std::uniform_real_distribution random(-1.0, 1.0);

        #pragma omp for
        for (int i=0; i<1000000; ++i)
        {
            double x = random(generator);
            double y = random(generator);

            double r = std::sqrt( x*x + y*y );

            if (r < 1.0)
            {
                ++pvt_n_inside;
            }
            else
            {
                ++pvt_n_outside;
            }
        }

        n_inside += pvt_n_inside;
        n_outside += pvt_n_outside;
    }

    double pi = (4.0 * n_inside) / (n_inside + n_outside);

    std::cout << "The estimated value of pi is " << pi << std::endl;

    return 0;
}
```

[Back](reduction.md)

