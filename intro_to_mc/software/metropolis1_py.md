
# metropolis.py

You can download the `metropolis.py` script directly by [clicking here](1/metropolis.py) (depending on your browser, on the next page you may need to click on the button marked 'Raw', or right click on the button marked 'Raw' and choose 'Save As...').

Alternatively, you can copy and paste the script from below. To do this, first remove your old copy of `metropolis.py` using the command;

```
rm metropolis.py
```

Next, create a new file called `metropolis.py` using the command;

```
nano metropolis.py
```

Then copy and paste the below script into that file;

```python

import random
import math
import copy

# Set the number of atoms in the box
n_atoms = 25

# Set the number of Monte Carlo moves to perform
num_moves = 5000

# Set the size of the box (in Angstroms)
box_size = [ 15.0, 15.0, 15.0 ]

# The maximum amount that the atom can be translated by
max_translate = 0.5    # angstroms

# Simulation temperature
temperature = 298.15   # kelvin

# Simulation pressure
pressure = 1           # atmospheres

# Convert pressure to internal units (kcal mol-1 A-3)
pressure = pressure * 1.458397506863647E-005

# Give the Lennard Jones parameters for the atoms
# (these are the OPLS parameters for Krypton)
sigma = 3.624         # angstroms
epsilon = 0.317       # kcal mol-1

# Create an array to hold the coordinates of the atoms
coords = []

# Randomly generate the coordinates of the atoms in the box
for i in range(0,n_atoms):
    # Note "random.uniform(x,y)" would generate a random number
    # between x and y
    coords.append( [random.uniform(0,box_size[0]), \
                    random.uniform(0,box_size[1]), \
                    random.uniform(0,box_size[2]) ] )


def make_periodic(x, box):
    """Subroutine to apply periodic boundaries"""
    while (x < -0.5*box):
        x += box

    while (x > 0.5*box):
        x -= box

    return x


def wrap_into_box(x, box):
    """Subroutine to wrap the coordinates into a box"""
    while (x > box):
        x -= box

    while (x < 0):
        x += box

    return x


def print_pdb(move):
    """Print a PDB for the specified move"""
    filename = "output%000006d.pdb" % move

    FILE = open(filename, "w")

    FILE.write("CRYST1 %8.3f %8.3f %8.3f  90.00  90.00  90.00\n" % \
                  (box_size[0], box_size[1], box_size[2]))

    for i in range(0,n_atoms):
        FILE.write("ATOM  %5d  Kr   Kr     1    %8.3f%8.3f%8.3f  1.00  0.00          Kr\n" % \
                      (i+1, coords[i][0], coords[i][1], coords[i][2]))
        FILE.write("TER\n")

    FILE.close()


# Subroutine that calculates the energies of the atoms
def calculate_energy():
    """Calculate the energy of the passed atoms (assuming all atoms
       have the same LJ sigma and epsilon values)"""

    # Loop over all pairs of atoms and calculate
    # the LJ energy
    total_energy = 0

    for i in range(0,n_atoms-1):
        for j in range(i+1, n_atoms):
            delta_x = coords[j][0] - coords[i][0]
            delta_y = coords[j][1] - coords[i][1]
            delta_z = coords[j][2] - coords[i][2]

            # Apply periodic boundaries
            delta_x = make_periodic(delta_x, box_size[0])
            delta_y = make_periodic(delta_y, box_size[1])
            delta_z = make_periodic(delta_z, box_size[2])

            # Calculate the distance between the atoms
            r = math.sqrt( (delta_x*delta_x) + (delta_y*delta_y) +
                           (delta_z*delta_z) )

            # E_LJ = 4*epsilon[ (sigma/r)^12 - (sigma/r)^6 ]
            e_lj = 4.0 * epsilon * ( (sigma/r)**12 - (sigma/r)**6 )

            total_energy += e_lj

    # return the total energy of the atoms
    return total_energy


# calculate kT
k_boltz = 1.987206504191549E-003  # kcal mol-1 K-1

kT = k_boltz * temperature

# The total number of accepted moves
naccept = 0

# The total number of rejected moves
nreject = 0

# Print the initial PDB file
print_pdb(0)

# Now perform all of the moves
for move in range(1,num_moves+1):

    # calculate the old energy
    old_energy = calculate_energy()

    # calculate the old volume of the box
    V_old = box_size[0] * box_size[1] * box_size[2]

    # Pick a random atom (random.randint(x,y) picks a random
    # integer between x and y, including x and y)
    atom = random.randint(0, n_atoms-1)

    # save the old coordinates
    old_coords = copy.deepcopy(coords)

    # Make the move - translate by a delta in each dimension
    delta_x = random.uniform( -max_translate, max_translate )
    delta_y = random.uniform( -max_translate, max_translate )
    delta_z = random.uniform( -max_translate, max_translate )

    coords[atom][0] += delta_x
    coords[atom][1] += delta_y
    coords[atom][2] += delta_z

    # wrap the coordinates back into the box
    coords[atom][0] = wrap_into_box(coords[atom][0], box_size[0])
    coords[atom][1] = wrap_into_box(coords[atom][1], box_size[1])
    coords[atom][2] = wrap_into_box(coords[atom][2], box_size[2])

    # calculate the new energy
    new_energy = calculate_energy()

    # calculate the new volume of the box
    V_new = box_size[0] * box_size[1] * box_size[2]

    accept = False

    # Automatically accept if the energy goes down
    if (new_energy <= old_energy):
        accept = True

    else:
        # Now apply the Monte Carlo test - compare
        # exp( -(E_new - E_old + P(V_new - V_old)) / kT
        #             +  N ln (V_new - V_old) ) >= rand(0,1)
        x = math.exp( -(new_energy - old_energy + pressure * (V_new - V_old)) / kT
                      + n_atoms * (math.log(V_new) - math.log(V_old) ) )

        if (x >= random.uniform(0.0,1.0)):
            accept = True
        else:
            accept = False

    if accept:
        # accept the move
        naccept += 1
        total_energy = new_energy
    else:
        # reject the move - restore the old coordinates
        nreject += 1

        # restore the old conformation
        coords = copy.deepcopy(old_coords)

        total_energy = old_energy

    # print the energy every 10 moves
    if move % 10 == 0:
        print("%s %s  %s  %s" % (move, total_energy, naccept, nreject))


    # print the coordinates every 100 moves
    if move % 100 == 0:
        print_pdb(move)
```

***

