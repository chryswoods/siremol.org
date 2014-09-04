
# Sampling the Solvent - Rigid Body Moves

Up to now, you have only performed Monte Carlo moves on single krypton atoms. This was simple, as you were able to randomly move each atom by randomly translating it along the x, y and z axes.

In contrast, Monte Carlo moves for molecules are more complex. This is because each molecule is formed of atoms that are bonded together. Randomly translating individual atoms could lead to high changes in energy. This is because randomly translating individual atoms could change the bond lengths, and angle and dihedral sizes within a molecule to high energy values. Randomly translating individual atoms is also inefficient as it would take a large number of moves to accomplish something as simple as the rotation of the entire molecule.

Over the next few pages we will explore Monte Carlo moves that are designed to efficiently move molecules in a simulation of a solvated protein-ligand complex. We will start by looking at how we could efficiently move the water solvent.

In Monte Carlo simulations we typically view the solvent as being a rigid body. This means that we want to move each solvent molecule as a single, rigid object, and to not change any of the bonds, angles or dihedrals within the solvent. This is achieved by combining random rigid body translations with random rigid body rotations of the entire solvent molecule. This is demonstrated in the script `rigidbody.py`.

Change into the `montecarlo` directory. In this directory you should see `rigidbody.py`. This is a Sire python script that is used to perform rigid body Monte Carlo sampling of water molecules in a periodic box. 

Take a look at the file by typing;

```
nano rigidbody.py
```

The first block of the file...

```python
from Sire.Mol import *
from Sire.Maths import *
from Sire.IO import *
from Sire.Units import *
from Sire.Stream import *

import math
```

...is used to load up the Sire python modules that are used in this script (as well as the standard library `math` module).

The next part...

```python
## Load up the box of water from the Sire restart file
waterbox = load("waterbox.s3")
```

...is used to load up the periodic box of water molecules from a Sire Streamed Save (.s3) file called `waterbox.s3`. This file was created from the Amber format topology/coordinate file pair `waterbox.top` and `waterbox.crd` using the script `make_waterbox.py`.

The next line...

```python
## Get the number of water molecules in the box
nwaters = waterbox.nMolecules()
```

...obtains the number of water molecules that have been loaded by calling the `nMolecules` function on `waterbox`. Next...

```python
## Create a random number generator to generate
## all of the random number we will use
rangen = RanGenerator()
```
...a RanGenerator object is created. This is used to generate the random numbers and random vectors that will be used later in the script. Next, we have to specify the temperature of the Monte Carlo simulation using the line...

```python
## Specify the temperature of the simulation
temperature = 298.15 * kelvin
```

Just as was supplied for the krypton example, we also now need to supply the maximum amount by which we want to translate each water molecule. For krypton, this amount was used to specify the maximum amount to translate each atom. In this case, this amount is used to specify the maximum amount to translate each water molecule.

```python
## Specify the maximum amount by which to translate
## each water
max_translation = 0.15 * angstrom
```

As well as specifying the maximum amount to translate each water, we also need to specify the maximum angle by which we will rotate each water molecule. This is specified using the line;

```python
## Specify the maximum amount by which to rotate
## each water
max_rotation = 15 * degrees
```

The next part of the script defines the function `mcMove`. This is a function that is used to perform a single rigid body translation / rotation move on a single, randomly chosen water molecule. Within `mcMove` the Monte Carlo algorithm is the same as that used for the krypton atoms, except now we translate and rotate a complete water molecule.

First, we calculate the 'old' energy of the water box, before the move, using

```python
    ## Calculate the current energy of the water box
    old_energy = waterbox.energy()
```

Next, we randomly choose one of the water molecules by picking a random number between `0` and `nwaters - 1`.

```python
    ## Choose a water molecule from the box at random
    water_id = rangen.randInt(0, nwaters-1)
    random_water = waterbox[ MolIdx(water_id) ].molecule()

    print("\nRandomly chosen water %s" % water_id)
```

Next, we randomly generate a vector by which to translate the water molecule. This is a random vector chosen to lie within a sphere of radius `max_translation` (the `.value()` function converts the translation into internal units used by Sire).

```
    ## Now choose a random vector by which to translate
    ## the water (any amount up to 0.15 angstroms)
    random_translate = rangen.vectorOnSphere( max_translation.value() )
```

Next, we randomly generate a vector about which we will randomly rotate the water molecule, and a random angle by which to rotate around this vector,

```python
    ## Now choose a random axis about which to 
    ## rotate the water molecule
    random_rotate_axis = rangen.vectorOnSphere()

    ## Now choose a random amount by which to rotate
    ## the water molecule (up to 15 degrees)
    random_rotate_angle = rangen.rand(-max_rotation.value(),
                                       max_rotation.value()) * degrees

    print("Randomly translating by %s" % random_translate)
    print("Randomly rotating by %s about %s" % \
               (random_rotate_angle,random_rotate_axis))
```

Now we use this random translation and rotation to actually translate and rotate the water molecule. We used the `.move()` function on the randomly selected water to first `.rotate()` and then `.translate()` the water molecule. Note that we have to rotate the water molecule before translating it, and also that we must rotate about the center of rotation of the water molecule (obtained using the `.evaluate().center()` function). The rigid body rotation is specified as a `Quaternion`, which is a 4-element vector that uniquely describes a rotation of a set angle around a 3-dimensional vector. Finally, the two moves are committed by calling the `.commit()` function, which returns the moved water as a new object called `moved_water`. The code used to move the water is;

```python
    moved_water = random_water.move() \
                              .rotate( \
                    Quaternion(random_rotate_angle,random_rotate_axis), \
                               random_water.evaluate().center() ) \
                              .translate(random_translate).commit()
```

Once the water has been moved, it has to be passed back to box of water. This is achieved by calling the `.update()` function on `waterbox`,

```python
    ## update the water box with the new coordinates of the water
    waterbox.update(moved_water)
```

We can then calculate the new energy of the water box using

```python
    ## calculate the energy after the move
    new_energy = waterbox.energy()
```

and can then put this into the standard NVT (canonical) Monte Carlo acceptance test, using;

```python
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
        
        # move has been rejected, so we have to move the water
        # back to its old conformation
        waterbox.update(random_water)
```

You can see here that if the move failed, then we use the `.update()` function of `waterbox` to restore the original coordinates of the randomly selected water molecule.

Finally, at the end of the script are a pair of nested loops that are used to perform 500 Monte Carlo moves as 50 blocks of 10 moves;

```python
# perform 50 blocks of 10 moves
for i in range(1,51):
    print("\nBlock %d" % i)

    for j in range(1,11):
        mcMove(i, j)

    # print out a PDB of the coordinates
    PDB().write(waterbox.molecules(), "output_%00000008d.pdb" % i)
```

Here you can see that we are just calling our `mcMove()` function repeatedly (passing in the block and move number), and are then writing out the coordinates of all of the atoms at the end of each block. This is achieved using the `PDB()` object that can write out the molecules to a PDB format file with filename `output????????.pdb`, where `????????` is the block number.

Now that you have taken a look at the script, run it by typing;

```
$SIRE/bin/python rigidbody.py
```

You should see something like this (it will be different as you will have different random numbers);

```
Block 1

Block 1, Move 1

Randomly chosen water 2467
Randomly translating by ( 0.0103531, 0.0233645, 0.147807 )
Randomly rotating by 0.111814 degree about ( 0.0216355, 0.707916, -0.705965 )
Change in energy = 1.12021 kcal mol-1
exp( -dE / kT ) = 0.15096746907575243
Random number = 0.45309103314138277
exp(-dE / kT) < random(0,1), so MC move rejected.

Block 1, Move 2

Randomly chosen water 1935
Randomly translating by ( -0.0798828, -0.115544, -0.0526143 )
Randomly rotating by -0.0431691 degree about ( -0.558803, -0.821672, 0.11222 )
Change in energy = -0.127177 kcal mol-1
exp( -dE / kT ) = 1.2394277172047041
Random number = 0.4478638191818874
exp(-dE / kT) >= random(0,1), so MC move accepted.

Block 1, Move 3

Randomly chosen water 846
Randomly translating by ( -0.0763193, 0.0936943, 0.0888636 )
Randomly rotating by 0.101704 degree about ( -0.591248, -0.782721, -0.194354 )
Change in energy = -0.113767 kcal mol-1
exp( -dE / kT ) = 1.2116907179981249
Random number = 0.9047896966582141
exp(-dE / kT) >= random(0,1), so MC move accepted.

etc. etc.
```

As you can see, complete information about every move is provided. 

* Take a look through the output and see if you can find moves that are rejected. Can you see why the move was rejected? In the case above, the first move was rejected because the random translation / rotation increased the energy by 1.12 kcal mol-1. The exponential of the energy change divided by kT was 0.15. However, the random number used for the Monte Carlo test was greater than this (0.45) and so the move was rejected. Can you find any moves in your simulation where the move was only just rejected? (i.e. the exponential of the energy difference over kT was less than 0.05 greater than the random number). Also, can you find any moves in your simulation where the move resulted in a large increase in energy (greater than 4 kcal mol-1)? What is the exponential of the difference in energy divided by kT in this case? What is the probability that such a move would be accepted?

* Take a look through the output and see if you can find moves that are accepted. Can you see why the move was accepted? In the case above, both moves were accepted because they resulted in the energy decreasing, and thus the exponential of the energy difference divided by kT always being greater than 1. Can you find any moves that were accepted despite the energy decreasing? Can you find any moves that resulted in an energy increase of more than 1 kcal mol-1 that were accepted? What is the probability that a move that results in an increase in energy of 1 kcal mol-1 being accepted?

In addition to printing out information about the moves, this script also prints out the coordinates as a series of PDB files. To view these type;

```
vmd output*.pdb
```

This will play a short movie showing the (small) number of moves that you performed.

As you can see, not a lot of water molecules are moving. This is because the water box contains 2544 water molecules and you performed only 500 moves. This means that over 2000 of the 2544 water molecules will not have been moved.

In Monte Carlo, we use the term 'cycle' to refer to the number of moves required to, on average, move every molecule in the system once. In the case of the water box, there are 2544 water molecules, so one cycle would be 2544 moves. 500 moves is only 0.2 cycles, so is not much. To sample a system well, you need to perform tens or hundreds of thousands of cycles (so, in this case, of the order of tens or hundreds of millions of moves). Our simple python script is too slow to perform this many moves, so Sire comes with a C++ alternative. This is called `RigidBodyMC`, and is a C++ object that can be used in Python to run large numbers of rigid body Monte Carlo moves. You can see it in action in the file `rigidbodymc.py`, which is copied below;

```python

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
```

As you can see, this is very similar to `rigidbody.py`, except now the `mcMove` function has been replaced with the creation of the `RigidBodyMC` object that is called `rb_move`. This is constructed to move molecules within the molecule group called `water` in the `waterbox` (Sire allows you to divide molecules into different named groups - in this case all of the water molecules were placed into a molecule group called `water` in `make_waterbox.py`).

The maximum amount to translate and rotate each water molecule is provided via the `.setMaximumTranslation()` and `.setMaximumRotation()` functions, with the temperature set using `.setTemperature()`. Each move is performed using the `.move()` function, where we pass in the system of molecules to be moved (`waterbox`) and specify the number of moves (`2000`). Then, after we have performed this block of moves, we write out the coordinates to a PDB file as before.

Run this script by typing;

```
$SIRE/bin/python rigidbodymc.py
```

You should see something like this;

```
Block 1
Energy -23164.2 kcal mol-1, nAccepted = 901, nRejected = 1099

Block 2
Energy -23169 kcal mol-1, nAccepted = 1771, nRejected = 2229

Block 3
Energy -23170.8 kcal mol-1, nAccepted = 2620, nRejected = 3380

etc. etc.
```

You can view the trajectory by typing;

```
vmd output*.pdb
```

* Do the individual water molecules translate or rotate much during the (still short) simulation?

* What is the acceptance ratio for the simulation? (number of accepted moves divided by total number of moves). Is this in the acceptable range of 40-60%?

* Try changing the maximum amount by which to translate or rotate the water molecules. How does this change affect the acceptance ratio? How does this change affect how much sampling is visible in the VMD movie?


***

# [Previous](intro.md) [Up](README.md) [Next](intra.md)
