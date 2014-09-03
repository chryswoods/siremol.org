
from Sire.Mol import *
from Sire.MM import *
from Sire.IO import *
from Sire.System import *
from Sire.Maths import *
from Sire.Units import *

import Sire.Stream
import math

## Set the maximum amount to change each dihedral
max_delta = 5 * degrees

## Set the temperature
temperature = 298.15 * kelvin

## we will move dihedrals by splitting the change
## across the two sets by mass
map = { "weight function" : RelFromMass() }

## Load the ligand from the Sire restart file
system = Sire.Stream.load("l7n.s3")

## pick out the ligand molecule
ligand = system[ MolWithResID("L7N") ].molecule()

## Get the list of all dihedrals from the ligand's
## 'connectivity' property
dihedrals = ligand.property("connectivity").getDihedrals()

## Get the number of dihedrals
ndihedrals = len(dihedrals)

## create a random number generator for the moves
rangen = RanGenerator()

def mcMove(block, nmove):
    print("\nBlock %d, Move %d" % (block,nmove))

    ## calculate the energy before the move
    old_energy = system.energy()

    ## get the version of the ligand
    ## currently in the system
    ligand = system[ MolWithResID("L7N") ].molecule()

    ## randomly choose a dihedral to move
    dihedralid = dihedrals[ rangen.randInt(0,ndihedrals-1) ]

    print("\nRandomly chosen dihedral %s" % dihedralid)

    ## randomly choose an amount to move the dihedral
    delta = rangen.rand(-max_delta.to(degrees), max_delta.to(degrees)) * degrees

    print("Randomly changing the dihedral by %s" % delta)

    ## change the dihedral - either change the whole dihedral
    ## or just change the specified dihedral
    if rangen.randBool():
        new_ligand = ligand.move().change(dihedralid, delta, map).commit()
    else:
        center_bond = BondID(dihedralid.atom1(), dihedralid.atom2())
        new_ligand = ligand.move().change(center_bond, delta, map).commit()

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
