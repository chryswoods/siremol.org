
# Sampling it all - Weighting Moves

Up to now, you have only been performing one type of move at a time. The advantage of Monte Carlo is that you can mix and match lots of different Monte Carlo moves together into a single simulation. You have complete power to choose which types of Monte Carlo move you want to perform, e.g. if you don't want to keep bond lengths fixed, then you can choose not to include any bond moves. Equally, if you want to keep your water molecules rigid, then only sample them using rigid body translation and rotation moves.

Typically, for an explicit solvent protein-ligand simulation you would use;

* Rigid body translation and rotation moves for the water,
* A combination of rigid body translation and rotation moves with internal (bond, angle and dihedral) moves for the ligand, and
* A combination of rigid body translation and rotation moves for the protein backbone with internal (bond, angle and dihedral) moves for the sidechains

This would allow you to sample from the NVT (canonical) ensemble. If you wanted to sample from the NPT (isothermal-isobaric) ensemble then you would also add;

* Volume moves that change the size of the periodic box and move all molecules, with the center of the box centered on the center of the ligand.

Once you have chosen your suite of moves, you have to choose the relative probability of choosing to perform each move. The script `weightedmove.py` shows how you can do this. Take a look at the script by typing;

```
nano weightedmove.py
```

The script starts by loading the entire protein / ligand / water molecular system from the s3 file `system.s3` (this was prepared from `l7n.top` and `l7n.crd` using `make_system.py`). The script then creates the suite of moves;

```python
## create an InternalMove that will move the bonds,
## angles and dihedrals of the molecules in group 'ligand'
ligand_internalmove = InternalMove( system[MGName("ligand")] )

## create a Rigid Body move that will translate and rotate the ligand
ligand_rbmove = RigidBodyMC( system[MGName("ligand")] )
ligand_rbmove.setMaximumTranslation(0.05*angstrom)
ligand_rbmove.setMaximumRotation(0.25*degrees)
```

creates the internal and rigid body moves for the ligand,

```python
## create a Rigid Body move that will translate and rotate the water
## molecules
water_rbmove = RigidBodyMC( system[MGName("water")] )
water_rbmove.setMaximumTranslation(0.15*angstrom)
water_rbmove.setMaximumRotation(15*degrees)
```

creates the rigid body moves for the water, and

```python
## create a ZMatMove to move the bonds, angles and dihedrals
## in each of the residues in the protein (this is similar to
## an internal move, but can use pre-defined templates for 
## each of the amino acids to decide how to move the sidechains)
protein_internalmove = ZMatMove( system[MGName("residues")] )

## create a Rigid Body move to move each protein residue backbone
protein_backbonemove = RigidBodyMC( system[MGName("backbones")] )
protein_backbonemove.setMaximumTranslation(0.01*angstrom)
protein_backbonemove.setMaximumRotation(1*degrees)
```

creates the internal sidechain and rigid body backbone moves for the protein.

We then combine these moves together into a `WeightedMoves` object called `moves`, that stores each move together with the probability with which it should be chosen. The line

```python
## add the water moves, weighted by the number of water molecules
moves.add(water_rbmove, system[MGName("water")].nMolecules())
```

adds the water rigid body moves to `moves`, and assigns this move type a weight equal to the number of water molecules in the molecular system. Next,

```python
## add the ligand translation/rotation moves with a weight of 5 (we want to move
## the ligand a lot more than the water)
moves.add(ligand_rbmove, 5)

## add the ligand internal moves with the same weight at its
## translation/rotation moves
moves.add(ligand_internalmove, 5)
```

adds in the ligand rigid body and internal moves and assigns them a weight of 5. Next, 

```python
## add the residue internal moves with a weight of half of the number
## of residues
moves.add(protein_internalmove, 0.5 * system[MGName("residues")].nViews())

## add the residue backbone moves with a weight of half the number
## of movable backbones
moves.add(protein_backbonemove, 0.5 * system[MGName("backbones")].nViews())
```

the protein backbone and sidechain moves are added and assigned a probability that is 0.5 times the number of residues in the protein.

The line (later in the script);

```python
    system = moves.move(system, 5000, False)
```

then tells this `moves` object to perform 5000 moves on the molecular system `system`, and to return the result (which is copied back to `system`). The `False` is a flag telling `moves` that this is equilibration and that we don't need to record any statistics or energies during the moves.

What `moves.move()` does is to randomly choose which move to perform. It does this by calculating the probability of performing each move based on the weight that was assigned when the move was added to the set. The probability of each move is calculated as the weight of the move divided by the sum of the weights of all moves. In this case;

* The number of water molecules is 13976, so its weight is 13976
* The number of two ligand moves both have a weight of 5
* The number of protein residues is 261, so the sidechain and backbone moves both have a weight of 130.5.

The sum of all weights is 14247, so the probability of each move type is;

* Water moves: 98.1%
* Ligand moves: both equal to 0.035%
* Protein moves: both equal to 0.92%

These numbers are chosen to ensure that each cycle of Monte Carlo is roughly balanced, i.e. each cycle will, on average, move every water molecule once, every protein residue once, and the ligand ten times (we increase the probability of the ligand as, typically, the ligand is of interest and so increasing its probability can lead to more efficient convergance of ligand properties, e.g. like binding free energies).

An alternative way to look at this is that, on average, for every one protein backbone residue move, there will be one protein sidechain move, two water moves and ten ligand intramolecular moves and ten ligand rigid body moves.

Run this script using the command;

```
$SIRE/bin/python weightedmove.py
```

This will take about 5 minutes to complete and will print out something like this;

```
Block 1
Energy -136936 kcal mol-1 (took 5419 ms)
WeightedMoves{
  1 : weight == 13976
       RigidBodyMC( maximumTranslation() = 0.15 A, maximumRotation() = 15 degrees nAccepted() = 2197 nRejected() = 2704 )
  2 : weight == 5
       RigidBodyMC( maximumTranslation() = 0.05 A, maximumRotation() = 0.25 degrees nAccepted() = 2 nRejected() = 0 )
  3 : weight == 5
       InternalMove( nAccepted() = 0 nRejected() == 0 )
  4 : weight == 130.5
       ZMatMove( nAccepted() = 17 nRejected() == 29 )
  5 : weight == 130.5
       RigidBodyMC( maximumTranslation() = 0.01 A, maximumRotation() = 1 degrees nAccepted() = 38 nRejected() = 13 )
}
Writing coordinates...
...done (took 2217 ms)

Block 2
Energy -136933 kcal mol-1 (took 4195 ms)
etc. etc.
```

The script will perform 50 blocks of 5000 moves (so 250000 moves in total, which is not too bad for five minutes).

As you can see, you will get the energy at the end of each block of moves, how long (in milliseconds) it took to perform the moves, and also the breakdown of the number of accepted and rejected moves for each move type.

* Do the number of moves attempted for each move match up with your expectation based on their weights?
* Where is the majority of the computational expense of the calculation being spent? How could you speed up this simulation?

You can visualise the trajectory by typing;

```
vmd output*.vmd
```

* Do you think that the sampling is balanced? Does the protein appear to be moving more or less than the ligand or water? How could you balance the sampling?

As you can see, the majority of the simulation time is being spent sampling the thousands of water molecules, and sampling the hundreds of protein residues. Most of this time is spent sampling water molecules and protein residues that are far from the ligand. If you know that you are only interested in the ligand, it is possible to speed up Monte Carlo simulations by applying techniques (called 'preferential sampling') that bias the choice of water or residue to sample such that those closest to the ligand are sampled more often. This allows you to reduce the weighting of the protein and water moves. It is also possible to apply what is known as a 'reflection sphere' boundary condition that, effectively, ensures that you only sample water molecules and protein residues within a fixed radius of the ligand. This can drastically reduce the number of sampled water molecules and protein residues, allowing you to further reduce their weight and thus their computational cost (as well as reducing the total number of moves needed to complete one 'cycle' of Monte Carlo). Beyond that, the best way to reduce the cost is to remove the explicit solvent and use an implicit solvent model such as Generalised Born (GB) or Poisson Boltzmann (PB). This speedup would, of course, come at the cost of the accuracy of the model.

***

# [Previous](backbone.md) [Up](README.md) [Next](relative.md)
