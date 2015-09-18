
from Sire.Mol import *
from Sire.Maths import *
from Sire.IO import *
from Sire.Move import *
from Sire.Units import *
from Sire.Stream import *

import math

## Load up the box of water from the Sire restart file
waterbox = load("waterbox.s3")

## Specify the temperature of the simulation
temperature = 298.15 * kelvin

## Specify the maximum amount by which to translate
## each water
max_translation = 0.15 * angstrom

## Specify the maximum amount by which to rotate
## each water
max_rotation = 15 * degrees

## Create a RigidBodyMC move that moves the molecules
## that are contained in the molecule group called 'water'
rb_move = RigidBodyMC( waterbox[ MGName("water") ] )

## Set the maximum translation and rotation for the moves
rb_move.setMaximumTranslation(max_translation)
rb_move.setMaximumRotation(max_rotation)

## Set the temperature of the move
rb_move.setTemperature(temperature)

## Perform 50 blocks of 2000 moves
for i in range(1,51):
    print("\nBlock %d" % i)
    
    # perform the moves
    rb_move.move(waterbox, 2000)

    # print out the energy, and number of accepted / rejected move
    print("Energy %s, nAccepted = %s, nRejected = %s" % \
          (waterbox.energy(), rb_move.nAccepted(), rb_move.nRejected()) )

    # write a PDB of the coordinates
    PDB().write( waterbox.molecules(), "output_%00000008d.pdb" % i )
