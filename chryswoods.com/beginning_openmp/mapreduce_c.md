#C

```c
#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/* Define an Ion type to hold the 
   coordinates of an Ion */
typedef struct Ion
{
    double x;
    double y;
    double z;
} Ion;

/* The reference Ion */
struct Ion reference_ion;

/* Return the square of a number */
double square(double x)
{
    return x*x;
}

/* Energy function to be mapped */
double calc_energy( struct Ion ion )
{
    double r;

    r = sqrt( square( reference_ion.x - ion.x ) +
              square( reference_ion.y - ion.y ) +
              square( reference_ion.z - ion.z ) );

    /* The energy is simply 1 / r */
    return 1.0 / r;
}

/* You will need to fill in this function to read in 
   an array of ions and return the array */
struct Ion* readArrayOfIons(int *num_ions)
{
    int i;
    Ion *ions = (Ion*)malloc(10 * sizeof(Ion));

    *num_ions = 10;

    for (i=0; i<10; ++i)
    {
        ions[i].x = 0.0;
        ions[i].y = 0.0;
        ions[i].z = i;
    }

    return ions;
}

int main(int argc, char **argv)
{
    int i, num_ions;
    struct Ion *ions_array;
    double total_energy, mapped_energy;

    /* Lets put the reference ion at (1,2,3) */
    reference_ion.x = 1.0;
    reference_ion.y = 2.0;
    reference_ion.z = 3.0;

    /* Now read in an array of ions */
    ions_array = readArrayOfIons( &num_ions );

    total_energy = 0.0;

    #pragma omp parallel private(mapped_energy) \
                         reduction( + : total_energy )
    {
        mapped_energy = 0.0;

        #pragma omp for
        for (i=0; i < num_ions; ++i)
        {
            /* Map this ion against the function */
            mapped_energy += calc_energy( ions_array[i] );
        }

        /* Reduce to get the result */
        total_energy += mapped_energy;
    }
    
    printf("The total energy is %f\n", total_energy);

    return 0;
}
```

[Back](mapreduce.md)

