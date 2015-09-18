
from Sire.Mol import *
from Sire.Maths import *
from Sire.IO import *
from Sire.Units import *
from Sire.Stream import *

import math

## Load up the box of water from the Sire restart file
waterbox = load("waterbox.s3")

## Get the number of water molecules in the box
nwaters = waterbox.nMolecules()

## Create a random number generator to generate
## all of the random number we will use
rangen = RanGenerator()

## Specify the temperature of the simulation
temperature = 298.15 * kelvin

## Specify the maximum amount by which to translate
## each water
max_translation = 0.15 * angstrom

## Specify the maximum amount by which to rotate
## each water
max_rotation = 15 * degrees

def mcMove(block, nmove):
    print("\nBlock %d, Move %d" % (block,nmove))

    ## Calculate the current energy of the water box
    old_energy = waterbox.energy()

    ## Choose a water molecule from the box at random
    water_id = rangen.randInt(0, nwaters-1)
    random_water = waterbox[ MolIdx(water_id) ].molecule()

    print("\nRandomly chosen water %s" % water_id)

    ## Now choose a random vector by which to translate
    ## the water (any amount up to 0.15 angstroms)
    random_translate = rangen.vectorOnSphere( max_translation.value() )

    ## Now choose a random axis about which to 
    ## rotate the water molecule
    random_rotate_axis = rangen.vectorOnSphere()

    ## Now choose a random amount by which to rotate
    ## the water molecule (up to 15 degrees)
    random_rotate_angle = rangen.rand(-max_rotation.value(),
                                       max_rotation.value()) * degrees

    print("Randomly translating by %s" % random_translate)
    print("Randomly rotating by %s about %s" % \
               (random_rotate_angle,random_rotate_axis))

    moved_water = random_water.move() \
                              .rotate( \
                    Quaternion(random_rotate_angle,random_rotate_axis), \
                               random_water.evaluate().center() ) \
                              .translate(random_translate).commit()

    ## update the water box with the new coordinates of the water
    waterbox.update(moved_water)

    ## calculate the energy after the move
    new_energy = waterbox.energy()

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
        
        # move has been rejected, so we have to move the water
        # back to its old conformation
        waterbox.update(random_water)


# perform 50 blocks of 10 moves
for i in range(1,51):
    print("\nBlock %d" % i)

    for j in range(1,11):
        mcMove(i, j)

    # print out a PDB of the coordinates
    PDB().write(waterbox.molecules(), "output_%00000008d.pdb" % i)

