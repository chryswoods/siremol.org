
# Sampling the Ligand - Intramolecular Moves

Rigid body moves are all you need to sample small molecules, such as small solvents like water. However, they are not enough on their own to sample larger molecules, such as ligands. To fully sample a ligand you need to randomly vary the bonds, angles and dihedrals in the molecule. You can do this using intramolecular Monte Carlo moves.

***

## Bond Moves

The script `bond.py` performs a Monte Carlo simulation which only samples the bonds of a ligand called L7N. Take a look at this script by typing;

```
nano bond.py
```

The script starts similarly to `rigidbody.py` from the last page, with the beginning of the script used to load up the Sire python modules and to load the molecular system containing the ligand from the s3 file called `l7n.s3` (this was created from the Amber topology / coordinate files `l7n.top` and `l7n.crd` that contain the complete solvated protein / ligand system. The script `make_l7n.py` was used to extract the ligand from the complex and to save it into the s3 file called `l7n.s3`).

```python
from Sire.Mol import *
from Sire.MM import *
from Sire.IO import *
from Sire.System import *
from Sire.Maths import *
from Sire.Units import *

import Sire.Stream
import math

## Set the maximum amount to change each bond
max_delta = 0.05 * angstrom

## Set the temperature
temperature = 298.15 * kelvin

## Load the ligand from the Sire restart file
system = Sire.Stream.load("l7n.s3")
```

As with all Monte Carlo moves, we have to specify the maximum amount to move, and in this case, the variable `max_delta` above is used to store the maximum amount by which we will change an individual bond.

Next, we need to find all of the bonds that we want to sample. We do this by selecting the ligand from the system using

```python
## pick out the ligand molecule
ligand = system[ MolWithResID("L7N") ].molecule()
```

This picks out the `.molecule()` in `system` that contains a residue with name `L7N` (which is our ligand - the selector object `MolWithResID()` searches for molecules with the specified residue identification).

Next, we use the `connectivity` property of the molecule to find and then count all of the bonds in the ligand using;

```python
## Get the list of all bonds from the ligand's
## 'connectivity' property
bonds = ligand.property("connectivity").getBonds()

## Get the number of bonds
nbonds = len(bonds)
```

After creating a random number generator (`RanGenerator`) we define the `mcMove()` function that is used to perform the bond move. This is very similar to the `mcMove()` function in `rigidbody.py`. The only difference is that instead randomly selecting a water and then randomly translating or rotating that water, we now randomly select a bond and randomly change the length of that bond. This is performed using the lines;

```python
    ## randomly choose a bond to move
    bondid = bonds[ rangen.randInt(0,nbonds-1) ]

    print("\nRandomly chosen bond %s" % bondid)

    ## randomly choose an amount to move the bond
    delta = rangen.rand(-max_delta.value(), max_delta.value()) * angstrom

    print("Randomly changing the bond by %s" % delta)

    ## change the bond
    new_ligand = ligand.move().change(bondid, delta).commit()
```

You can see that that you can change a bond in a molecule using the `.move().change()` function and passing in the ID of the bond to change, and the amount by which you want to change it. If you want more detail on how `.move().change()` works, please look at the description of bond moves in [this PDF file](https://docs.google.com/file/d/0B_KkGMZ8ACfaa2k4eVljODN3X1k/edit).

Before running this script, remove the output PDB files from previous scripts using;

```
rm output*.pdb
```

Run the `bond.py` script using the command;

```
$SIRE/bin/python bond.py
```

You should see something like

```
Block 1

Block 1, Move 1

Randomly chosen bond Bond( AtomIdx(34), AtomIdx(36) )
Randomly changing the bond by 0.0364112 angstrom
Change in energy = 0.424867 kcal mol-1
exp( -dE / kT ) = 0.4881692943577321
Random number = 0.983842958459594
exp(-dE / kT) < random(0,1), so MC move rejected.

Block 1, Move 2

Randomly chosen bond Bond( AtomIdx(49), AtomIdx(50) )
Randomly changing the bond by -0.0277991 angstrom
Change in energy = 0.268045 kcal mol-1
exp( -dE / kT ) = 0.6360952185153848
Random number = 0.188391410556713
exp(-dE / kT) >= random(0,1), so MC move accepted.

Block 1, Move 3

Randomly chosen bond Bond( AtomIdx(9), AtomIdx(10) )
Randomly changing the bond by -0.0400429 angstrom
Change in energy = -0.0971774 kcal mol-1
exp( -dE / kT ) = 1.1782338064295677
Random number = 0.2693242259019344
exp(-dE / kT) >= random(0,1), so MC move accepted.

etc. etc.
```

The format is identical to that output by `rigidbody.py`. You can also visualise the trajectory by typing

```
vmd output*.pdb
```

* Does the VMD movie show that you are sampling the bonds well? If you know how, select one of the bonds and use VMD to graph the bond length versus move number. Have you run enough Monte Carlo moves to equilibrate the bond?

* Try changing the `max_delta` that specifies the maximum amount to change a bond. What happens if you make this value larger? Or smaller? Why do you think that this is a much smaller value that the maximum amount by which we translated water molecules in `rigidbody.py`?

***

## Angle Moves

The script `angle.py` performs a Monte Carlo simulation which only samples the angles of the ligand called L7N. Take a look at this script by typing;

```
nano angle.py
```

You should see that it is very similar to `bond.py`, where the differences are;

```python
## Get the list of all angles from the ligand's
## 'connectivity' property
angles = ligand.property("connectivity").getAngles()

## Get the number of angles
nangles = len(angles)
```

where we use the `connectivity` property to get the list and number of angles in the ligand, and in `mcMove()`, where,

```python
    ## randomly choose an angle to move
    angleid = angles[ rangen.randInt(0,nangles-1) ]

    print("\nRandomly chosen angle %s" % angleid)

    ## randomly choose an amount to move the angle
    delta = rangen.rand(-max_delta.to(degrees), max_delta.to(degrees)) * degrees

    print("Randomly changing the angle by %s" % delta)

    ## change the angle
    new_ligand = ligand.move().change(angleid, delta).commit()
```

we randomly choose an angle to move, randomly choose an angle by which to move it, and then actually change that angle using `.move().change()`. If you want to know how `.move().change()` works please take a look at the description of angle moves in [this PDF file](https://docs.google.com/file/d/0B_KkGMZ8ACfaa2k4eVljODN3X1k/edit).

Remove the output from `bond.py` using

```
rm output*.pdb
```

and then run the `angle.py` script using

```
$SIRE/bin/python angle.py
```

The output has the same format as `bond.py` and you can visualise the trajectory using

```
vmd output*.pdb
```

* Does the VMD movie show that you are sampling the angles well? If you know how, select one of the angles and use VMD to graph the angle size versus move number. Have you run enough Monte Carlo moves to equilibrate the angle?

* Try changing the `max_delta` that specifies the maximum amount to change an angle. What happens if you make this value larger? Or smaller? Why do you think is a sensible value for `max_delta` for this ligand?

***

## Dihedral Moves

The script `dihedral.py` performs a Monte Carlo simulation which only samples the (shock horror!) dihedrals of the ligand called L7N. Take a look at this script by typing;

```
nano dihedral.py
```

You should see that it is very similar to `bond.py` and `angle.py`, where the differences are;

```python
## Get the list of all dihedrals from the ligand's
## 'connectivity' property
dihedrals = ligand.property("connectivity").getDihedrals()

## Get the number of dihedrals
ndihedrals = len(dihedrals)
```

where we use the `connectivity` property to get the list and number of dihedrals in the ligand, and in `mcMove()`, where,

```python
    ## randomly choose a dihedral to move
    dihedralid = dihedrals[ rangen.randInt(0,ndihedrals-1) ]

    print("\nRandomly chosen dihedral %s" % dihedralid)

    ## randomly choose an amount to move the dihedral
    delta = rangen.rand(-max_delta.to(degrees), max_delta.to(degrees)) * degrees

    print("Randomly changing the dihedral by %s" % delta)

    ## change the dihedral - either change the whole dihedral
    ## or just change the specified dihedral
    if rangen.randBool():
        new_ligand = ligand.move().change(dihedralid, delta).commit()
    else:
        center_bond = BondID(dihedralid.atom1(), dihedralid.atom2())
        new_ligand = ligand.move().change(center_bond, delta).commit()
```

we randomly choose a dihedral to move, randomly choose an angle by which to move it, and then actually change that dihedral using `.move().change()`. If you want to know how `.move().change()` works please take a look at the description of dihedral moves in [this PDF file](https://docs.google.com/file/d/0B_KkGMZ8ACfaa2k4eVljODN3X1k/edit).

Notice in this case, that we had a choice of two different ways of moving the dihedral. We could either rotate just the atoms specified in the `dihedral` by passing in the entire `dihedralid` to `.move().change()`. Or, we could rotate all atoms that are either side of the bond in the center of the dihedral by passing in this central `center_bond` Bond ID to `.move().change()`. We randomly choose between these two options by telling our `RanGenerator` random number generator to randomly generate `True` or `False` using `rangen.randBool()`.

Remove the output from `angle.py` using

```
rm output*.pdb
```

and then run the `dihedral.py` script using

```
$SIRE/bin/python dihedral.py
```

The output has the same format as `bond.py` and `angle.py` and you can visualise the trajectory using

```
vmd output*.pdb
```

* Does the VMD movie show that you are sampling the dihedrals well? If you know how, select one of the dihedrals and use VMD to graph the dihedral size versus move number. Have you run enough Monte Carlo moves to equilibrate the dihedral?

* Try changing the `max_delta` that specifies the maximum amount to change a dihedral. What happens if you make this value larger? Or smaller? Why do you think is a sensible value for `max_delta` for this ligand?

* [OPTIONAL/ADVANCED] What is the affect of the choice of rotating the entire dihedral, or rotating around the central bond of the dihedral? You can experiment with this by changing the line `if rangen.randBool():` to `if True:` if you want a simulation where you only sample the entire dihedral, or to `it False:` if you want a simulation where you only sample around the central bond of the dihedral. How does this affect the quality of sampling? How does this affect the choice of `max_delta` and the acceptance ratio of the moves?

***

## Internal Moves

As was the case for `rigidbody.py`, the above scripts are too slow to allow sufficient sampling of the internal degrees of freedom (bonds, angles and dihedrals) or a ligand. Sire comes with a C++ object, called `InternalMove` that can be used to efficiently perform large numbers of internal (bond, angle and dihedral) moves on a molecule. This is demonstrated in the script `internalmove.py`, which is copied below;

```python

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

    internalmove.move(system, 250)

    # print out the energy, and number of accepted / rejected move
    print("Energy %s, nAccepted = %s, nRejected = %s" % \
          (system.energy(), internalmove.nAccepted(), 
           internalmove.nRejected()) )
    
    # print out a PDB of the coordinates - align the ligand
    # against the first frame
    ligand = system[MolWithResID("L7N")].molecule()
    ligand = ligand.move().align(first_ligand).commit()
    PDB().write(ligand, "output_%00000008d.pdb" % i)
```

The main change to the `bond.py`, `angle.py` and `dihedral.py` scripts is that we have replaced `mcMove()` with the creation of `internalmove`, which is a C++ object of type `InternalMove`. This is a C++ Monte Carlo move object that can efficiently perform bond, angle and dihedral moves on molecules. In this case, we have told it to perform these moves on molecules contained in the `ligand` molecule group in the molecular system. 

`InternalMove` needs to be told how much it can randomly change each bond, angle and dihedral. This information is provided by the `flexibility` property of a molecule. To generate this property, we must put these maximum deltas into a `params` dictionary parameter object, and then push these parameters into Sire using `Parameter.push()`. The function `generateFlexibility()` which comes with the `AmberLoader` module in Sire is then used to generate the flexibility object. This is passed into the ligand by calling `.edit().setProperty()`, where we set the `flexibility` property of the ligand to equal the `flexibility` object returned by `generateFlexibility()`.

Run the script by typing;

```
$SIRE/bin/python internalmove.py
```

This will run fifty blocks of 250 internal moves. The output is very similar to that for `rigidbodymd.py`, and you can visualise the trajectory in VMD by typing;

```
vmd output*.pdb
```

* What is the acceptance ratio of the simulation? Is this in the acceptable range of 40%-60%?
* Does the molecule look to be well sampled in VMD?
* What is the affect of changing the maximum deltas for the bond, angle and dihedral moves?
* The `max_num_move` variable specifies the number of bonds, angles and dihedrals that can be changed in a single move. At the moment, this is equal to 1. This means that each move only involves changing a single, randomly selected bond, angle or dihedral. Try increasing this number so that multiple random bonds, angles and dihedrals are changed per move. How does this affect the sampling you see in VMD? How does this affect the acceptance ratio of the move?

***

# [Previous](rigid.md) [Up](README.md) [Next](backbone.md)