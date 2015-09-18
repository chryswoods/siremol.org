
from Sire.IO import *
from Sire.System import *
from Sire.MM import *
from Sire.Mol import *
from Sire.Move import *
from Sire.Vol import *
from Sire.Maths import *
from Sire.Units import *

from Sire.Tools import AmberLoader

## Simple script to load up the protein from l7n.top/.crd
## and to create a System that can be used for Monte Carlo
## simulation

# Load the molecules and the periodic box from the crd/top files
(mols, space) = Amber().readCrdTop("l7n.crd", "l7n.top")

# extract the protein molecule (molecule with residue called "ALA")
protein_mol = mols[ MolWithResID("ALA") ].molecule()

# Create the 'protein' molecule group
protein = MoleculeGroup("protein")

# add the protein molecule to this group
protein.add( protein_mol )

# Create a system to hold the system to be simulated
system = System()

# Add the protein to the system
system.add(protein)

# create a forcefield to calculate the intramolecular
# Coulomb and Lennard-Jones energies of the protein (CLJ)
cljff = IntraFF("cljff")

# Use a shift-electrostatics with a 10 angstrom cutoff
cljff.setCLJFunction( CLJIntraShiftFunction(10*angstrom) )

# Add the protein
cljff.add(protein)

# Now also add a forcefield to calculate the intramolecular
# bond, angle and dihedral energy of the protein
intraff = InternalFF("intraff")

# Add the protein
intraff.add(protein)

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
system.add( SpaceWrapper(Vector(0), protein) )
system.applyConstraints()

# Save a binary representation of the system
# to the file "protein.s3"
import Sire.Stream
Sire.Stream.save( system, "protein.s3" )
