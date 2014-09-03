
from Sire.Mol import *
from Sire.MM import *
from Sire.IO import *
from Sire.System import *
from Sire.Maths import *
from Sire.Units import *

import Sire.Stream
import math

## Set the maximum amount to change each bond
max_delta = 0.05 * angstrom

## Set the temperature
temperature = 298.15 * kelvin

## we will move bonds by splitting the change
## across the two sets by mass
map = { "weight function" : RelFromMass() }

## Load the ligand from the Sire restart file
system = Sire.Stream.load("l7n.s3")

## pick out the ligand molecule
ligand = system[ MolWithResID("L7N") ].molecule()

## Get the list of all bonds from the ligand's
## 'connectivity' property
bonds = ligand.property("connectivity").getBonds()

## Get the number of bonds
nbonds = len(bonds)

## create a random number generator for the moves
rangen = RanGenerator()

def mcMove(block, nmove):
    print("\nBlock %d, Move %d" % (block,nmove))

    ## calculate the energy before the move
    old_energy = system.energy()

    ## get the version of the ligand
    ## currently in the system
    ligand = system[ MolWithResID("L7N") ].molecule()

    ## randomly choose a bond to move
    bondid = bonds[ rangen.randInt(0,nbonds-1) ]

    print("\nRandomly chosen bond %s" % bondid)

    ## randomly choose an amount to move the bond
    delta = rangen.rand(-max_delta.value(), max_delta.value()) * angstrom

    print("Randomly changing the bond by %s" % delta)

    ## change the bond
    new_ligand = ligand.move().change(bondid, delta, map).commit()

    ## update the system with the moved molecule
    system.update(new_ligand)

    ## calcualte the new energy after the move
    new_energy = system.energy()

    ## what is the difference in energy
    delta_energy = new_energy - old_energy

    print("Change in energy = %s" % delta_energy)

    ## calculate exp( -dE / kT )
    x = math.exp( -delta_energy.value() / (k_boltz * temperature.to(kelvin)) )

    print("exp( -dE / kT ) = %s" % x)

    ## generate a random number between 0 and 1
    random_number = rangen.rand(0,1)

    print("Random number = %s" % random_number)
 
    ## Compare exp(-dE/kT) against this random number
    if x >= random_number:
        print("exp(-dE / kT) >= random(0,1), so MC move accepted.")
    else:
        print("exp(-dE / kT) < random(0,1), so MC move rejected.")
        # move has been rejected, so we have to move the ligand
        # back to its old conformation
        system.update(ligand)


# save the first conformation of the ligand
first_ligand = system[MolWithResID("L7N")].molecule()

# perform 50 blocks of 10 moves
for i in range(1,51):
    print("\nBlock %d" % i)

    for j in range(1,11):     
        mcMove(i, j)
    
    # print out a PDB of the coordinates - align the ligand
    # against the first frame
    ligand = system[MolWithResID("L7N")].molecule()
    ligand = ligand.move().align(first_ligand).commit()
    PDB().write(ligand, "output_%00000008d.pdb" % i)
