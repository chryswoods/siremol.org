
from Sire.Mol import *
from Sire.MM import *
from Sire.IO import *
from Sire.System import *
from Sire.Maths import *
from Sire.Units import *

import Sire.Stream
import math

## Set the maximum amount to change each angle
max_delta = 2.5 * degrees

## Set the temperature
temperature = 298.15 * kelvin

## we will move angles by splitting the change
## across the two sets by mass
map = { "weight function" : RelFromMass() }

## Load the protein from the Sire restart file
system = Sire.Stream.load("protein.s3")

## create a random number generator for the moves
rangen = RanGenerator()

def mcMove(block, nmove):
    print("\nBlock %d, Move %d" % (block,nmove))

    ## calculate the energy before the move
    old_energy = system.energy()

    ## get the version of the protein
    ## currently in the system
    protein = system[ MolWithResID("ALA") ].molecule()

    ## choose a random residue to move (will change the backbone angle)
    res = ResIdx( rangen.randInt(0, protein.nResidues()-1) )

    angleid = AngleID( res + AtomName("C"), res + AtomName("CA"), res + AtomName("N") )

    print("\nRandomly chosen angle %s" % angleid)

    ## randomly choose an amount to move the angle
    delta = rangen.rand(-max_delta.to(degrees), max_delta.to(degrees)) * degrees

    print("Randomly changing the angle by %s" % delta)

    ## change the angle
    new_protein = protein.move().change(angleid, delta, map).commit()

    ## update the system with the moved molecule
    system.update(new_protein)

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
        # move has been rejected, so we have to move the protein
        # back to its old conformation
        system.update(protein)

# save the first conformation of the protein
first_protein = system[MolWithResID("ALA")].molecule()

# perform 10 blocks of 10 moves
for i in range(1,11):
    print("\nBlock %d" % i)

    for j in range(1,11):     
        mcMove(i, j)
    
    # print out a PDB of the coordinates - align the protein
    # against the first frame
    protein = system[MolWithResID("ALA")].molecule()
    protein = protein.move().align(first_protein).commit()
    PDB().write(protein, "output_%00000008d.pdb" % i)
