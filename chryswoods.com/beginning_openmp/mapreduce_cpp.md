#C++

```c++
#include <cmath>
#include <vector>
#include <iostream>

// Define an ion type to hold the
// coordinates of the ion
struct Ion
{
    Ion()
    {
        x = 0;
        y = 0;
        z = 0;
    }

    Ion(double _x, double _y, double _z)
    {
        x = _x;
        y = _y;
        z = _z;
    }

    double x;
    double y;
    double z;
};

// The reference ion
Ion reference_ion;

// Return the square of a number
inline double square(const double x)
{
    return x*x;
}

// Energy function to be mapped
double calc_energy(const Ion &ion)
{
    double r = std::sqrt( square( reference_ion.x - ion.x ) + 
                          square( reference_ion.y - ion.y ) +
                          square( reference_ion.z - ion.z ) );

    // The energy is simply 1 / r
    return 1.0 / r;
}

// You would need to fill in this function to read
// in an array of ions and return the array
std::vector<Ion> readArrayOfIons()
{
    std::vector<Ion> ions;

    for (int i=0; i<10; ++i)
    {
        ions.push_back( Ion(0,0,i) );
    }

    return ions;
}

int main(int argc, const char **argv)
{
    //put the reference ion at (1,2,3)
    reference_ion.x = 1.0;
    reference_ion.y = 2.0;
    reference_ion.z = 3.0;

    //read in the array of ions
    std::vector<Ion> ions_array = readArrayOfIons();

    double total_energy = 0.0;

    #pragma omp parallel reduction( + : total_energy )
    {
        double mapped_energy = 0.0;

        const int n_ions = ions_array.size();

        #pragma omp for
        for (int i=0; i < n_ions; ++i)
        {
            //map this ion against the function
            mapped_energy += calc_energy( ions_array[i] );
        }

        //reduce to get the result
        total_energy += mapped_energy;
    }

    std::cout << "The total energy is " << total_energy << std::endl;

    return 0;
}
```

[Back](mapreduce.md)

