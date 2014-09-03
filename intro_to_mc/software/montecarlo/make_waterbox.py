
from Sire.IO import *
from Sire.System import *
from Sire.MM import *
from Sire.Mol import *
from Sire.Move import *
from Sire.Vol import *
from Sire.Maths import *
from Sire.Units import *

## Simple script to load up a water box from waterbox.top/.crd
## and to create a System that can be used for Monte Carlo
## simulation of these waters

# Load the waters and the periodic box from the crd/top files
(waters, space) = Amber().readCrdTop("waterbox.crd", "waterbox.top")

# Rename the 'waters' group to 'water'
waters.setName("water")

# Create a system to hold the system to be simulated
system = System()

# Add the waters to the system
system.add(waters)

# create a forcefield to calculate the intermolecular
# Coulomb and Lennard-Jones energies of the waters (CLJ)
cljff = InterFF("cljff")

# Use a shift-electrostatics with a 10 angstrom cutoff
cljff.setCLJFunction( CLJShiftFunction(10*angstrom) )

# Add the waters and set the cutoff to 10 angstroms
cljff.add(waters)

# Add the forcefield to the system
system.add(cljff)

# Tell the system about the periodic box
system.setProperty("space", space)
system.add( SpaceWrapper(Vector(0), waters) )
system.applyConstraints()

# Save a binary representation of the system
# to the file "waterbox.s3"
import Sire.Stream
Sire.Stream.save( system, "waterbox.s3" )
