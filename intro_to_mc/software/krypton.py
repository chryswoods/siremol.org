
from Sire.Mol import *
from Sire.MM import *
from Sire.System import *
from Sire.Move import *
from Sire.IO import *
from Sire.Maths import *
from Sire.Units import *
from Sire.Vol import *

# Set the number of atoms in the box
n_atoms = 25

# Set the number of Monte Carlo moves to perform
num_moves = 100000

# Set the size of the box
box_size = ( 15.0*angstrom, 15.0*angstrom, 15.0*angstrom )

# The maximum amount that the atom can be translated by
max_translate = 0.5*angstrom

# Simulation temperature
temperature = 298.15*kelvin

# Simulation pressure
pressure = 1 * atm

# Lennard Jones parameters for the atoms
# (these are the OPLS parameters for Krypton)
sigma = 3.624*angstrom
epsilon = 0.317*kcal_per_mol

# Now create a 'MoleculeGroup' container to hold
# all of the krypton atoms
mols = MoleculeGroup("krypton")

# Create a random number generator
rangen = RanGenerator()

# Now create and add all of the atoms
for i in range(0,n_atoms):
    # create a new krypton atom that is part of a krypton molecule
    krypton = Molecule("krypton").edit() \
                                 .add(CGName("1")) \
                                 .add(AtomName("Kr")) \
                                 .commit()

    # randomly generate the atom's coordinates
    coords = Vector( rangen.rand(0,box_size[0].value()),
                     rangen.rand(0,box_size[1].value()),
                     rangen.rand(0,box_size[2].value()) )

    # create the charge (0) and LJ parameters for the atom
    charge = 0 * mod_electron
    lj = LJParameter(sigma, epsilon)

    # now give the krypton atom its coordinates, charge and LJ 
    # values
    krypton = krypton.edit() \
                     .setProperty("coordinates", coords) \
                     .setProperty("charge", charge) \
                     .setProperty("LJ", lj) \
                     .molecule().commit()

    mols.add(krypton)

# create the periodic box space for the atoms
box = PeriodicBox( Vector(box_size[0].value(),
                          box_size[1].value(),
                          box_size[2].value()) )

# create a forcefield to calculate the intermolecular coulomb and LJ (CLJ)
# energy between all krypton atoms
interff = InterCLJFF("CLJ")
interff.setProperty("space", box)
interff.add(mols)

# create a simulation system to hold the forcefield and atoms
system = System()
system.add(interff)
system.add(mols)
system.setProperty("space", box)

# add a wrapper that wraps the atoms back into the box
system.add( SpaceWrapper( Vector(0), mols ) ) 

# create rigid body translation moves for the atoms
rb_moves = RigidBodyMC(mols)
rb_moves.setMaximumTranslation(max_translate)
rb_moves.setTemperature(temperature)

# create volume moves to change the box size
vol_moves = VolumeMove(mols)
vol_moves.setMaximumVolumeChange( mols.nMolecules() * 0.1 * angstrom3 )
vol_moves.setTemperature(temperature)
vol_moves.setPressure(pressure)

# group these two moves together
moves = WeightedMoves()
moves.add( rb_moves, mols.nMolecules() )
moves.add( vol_moves, 1 )

# print the initial energy and coordinates
print("0:   %s" % system.energy())
PDB().write(system.molecules(), "output000000.pdb") 

# now run the simulation in blocks of 1000 moves
nmoves = 0
while nmoves < num_moves:
    system = moves.move(system, 1000, False)
    nmoves += 1000

    # print out the energy and coordinates every 1000 moves
    print("%s:   %s" % (nmoves, system.energy()))
    print(moves)

    PDB().write(system.molecules(), "output%000006d.pdb" % nmoves)

print("Complete!")
