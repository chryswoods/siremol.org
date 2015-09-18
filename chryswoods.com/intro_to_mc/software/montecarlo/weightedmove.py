
from Sire.Mol import *
from Sire.MM import *
from Sire.IO import *
from Sire.Move import *
from Sire.Qt import *
from Sire.System import *
from Sire.Maths import *
from Sire.Units import *
from Sire.Tools import *
from Sire.Tools.AmberLoader import *

import Sire.Stream
import math

## Set the temperature
temperature = 298.15 * kelvin

## Load the protein-ligand complex from the Sire restart file
system = Sire.Stream.load("system.s3")

## create an InternalMove that will move the bonds,
## angles and dihedrals of the molecules in group 'ligand'
ligand_internalmove = InternalMove( system[MGName("ligand")] )

## create a Rigid Body move that will translate and rotate the ligand
ligand_rbmove = RigidBodyMC( system[MGName("ligand")] )
ligand_rbmove.setMaximumTranslation(0.05*angstrom)
ligand_rbmove.setMaximumRotation(0.25*degrees)

## create a Rigid Body move that will translate and rotate the water
## molecules
water_rbmove = RigidBodyMC( system[MGName("water")] )
water_rbmove.setMaximumTranslation(0.15*angstrom)
water_rbmove.setMaximumRotation(15*degrees)

## create a ZMatMove to move the bonds, angles and dihedrals
## in each of the residues in the protein (this is similar to
## an internal move, but can use pre-defined templates for 
## each of the amino acids to decide how to move the sidechains)
protein_internalmove = ZMatMove( system[MGName("residues")] )

## create a Rigid Body move to move each protein residue backbone
protein_backbonemove = RigidBodyMC( system[MGName("backbones")] )
protein_backbonemove.setMaximumTranslation(0.01*angstrom)
protein_backbonemove.setMaximumRotation(1*degrees)

## create a WeightedMoves object that will randomly select
## which move to perform
moves = WeightedMoves()

## add the water moves, weighted by the number of water molecules
moves.add(water_rbmove, system[MGName("water")].nMolecules())

## add the ligand translation/rotation moves with a weight of 5 (we want to move
## the ligand a lot more than the water)
moves.add(ligand_rbmove, 5)

## add the ligand internal moves with the same weight at its
## translation/rotation moves
moves.add(ligand_internalmove, 5)

## add the residue internal moves with a weight of half of the number
## of residues
moves.add(protein_internalmove, 0.5 * system[MGName("residues")].nViews())

## add the residue backbone moves with a weight of half the number
## of movable backbones
moves.add(protein_backbonemove, 0.5 * system[MGName("backbones")].nViews())

t = QElapsedTimer()

# perform 50 blocks of 5000 moves
for i in range(1,51):
    print("\nBlock %d" % i)

    t.start()
    system = moves.move(system, 5000, False)
    ns = t.nsecsElapsed()

    # print out the energy, and number of accepted / rejected move
    print("Energy %s (took %d ms)\n%s" % (system.energy(), 0.000001*ns, moves))
    
    # print out a PDB of the system
    print("Writing coordinates...")
    t.start()

    # write out the coordinates
    PDB().write(system.molecules(), "output_%00000008d.pdb" % i)
    ns = t.nsecsElapsed()
    print("...done (took %d ms)" % (0.000001*ns))
