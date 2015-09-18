# Part 2: Molecular Dynamics
## Constraining bonds using the SHAKE algorithm

In the last section you saw that the size of the molecular dynamics timestep was limited by the frequency of vibration of bonds involving hydrogen. To overcome this problem, algorithms have been developed that can freeze bonds during a molecular dynamics simulation. One widely used algorithm is called [SHAKE](http://www.sciencedirect.com/science/article/pii/0021999177900985). Other algorithms exist, and are described [here](http://en.wikipedia.org/wiki/Constraint_algorithm).

The aim of SHAKE is to fix any bonds involving hydrogen atoms, while still allowing all of the atoms to move and vibrate. Because the bonds involving hydrogen are not vibrating, the timestep for the molecular dynamics simulation can be increased.

We are now going to turn on SHAKE for the gas phase simulation of zanamivir. Edit the mdconfig file by typing;

```
nano mdconfig
```

and then add the following lines to the end of the file

```
rigidBonds all
rigidTolerance 0.0005
```

The first line tells namd to use SHAKE to constrain the bond length of "all" bonds involving hydrogen. The second line sets the tolerance used for the numerical algorithm used to constrain the bond length. The smaller this tolerance, the more tightly the bond lengths will be constrained. However, the smaller the tolerance, the greater the chance that the numerical algorithm will fail and namd will exit (with a SHAKE error). A tolerance of 0.0005 angstroms is about right for all room temperature biomolecular simulations.

Once you have added the two line, set the timestep to 1 femtosecond and then rerun namd using the command

```
$NAMD/namd2 ++ppn 4 mdconfig
```

Once the simulation has finished, load the trajectory into VMD by typing

```
vmd zan.pdb output.dcd
```

Align the trajectory and then draw a graph of the length of the hydrogen-nitrogen bond that you measured in the last section. Add this graph to the spreadsheet you made in the last section. How does the bond length with SHAKE on compare to the bond length when SHAKE is off?

Once you have finished, you should find that you have produced a graph that looks something similar to this;

![Image of completed spreadsheet](vmd_shake1.jpg)

As you can see, SHAKE has constrained the N-H bond length to a value that is within +/-0.0005 angstroms of the starting bond length (the standard deviation is only 0.0001 angstroms).

* **Now that you have successfully constrained the lengths of bonds involving hydrogen, try to increase the timestep of the simulation. How large can the timestep be? What error do you get when the timestep becomes too large?**

# [Previous](time.md) [Up](README.md) [Next](protein.md)
