
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

// Set the number of atoms in the box
const int n_atoms = 25;

// Set the number of Monte Carlo moves to perform
const int num_moves = 20000000;

// Set the size of the box (in Angstroms)
double box_size[3] = { 15.0, 15.0, 15.0 };

// The maximum amount that the atom can be translated by
const double max_translate = 0.5;   // angstroms

// Simulation temperature
const double temperature = 100;   // kelvin

// Simulation pressure (atmospheres converted to internal
// units - kcal mol-1 A-3)
double pressure = 1 * 1.458397506863647E-005;   // atmospheres

// The maximum amount to change the volume - the
// best value is 10% of the number of atoms
const double max_volume_change = 0.1 * n_atoms;   // Angstroms**3

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
    
    snprintf(filename, 128, "output%00000008d.pdb", move);

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

    // The total number of accepted volume moves
    int nvolaccept = 0;

    // The total number of rejected volume moves
    int nvolreject = 0;

    // Print the initial PDB file
    print_pdb(coords, n_atoms, 0);

    for (int move=1; move<=num_moves; move = move + 1)
    {
        // calculate the old energy
        const double old_energy = calculate_energy(coords, n_atoms, box_size, sigma, epsilon);

        // calculate the old volume of the box
        const double V_old = box_size[0] * box_size[1] * box_size[2];

        // Pick a random atom
        int atom = int( rand(0, n_atoms) );

        // save the old coordinates
        copy_coordinates(coords, old_coords);

        // save the old box dimensions
        const double old_box_size[3] = { box_size[0], box_size[1], box_size[2] };

        // Decide if we are performing an atom move, or a volume move
        if (rand(0.0, 1.0) <= 1.0 / n_atoms)
        {
            // 1 in $n_atoms chance of being here. Perform a volume move
            // by changing the volume for a random amount
            double delta_vol = rand(-max_volume_change, max_volume_change);

            double V_new = V_old + delta_vol;

            // Volume is the cube of the box length, so add the cube root
            // of this change onto the box size
            double box_side = pow(V_new, 1.0/3.0);

            // work out how much we need to scale the position of the atoms
            double scale_ratio = std::pow( V_new / V_old, 1.0/3.0 );

            // now translate every atom so that it is scaled from the center 
            // of the box
            for (int i=0; i<n_atoms; ++i)
            {
                double dx = coords[i][0] - (0.5*box_size[0]);
                double dy = coords[i][1] - (0.5*box_size[1]);
                double dz = coords[i][2] - (0.5*box_size[2]);

                double length = std::sqrt(dx*dx + dy*dy + dz*dz);
                
                if (length > 0.01)   // don't scale atoms already near the center
                {
                    dx /= length;
                    dy /= length;
                    dz /= length;

                    length *= scale_ratio;

                    coords[i][0] = (0.5*box_size[0]) + dx * length;
                    coords[i][1] = (0.5*box_size[1]) + dy * length;
                    coords[i][2] = (0.5*box_size[2]) + dz * length;
                }
            }

            // now update the new size of the box
            box_size[0] = box_side;
            box_size[1] = box_side;
            box_size[2] = box_side;
        }
        else
        {
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
        }

        // calculate the new energy
        const double new_energy = calculate_energy(coords, n_atoms, box_size, sigma, epsilon);

        // calculate the new volume of the box
        const double V_new = box_size[0] * box_size[1] * box_size[2];

        bool accept = false;

        // Automatically accept if the energy goes down
        if (new_energy <= old_energy)
        {
            accept = true;
        }
        else
        {
            // Now apply the Monte Carlo test - compare
            // exp( -(E_new - E_old + P(V_new - V_old)) / kT
            //             +  N ln (V_new - V_old) ) >= rand(0,1)
            double x = exp( -((new_energy - old_energy + pressure * (V_new - V_old)) / kT)
                          + (n_atoms * (log(V_new) - log(V_old) )) );

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

            box_size[0] = old_box_size[0];
            box_size[1] = old_box_size[1];
            box_size[2] = old_box_size[2];

            // restore the old coordinates
            copy_coordinates( old_coords, coords );

            total_energy = old_energy;
        }

        // print the energy every 50000 moves
        if (move % 50000 == 0)
        {
            printf("%d %f  %d  %d\n", move, total_energy, 
                       naccept, nreject);

            const double vol = box_size[0] * box_size[1] * box_size[2];

            printf("    Box size = (%f,%f,%f). Volume = %f A^3\n",
                      box_size[0], box_size[1], box_size[2], vol);
        }

        // print the coordinates every 500000 moves
        if (move % 500000 == 0)
        {
            print_pdb(coords, n_atoms, move);
        }
    }

    return 0;
}
