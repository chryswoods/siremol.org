
from Sire.Mol import *
from Sire.MM import *
from Sire.IO import *
from Sire.Move import *
from Sire.System import *
from Sire.Maths import *
from Sire.Units import *
from Sire.Tools import *
from Sire.Tools.AmberLoader import *

import Sire.Stream
import math

## Set the temperature
temperature = 298.15 * kelvin

## Specify the maximum amount to move the
## bonds, angles and dihedrals
max_delta_bond = 0.05 * angstrom
max_delta_angle = 2.5 * degrees
max_delta_dihedral = 5 * degrees

## specify the maximum number of bonds,
## angles and dihedrals to move per move
max_num_move = 1

## Load the ligand from the Sire restart file
system = Sire.Stream.load("l7n.s3")

## create an InternalMove that will move the bonds,
## angles and dihedrals of the molecules in group 'ligand'
internalmove = InternalMove( system[MGName("ligand")] )

# save the first conformation of the ligand
first_ligand = system[MolWithResID("L7N")].molecule()

# set the maximum delta parameters
params = {}
params["bond flex"] = max_delta_bond
params["angle flex"] = max_delta_angle
params["dihedral flex"] = max_delta_dihedral
params["h dihedral flex"] = max_delta_dihedral
params["maxvar"] = max_num_move
Parameter.push(params)

# generate a new flexibility object for the ligand
flexibility = generateFlexibility(first_ligand)

# assign this flexibility to the ligand
first_ligand = first_ligand.edit() \
                           .setProperty("flexibility", flexibility) \
                           .commit()

# update the ligand in the system
system.update(first_ligand)

# perform 50 blocks of 250 moves
for i in range(1,51):
    print("\nBlock %d" % i)

    internalmove.move(system, 250, False)

    # print out the energy, and number of accepted / rejected move
    print("Energy %s, nAccepted = %s, nRejected = %s" % \
          (system.energy(), internalmove.nAccepted(), 
           internalmove.nRejected()) )
    
    # print out a PDB of the coordinates - align the ligand
    # against the first frame
    ligand = system[MolWithResID("L7N")].molecule()
    ligand = ligand.move().align(first_ligand).commit()
    PDB().write(ligand, "output_%00000008d.pdb" % i)
