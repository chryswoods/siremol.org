
from Sire.IO import *
from Sire.System import *
from Sire.MM import *
from Sire.Mol import *
from Sire.Move import *
from Sire.Vol import *
from Sire.Maths import *
from Sire.Units import *
from Sire.ID import *
from Sire.Qt import *
from Sire.Config import *

from Sire.Tools import Parameter
from Sire.Tools import AmberLoader

import os

## Simple script to load up all the molecules from l7n.top/.crd
## and to create a System that can be used for Monte Carlo
## simulation

## Specify the maximum amount to move the
## bonds, angles and dihedrals
max_delta_bond = 0.02 * angstrom
max_delta_angle = 1.0 * degrees
max_delta_dihedral = 2.0 * degrees

## specify the maximum number of bonds,
## angles and dihedrals to move per move
max_num_move = 1

# set the maximum delta parameters
params = {}
params["bond flex"] = max_delta_bond
params["angle flex"] = max_delta_angle
params["dihedral flex"] = max_delta_dihedral
params["h dihedral flex"] = max_delta_dihedral
params["maxvar"] = max_num_move
Parameter.push(params)

# Load the molecules and the periodic box from the crd/top files
(mols, space) = Amber().readCrdTop("l7n.crd", "l7n.top")

# extract the ligand molecule (molecule with residue called "L7N")
ligand_mol = mols[ MolWithResID("L7N") ].molecule()

# auto-generate the flexibility for the ligand
flexibility = AmberLoader.generateFlexibility(ligand_mol)

# attach this flexibility to the ligand using the 'flexibility' property
ligand_mol = ligand_mol.edit() \
                       .setProperty("flexibility", flexibility) \
                       .commit()

mols.update(ligand_mol)

# extract the protein molecule (molecule with residue called "ALA")
protein_mol = mols[ MolWithResID("ALA") ].molecule()

# auto-generate the z-matrix for the protein
zmat_maker = ZmatrixMaker()
zmat_maker.loadTemplates( os.path.join(parameter_directory, "amber.zmatrices") )
protein_mol = zmat_maker.applyTemplates(protein_mol)

mols.update(protein_mol)

# Create the 'ligand' molecule group
ligand = MoleculeGroup("ligand")

# Add the ligand molecule to this group
ligand.add(ligand_mol)

# Create the 'protein' molecule group
protein = MoleculeGroup("protein")

# add the protein molecule to this group
protein.add( protein_mol )

# Create the 'residues' molecule group
residues = MoleculeGroup("residues")

# add the protein residues to this group
for residue in protein_mol.residues():
     residues.add(residue)

# Create the 'backbones' molecule group
backbones = MoleculeGroup("backbones")

# the extra atoms moved as part of a backbone move
hn_atoms = AtomName("N", CaseInsensitive) * AtomName("H", CaseInsensitive) * \
           AtomName("HN", CaseInsensitive) * AtomName("HN1", CaseInsensitive) * \
           AtomName("HN2", CaseInsensitive) * AtomName("HN3", CaseInsensitive)

# Add all of the protein backbones to this group
for i in range(0, protein_mol.nResidues()):
    res = ResIdx(i)

    ## Now select the residue, plus the neighbouring N atom
    ## (and deselect our N atom)
    atoms = protein_mol.select(res).selection()

    N = protein_mol.atom( res + AtomName("N") )
   
    if res.value() < (protein_mol.nResidues()-1):
        try:
            atoms.deselect( hn_atoms + res )
        except:
            pass

    if res.value() > 0:
        try:
            atoms.select( hn_atoms + ResIdx(res.value()+1) )
            N = protein_mol.atom( ResIdx(res.value()-1) + AtomName("N") )
        except:
            pass

    backbones.add( PartialMolecule(protein_mol, atoms) )

# now create a 'water' group
water = MoleculeGroup("water")

# add all of the remaining molecules
for i in range(0, mols.nMolecules()):
    mol = mols[MolIdx(i)].molecule()

    if mol.number() != protein_mol.number() and \
       mol.number() != ligand_mol.number():
         water.add(mol)

# now create the 'all' group that contains all molecules
all = MoleculeGroup("all")
all.add(mols)

# Create a system to hold the system to be simulated
system = System()

# Add the 'all' group to the system
system.add(all)

# Add the protein to the system
system.add(protein)
system.add(residues)
system.add(backbones)

# Add the ligand to the system
system.add(ligand)

# Add the waters to the system
system.add(water)

# create a forcefield to calculate the intramolecular
# Coulomb and Lennard-Jones energies of the protein and ligand (CLJ)
intra_cljff = IntraFF("intra_cljff")

# Use a shift-electrostatics with a 10 angstrom cutoff
intra_cljff.setCLJFunction( CLJIntraShiftFunction(10*angstrom) )
intra_cljff.setProperty("space", space)

# Add the protein and ligand
intra_cljff.add(protein)
intra_cljff.add(ligand)

# Now also add a forcefield to calculate the intramolecular
# bond, angle and dihedral energy of the protein and ligand
intraff = InternalFF("intraff")

# Add the protein and ligand
intraff.add(protein)
intraff.add(ligand)

# Now create a forcefield to calculate the intermolecular
# energy between all molecules
inter_cljff = InterFF("inter_cljff")

# Use a shift-electrostatics with a 10 angstrom cutoff
inter_cljff.setCLJFunction( CLJShiftFunction(10*angstrom) )
inter_cljff.setProperty("space", space)

# Add the protein, ligand and water
inter_cljff.add(protein)
inter_cljff.add(ligand)
inter_cljff.add(water)

# Add the forcefields to the system
system.add(intra_cljff)
system.add(intraff)
system.add(inter_cljff)

# Set the expression used to calculate the total energy
# of the system
system.setComponent( system.totalComponent(),
                     intra_cljff.components().total() + 
                     intraff.components().total() +
                     inter_cljff.components().total() )

# Tell the system about the periodic box
system.setProperty("space", space)

# now wrap everything so that the ligand is in the center of the box
system.add( SpaceWrapper(ligand_mol.evaluate().center(), all) )
system.applyConstraints()
system.removeAllConstraints()

# Save a binary representation of the system
# to the file "system.s3"
import Sire.Stream
Sire.Stream.save( system, "system.s3" )
