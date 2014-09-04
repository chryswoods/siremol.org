
from Sire.Mol import *
from Sire.MM import *
from Sire.IO import *
from Sire.ID import *
from Sire.System import *
from Sire.Maths import *
from Sire.Units import *

import Sire.Stream
import math

## Set the maximum amount to change each angle
max_delta = 2.5 * degrees

## Set the temperature
temperature = 298.15 * kelvin

## Specify the maximum amount by which to translate
## each residue
max_translation = 0.03 * angstrom

## Specify the maximum amount by which to rotate
## each residue
max_rotation = 1 * degrees

## Load the protein from the Sire restart file
system = Sire.Stream.load("protein.s3")

## create a random number generator for the moves
rangen = RanGenerator()

# the extra atoms moved as part of a backbone move
hn_atoms = AtomName("N", CaseInsensitive) * AtomName("H", CaseInsensitive) * \
           AtomName("HN", CaseInsensitive) * AtomName("HN1", CaseInsensitive) * \
           AtomName("HN2", CaseInsensitive) * AtomName("HN3", CaseInsensitive)

def mcMove(block, nmove):
    print("\nBlock %d, Move %d" % (block,nmove))

    ## calculate the energy before the move
    old_energy = system.energy()

    ## get the version of the protein
    ## currently in the system
    protein = system[ MolWithResID("ALA") ].molecule()

    ## choose a random residue to move (will change the backbone angle)
    res = ResIdx( rangen.randInt(0, protein.nResidues()-1) )

    print("\nRandomly chosen residue %s" % res)

    ## Now choose a random vector by which to translate
    ## the residue
    random_translate = rangen.vectorOnSphere( max_translation.value() )

    ## Now choose a random axis about which to 
    ## rotate the residue molecule
    random_rotate_axis = rangen.vectorOnSphere()

    ## Now choose a random amount by which to rotate
    ## the residue molecule
    random_rotate_angle = rangen.rand(-max_rotation.value(),
                                       max_rotation.value()) * degrees

    print("Randomly translating by %s" % random_translate)
    print("Randomly rotating by %s about %s" % \
               (random_rotate_angle,random_rotate_axis))

    ## Now select the residue, plus the neighbouring N atom
    ## (and deselect our N atom)
    atoms = protein.select(res).selection()

    N = protein.atom( res + AtomName("N") )
   
    if res.value() < (protein.nResidues()-1):
        try:
            atoms.deselect( hn_atoms + res )
        except:
            pass

    if res.value() > 0:
        try:
            atoms.select( hn_atoms + ResIdx(res.value()+1) )
            N = protein.atom( ResIdx(res.value()-1) + AtomName("N") )
        except:
            pass

    ## now get the center of rotation - this is the geometric
    ## center of the bond between the CA and N atoms
    CA = protein.atom( res + AtomName("CA") )

    center = CA.property("coordinates") + \
             0.5*(N.property("coordinates")-CA.property("coordinates"))

    ## now translate and rotate these atoms
    new_protein = PartialMolecule(protein,atoms) \
                         .move() \
                         .rotate( \
                    Quaternion(random_rotate_angle,random_rotate_axis), \
                               center ) \
                         .translate(random_translate).commit().molecule()

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
