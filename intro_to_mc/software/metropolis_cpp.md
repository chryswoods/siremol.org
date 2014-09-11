
# metropolis.cpp

You can download the `metropolis.cpp` program directly by [clicking here](https://github.com/chryswoods/python_for_bio/raw/master/intro_to_mc/software/metropolis.cpp) (depending on your browser, on the next page you may need to click on the button marked 'Raw', or right click on the button marked 'Raw' and choose 'Save As...').

Alternatively, you can copy and paste the script from below. To do this, create a new file called `metropolis.cpp` using the command;

```
nano metropolis.cpp
```

Then copy and paste the below script into that file;

```c++

#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

// Set the number of atoms in the box
const int n_atoms = 25;

// Set the number of Monte Carlo moves to perform
const int num_moves = 500000;

// Set the size of the box (in Angstroms)
const double box_size[3] = { 15.0, 15.0, 15.0 };

// The maximum amount that the atom can be translated by
const double max_translate = 0.5;  // angstroms

// Simulation temperature
const double temperature = 298.15;   // kelvin

// Give the Lennard Jones parameters for the atoms
// (these are the OPLS parameters for Krypton)
const double sigma = 3.624;     // angstroms
const double epsilon = 0.317;   // kcal mol-1

// function to return a random number between 'start' to 'end'
double rand(const double start, const double end)
{
    return (end-start) * (double(rand()) / RAND_MAX) + start;
}

// Subroutine to apply periodic boundaries
double make_periodic(double x, const double box)
{
    while (x < -0.5*box)
    {
        x = x + box;
    }

    while (x > 0.5*box)
    {
        x = x - box;
    }

    return x;
}

// Subroutine to wrap the coordinates into a box
double wrap_into_box(double x, double box)
{
    while (x > box)
    {
        x = x - box;
    }

    while (x < 0)
    {
        x = x + box;
    }

    return x;
}

// Subroutine to print a PDB of the coordinates
void print_pdb(double **coords, const int n_atoms, const int move)
{
    char filename[128];
    
    snprintf(filename, 128, "output%000006d.pdb", move);

    FILE *f = fopen(filename, "w");

    fprintf(f, "CRYST1 %8.3f %8.3f %8.3f  90.00  90.00  90.00\n", 
               box_size[0], box_size[1], box_size[2]);

    for (int i = 0; i < n_atoms; i = i + 1)
    {
        fprintf(f, "ATOM  %5d  Kr   Kr     1    %8.3f%8.3f%8.3f  1.00  0.00          Kr\n",
                       i+1, coords[i][0], coords[i][1], coords[i][2]); 
        fprintf(f, "TER\n");
    }

    fclose(f);
}

// Subroutine that calculates the energies of the atoms
double calculate_energy(double **coords, const int n_atoms, const double *box_size,
                        const double sigma, const double epsilon)
{
    // Loop over all pairs of atoms and calculate
    // the LJ energy
    double total_energy = 0;

    for (int i = 0; i < n_atoms-1; i = i + 1)
    {
        for (int j = i+1; j < n_atoms; j = j + 1)
        {
            double delta_x = coords[j][0] - coords[i][0];
            double delta_y = coords[j][1] - coords[i][1];
            double delta_z = coords[j][2] - coords[i][2];

            // Apply periodic boundaries
            delta_x = make_periodic(delta_x, box_size[0]);
            delta_y = make_periodic(delta_y, box_size[1]);
            delta_z = make_periodic(delta_z, box_size[2]);

            const double r2 = (delta_x*delta_x) + (delta_y*delta_y) +
                              (delta_z*delta_z);

            // E_LJ = 4*epsilon[ (sigma/r)^12 - (sigma/r)^6 ]
            const double sig2_over_r2 = (sigma*sigma) / r2;
            const double sig6_over_r6 = sig2_over_r2*sig2_over_r2*sig2_over_r2;
            const double sig12_over_r12 = sig6_over_r6 * sig6_over_r6;

            const double e_lj = 4.0 * epsilon * ( sig12_over_r12 - sig6_over_r6 );

            total_energy = total_energy + e_lj;
        }
    }

    // return the total energy of the atoms
    return total_energy;
}

void copy_coordinates(double **from, double **to)
{
    for (int i=0; i<n_atoms; ++i)
    {
        to[i][0] = from[i][0];
        to[i][1] = from[i][1];
        to[i][2] = from[i][2];
    }
}

int main(int argc, const char **argv)
{
    double **coords = new double*[n_atoms];
    double **old_coords = new double*[n_atoms];

    // Randomly generate the coordinates of the atoms in the box
    for (int i = 0; i < n_atoms; i = i + 1)
    {
        coords[i] = new double[3];
        old_coords[i] = new double[3];

        // Note "rand(0,x)" would generate a random number
        // between 0 and $x
        coords[i][0] = rand(0, box_size[0]);
        coords[i][1] = rand(0, box_size[1]);
        coords[i][2] = rand(0, box_size[2]);
    }

    // calculate kT
    const double k_boltz = 1.987206504191549E-003;  // kcal mol-1 K-1

    const double kT = k_boltz * temperature;

    // The total number of accepted moves
    int naccept = 0;

    // The total number of rejected moves
    int nreject = 0;

    // Print the initial PDB file
    print_pdb(coords, n_atoms, 0);

    for (int move=1; move<=num_moves; move = move + 1)
    {
        // calculate the old energy
        const double old_energy = calculate_energy(coords, n_atoms, box_size, sigma, epsilon);

        // Pick a random atom
        int atom = int( rand(0, n_atoms) );

        // save the old coordinates
        copy_coordinates(coords, old_coords);

        // Make the move - translate by a delta in each dimension
        const double delta_x = rand(-max_translate, max_translate);
        const double delta_y = rand(-max_translate, max_translate);
        const double delta_z = rand(-max_translate, max_translate);

        coords[atom][0] = coords[atom][0] + delta_x;
        coords[atom][1] = coords[atom][1] + delta_y;
        coords[atom][2] = coords[atom][2] + delta_z;

        // wrap the coordinates back into the box
        coords[atom][0] = wrap_into_box(coords[atom][0], box_size[0]);
        coords[atom][1] = wrap_into_box(coords[atom][1], box_size[1]);
        coords[atom][2] = wrap_into_box(coords[atom][2], box_size[2]);

        // calculate the new energy
        const double new_energy = calculate_energy(coords, n_atoms, box_size, sigma, epsilon);

        bool accept = false;

        // Automatically accept if the energy goes down
        if (new_energy <= old_energy)
        {
            accept = true;
        }
        else
        {
            // Now apply the Monte Carlo test - compare
            // exp( E_new - E_old / kT ) >= rand(0,1)
            const double x = exp( -(new_energy - old_energy) / kT );

            if (x >= rand(0.0, 1.0))
            {
                accept = true;
            }
            else
            {
                accept = false;
            }
        }

        double total_energy = 0;

        if (accept)
        {
            // accept the move
            naccept = naccept + 1;
            total_energy = new_energy;
        }
        else
        {
            // reject the move - restore the old coordinates
            nreject = nreject + 1;

            // restore the old coordinates
            copy_coordinates( old_coords, coords );

            total_energy = old_energy;
        }

        // print the energy every 1000 moves
        if (move % 1000 == 0)
        {
            printf("%d %f  %d  %d\n", move, total_energy, naccept, nreject);
        }

        // print the coordinates every 10000 moves
        if (move % 10000 == 0)
        {
            print_pdb(coords, n_atoms, move);
        }
    }

    return 0;
}
```

***

