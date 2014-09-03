
from Sire.IO import *
from Sire.System import *
from Sire.MM import *
from Sire.Mol import *
from Sire.Move import *
from Sire.Vol import *
from Sire.Maths import *
from Sire.Units import *

from Sire.Tools import AmberLoader

## Simple script to load up the L7N ligand from l7n.top/.crd
## and to create a System that can be used for Monte Carlo
## simulation

# Load the molecules and the periodic box from the crd/top files
(mols, space) = Amber().readCrdTop("l7n.crd", "l7n.top")

# extract the ligand molecule (molecule with residue called "L7N")
ligand_mol = mols[ MolWithResID("L7N") ].molecule()

# auto-generate the flexibility for the ligand
flexibility = AmberLoader.generateFlexibility(ligand_mol)

# attach this flexibility to the ligand using the 'flexibility' property
ligand_mol = ligand_mol.edit() \
                       .setProperty("flexibility", flexibility) \
                       .commit()

# Create the 'ligand' molecule group
ligand = MoleculeGroup("ligand")

# add the ligand molecule to this group
ligand.add( ligand_mol )

# Create a system to hold the system to be simulated
system = System()

# Add the ligand to the system
system.add(ligand)

# create a forcefield to calculate the intramolecular
# Coulomb and Lennard-Jones energies of the ligand (CLJ)
cljff = IntraFF("cljff")

# Use a shift-electrostatics with a 10 angstrom cutoff
cljff.setCLJFunction( CLJIntraShiftFunction(10*angstrom) )

# Add the ligand
cljff.add(ligand)

# Now also add a forcefield to calculate the intramolecular
# bond, angle and dihedral energy of the ligand
intraff = InternalFF("intraff")

# Add the ligand
intraff.add(ligand)

# Add the forcefields to the system
system.add(cljff)
system.add(intraff)

# Set the expression used to calculate the total energy
# of the system
system.setComponent( system.totalComponent(),
                     cljff.components().total() + 
                     intraff.components().total() )

# Tell the system about the periodic box
system.setProperty("space", space)
system.add( SpaceWrapper(Vector(0), ligand) )
system.applyConstraints()

# Save a binary representation of the system
# to the file "l7n.s3"
import Sire.Stream
Sire.Stream.save( system, "l7n.s3" )
